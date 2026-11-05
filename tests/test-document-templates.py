#!/usr/bin/env python3
"""Check Phase 2 project creation and representative XeLaTeX page breaks."""

import argparse
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import unicodedata
import struct
import zlib
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "new-project.py"
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / "scripts"))
import project_generator

VARIANTS = (("letter-fa", "classic"), ("letter-fa", "modern"),
            ("letter-en", "classic"), ("letter-en", "modern"),
            ("resume-en", "article"), ("resume-en", "moderncv"))


def generate(template, dest, style=None):
    command = [sys.executable, str(SCRIPT), "--template", template,
               "--destination", str(dest)]
    if style:
        command.extend(("--style", style))
    return subprocess.run(command, capture_output=True, text=True, errors="replace")


def compile_project(project):
    for _ in range(2):
        result = subprocess.run(
            ["xelatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
            cwd=project, capture_output=True, text=True, errors="replace")
        if result.returncode:
            return result
    return result


def neutral_png(width=10, height=10):
    def chunk(kind, data):
        return (struct.pack(">I", len(data)) + kind + data +
                struct.pack(">I", zlib.crc32(kind + data) & 0xffffffff))
    return (b"\x89PNG\r\n\x1a\n" +
            chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)) +
            chunk(b"IDAT", zlib.compress((b"\x00" + b"\x40\x40\x40" * width) * height)) +
            chunk(b"IEND", b""))


def set_fields(path, values):
    source = path.read_text(encoding="utf-8")
    for name, value in values.items():
        pattern = rf"(\\newcommand\{{\\{re.escape(name)}\}}\{{)[^{{}}]*(\}})"
        source, count = re.subn(pattern, lambda match: match[1] + value + match[2],
                                source)
        if count != 1:
            raise AssertionError(f"Expected one metadata definition for {name}")
    path.write_text(source, encoding="utf-8")


def pdf_text(project):
    result = subprocess.run(["pdftotext", "-layout", "main.pdf", "-"],
                            cwd=project, capture_output=True, text=True,
                            encoding="utf-8", errors="replace")
    if result.returncode:
        raise RuntimeError(result.stderr)
    return result.stdout


def page_count(project):
    result = subprocess.run(["pdfinfo", "main.pdf"], cwd=project,
                            capture_output=True, text=True, errors="replace")
    match = re.search(r"(?m)^Pages:\s+(\d+)\s*$", result.stdout)
    if result.returncode or not match:
        raise RuntimeError(result.stderr or result.stdout)
    return int(match[1])


class DocumentTemplateTests(unittest.TestCase):
    def test_choices_and_required_style(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for template in ("letter-fa", "letter-en"):
                result = generate(template, root / template)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("require --style", result.stderr)
                self.assertFalse((root / template).exists())
            result = generate("resume-en", root / "bad-cv", "classic")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Resume styles", result.stderr)
            self.assertFalse((root / "bad-cv").exists())
            default = root / "default-cv"
            explicit = root / "article-cv"
            self.assertEqual(generate("resume-en", default).returncode, 0)
            self.assertEqual(generate("resume-en", explicit, "article").returncode, 0)
            self.assertEqual((default / "main.tex").read_bytes(),
                             (explicit / "main.tex").read_bytes())
            self.assertFalse((default / ".git").exists())

    def test_standalone_sources_unicode_path_and_existing_destination(self):
        with tempfile.TemporaryDirectory(prefix="plk phase2 ") as tmp:
            root = Path(tmp)
            for template, style in VARIANTS:
                with self.subTest(template=template, style=style):
                    dest = root / f"{template}-{style or 'cv'} نمونه"
                    result = generate(template, dest, style)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertTrue((dest / "main.tex").is_file())
                    self.assertTrue((dest / "config/metadata.tex").is_file())
                    self.assertTrue((dest / "config/fonts.tex").is_file())
                    self.assertTrue((dest / "README.md").is_file())
                    self.assertTrue((dest / "AGENTS.md").is_file())
                    self.assertFalse((dest / ".git").exists())
                    self.assertFalse((dest / ".gitmodules").exists())
                    if template.startswith("letter"):
                        self.assertTrue((dest / "letter-parts.tex").is_file())
                        self.assertTrue((dest / "content/body.tex").is_file())
                        self.assertTrue((dest / "content/final-paragraph.tex").is_file())
                    else:
                        for section in ("education", "experience", "projects",
                                        "skills", "languages", "research", "honors",
                                        "publications"):
                            self.assertTrue((dest / "sections" / f"{section}.tex").is_file())
                        if style == "moderncv":
                            self.assertIn(r"\documentclass[11pt,a4paper,sans]{moderncv}",
                                          (dest / "main.tex").read_text(encoding="utf-8"))
                    keep = dest / "user-file.txt"
                    keep.write_text("preserve", encoding="utf-8")
                    repeat = generate(template, dest, style)
                    self.assertNotEqual(repeat.returncode, 0)
                    self.assertEqual(keep.read_text(encoding="utf-8"), "preserve")

    def test_missing_template_dependency_leaves_no_project(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            kit = root / "kit"
            shutil.copytree(ROOT / "templates/letter-fa", kit / "templates/letter-fa")
            (kit / "templates/letter-fa/common/config/fonts.tex").unlink()
            args = argparse.Namespace(template="letter-fa", style="classic",
                                      destination=str(root / "dest"), offline=False,
                                      git=False, repository_url=None, kit_path=None,
                                      assignment_number=None, question_number="۱")
            with patch.object(project_generator, "KIT", kit):
                with self.assertRaisesRegex(FileNotFoundError, "font configuration"):
                    project_generator.build(args)
            self.assertFalse((root / "dest").exists())

    @unittest.skipUnless(shutil.which("xelatex"), "XeLaTeX unavailable")
    def test_missing_moderncv_class_has_actionable_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "moderncv"
            self.assertEqual(generate("resume-en", dest, "moderncv").returncode, 0)
            # An isolated TeX input path hides installed classes without changing TeX Live.
            result = subprocess.run(
                ["xelatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
                cwd=dest, env=dict(os.environ, TEXINPUTS=str(dest)),
                capture_output=True, text=True, errors="replace")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Missing moderncv class", result.stdout)

    @unittest.skipUnless(shutil.which("xelatex"), "XeLaTeX unavailable")
    def test_all_variants_compile_and_missing_font_fails(self):
        with tempfile.TemporaryDirectory(prefix="plk phase2 latex ") as tmp:
            root = Path(tmp)
            for template, style in VARIANTS:
                with self.subTest(template=template, style=style):
                    dest = root / f"{template}-{style or 'cv'}"
                    self.assertEqual(generate(template, dest, style).returncode, 0)
                    result = compile_project(dest)
                    self.assertEqual(result.returncode, 0, result.stdout[-2000:])
                    self.assertTrue((dest / "main.pdf").is_file())
                    font_file = dest / "config/fonts.tex"
                    source = font_file.read_text(encoding="utf-8")
                    if template == "letter-fa":
                        source = source.replace("Vazirmatn", "PLK Definitely Missing Font")
                    elif template == "letter-en":
                        selected = "TeX Gyre Termes" if style == "classic" else "TeX Gyre Heros"
                        source = source.replace(selected, "PLK Definitely Missing Font")
                    else:
                        source = source.replace("TeX Gyre Heros", "PLK Definitely Missing Font")
                    font_file.write_text(source, encoding="utf-8")
                    failed = compile_project(dest)
                    self.assertNotEqual(failed.returncode, 0)
                    self.assertIn("Missing", failed.stdout)

    @unittest.skipUnless(shutil.which("xelatex") and shutil.which("pdftotext"),
                         "XeLaTeX/Poppler unavailable")
    def test_optional_letter_fields_and_logo_sizes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for style in ("classic", "modern"):
                with self.subTest(language="fa", style=style):
                    dest = root / f"fa-{style}"
                    self.assertEqual(generate("letter-fa", dest, style).returncode, 0)
                    metadata = dest / "config/metadata.tex"
                    set_fields(metadata, {
                        "LetterOpeningPhraseFa": "", "SenderOrganizationFa": "",
                        "SenderLogoFa": "", "LetterNumberFa": "",
                        "LetterAttachmentFa": "", "SenderAddressFa": "",
                        "SenderEmailFa": "", "SenderPhoneFa": "",
                        "SignatureTitleFa": ""})
                    empty = compile_project(dest)
                    self.assertEqual(empty.returncode, 0, empty.stdout[-1500:])
                    self.assertNotIn("|", pdf_text(dest))
                    self.assertNotIn("example.invalid", pdf_text(dest))
                    set_fields(metadata, {
                        "LetterOpeningPhraseFa": "بسمه تعالی",
                        "SenderOrganizationFa": "گروه نمونه",
                        "SenderLogoFa": "assets/logo.png",
                        "LetterNumberFa": "۱۲۳", "LetterAttachmentFa": "رزومه",
                        "SenderEmailFa": "sender@example.invalid",
                        "SenderPhoneFa": "+00 111 222",
                        "SignatureTitleFa": "دانشجوی مهندسی کامپیوتر"})
                    font_file = dest / "config/fonts.tex"
                    font_file.write_text(font_file.read_text(encoding="utf-8").replace(
                        "TeX Gyre Termes", "TeX Gyre Heros"), encoding="utf-8")
                    for shape, dimensions in (("square", (120, 120)),
                                              ("wide", (1200, 150))):
                        with self.subTest(style=style, logo=shape):
                            (dest / "assets/logo.png").write_bytes(neutral_png(*dimensions))
                            result = compile_project(dest)
                            self.assertEqual(result.returncode, 0, result.stdout[-1500:])
                            self.assertNotIn("Overfull", result.stdout)
                            self.assertIn("sender@example.invalid", pdf_text(dest))
                    (dest / "assets/logo.png").unlink()
                    failed = compile_project(dest)
                    self.assertNotEqual(failed.returncode, 0)
                    self.assertIn("Sender logo not found", failed.stdout)
            for style in ("classic", "modern"):
                with self.subTest(language="en", style=style):
                    dest = root / f"en-{style}"
                    self.assertEqual(generate("letter-en", dest, style).returncode, 0)
                    metadata = dest / "config/metadata.tex"
                    set_fields(metadata, {"SenderOrganizationEn": "", "SenderAddressEn": "",
                                          "SenderEmailEn": "", "SenderPhoneEn": "",
                                          "SignatureTitleEn": ""})
                    empty = compile_project(dest)
                    self.assertEqual(empty.returncode, 0, empty.stdout[-1500:])
                    extracted = pdf_text(dest)
                    self.assertNotIn("example.invalid", extracted)
                    self.assertNotIn("+00", extracted)
                    set_fields(metadata, {"SenderOrganizationEn": "Example Studio",
                                          "SenderEmailEn": "sender@example.invalid",
                                          "SenderPhoneEn": "+00 111 222"})
                    populated = compile_project(dest)
                    self.assertEqual(populated.returncode, 0, populated.stdout[-1500:])
                    self.assertIn("sender@example.invalid", pdf_text(dest))

    @unittest.skipUnless(shutil.which("xelatex") and shutil.which("pdftotext")
                         and shutil.which("pdfinfo"), "XeLaTeX/Poppler unavailable")
    def test_persian_letterhead_page_balance(self):
        with tempfile.TemporaryDirectory(prefix="plk fa letterhead ") as tmp:
            root = Path(tmp)
            for style in ("classic", "modern"):
                for scenario, dimensions in (("square-only", (120, 120)),
                                             ("wide-only", (1200, 150)),
                                             ("full", (1200, 150))):
                    with self.subTest(style=style, scenario=scenario):
                        project = root / f"{style}-{scenario}"
                        self.assertEqual(generate("letter-fa", project, style).returncode, 0)
                        (project / "assets/logo.png").write_bytes(neutral_png(*dimensions))
                        fields = {"SenderLogoFa": "assets/logo.png"}
                        if scenario == "full":
                            fields.update({"SenderOrganizationFa": "گروه نمونه",
                                           "LetterOpeningPhraseFa": "بسمه تعالی",
                                           "LetterNumberFa": "۱۲۳",
                                           "LetterAttachmentFa": "رزومه"})
                        set_fields(project / "config/metadata.tex", fields)
                        result = compile_project(project)
                        self.assertEqual(result.returncode, 0, result.stdout[-1500:])
                        pages = [page for page in pdf_text(project).split("\f")
                                 if page.strip()]
                        self.assertEqual(len(pages), page_count(project))
                        last = unicodedata.normalize("NFKC", pages[-1])
                        self.assertIn("فرزان", last)
                        self.assertIn("احترام", last)
                        if len(pages) > 1:
                            lengths = [len(re.sub(r"\s", "", page)) for page in pages]
                            self.assertGreaterEqual(lengths[-1] / sum(lengths), 0.25,
                                "Normal sample left only its sign-off on a new page")

    @unittest.skipUnless(shutil.which("xelatex") and shutil.which("pdftotext"),
                         "XeLaTeX/Poppler unavailable")
    def test_optional_cv_contact_and_sections(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for style in ("article", "moderncv"):
                with self.subTest(style=style):
                    dest = root / style
                    self.assertEqual(generate("resume-en", dest, style).returncode, 0)
                    metadata = dest / "config/metadata.tex"
                    fields = {"CandidatePhone": "", "CandidateEmail": "",
                              "CandidateHomepage": ""}
                    if style == "article":
                        fields["CandidateLocation"] = ""
                    else:
                        fields.update({"CandidateCity": "", "CandidateCountry": ""})
                    set_fields(metadata, fields)
                    main = dest / "main.tex"
                    main.write_text(main.read_text(encoding="utf-8").replace(
                        r"\input{sections/publications}",
                        r"% \input{sections/publications}"), encoding="utf-8")
                    result = compile_project(dest)
                    self.assertEqual(result.returncode, 0, result.stdout[-1500:])
                    extracted = pdf_text(dest)
                    self.assertNotIn("example.invalid", extracted)
                    self.assertNotIn("+00", extracted)
                    self.assertNotIn("PUBLICATIONS", extracted.upper())
                    if style == "article":
                        self.assertNotIn("|", extracted)
                    experience = dest / "sections/experience.tex"
                    if style == "article":
                        extra = (r"\CVExperience{Extra Role}{Example Lab}{2023}"
                                 r"{Verified repeatable workflows.}")
                    else:
                        extra = (r"\cventry{2023}{Extra Role}{Example Lab}{}{}"
                                 r"{Verified repeatable workflows.}")
                    experience.write_text(experience.read_text(encoding="utf-8") +
                                          "\n" + extra + "\n", encoding="utf-8")
                    repeated = compile_project(dest)
                    self.assertEqual(repeated.returncode, 0, repeated.stdout[-1500:])
                    self.assertIn("Extra Role", pdf_text(dest))

    @unittest.skipUnless(shutil.which("xelatex") and shutil.which("pdftotext")
                         and shutil.which("pdfinfo"), "XeLaTeX/Poppler unavailable")
    def test_letter_and_cv_pagination(self):
        with tempfile.TemporaryDirectory(prefix="plk phase2 pages ") as tmp:
            root = Path(tmp)
            for template, style in VARIANTS:
                with self.subTest(template=template, style=style):
                    dest = root / f"{template}-{style or 'cv'}"
                    self.assertEqual(generate(template, dest, style).returncode, 0)
                    if template.startswith("letter"):
                        body = dest / "content/body.tex"
                        original = body.read_text(encoding="utf-8")
                        body.write_text((original + "\n\n") * 3, encoding="utf-8")
                    elif style == "article":
                        experience = dest / "sections/experience.tex"
                        experience.write_text(
                            experience.read_text(encoding="utf-8") +
                            ("\n\\CVExperience{Systems Assistant}{Example Lab}{2024--2025}"
                             "{Built and tested a repeatable benchmark workflow for small servers.}\n") * 3,
                            encoding="utf-8")
                        projects = dest / "sections/projects.tex"
                        projects.write_text(
                            projects.read_text(encoding="utf-8") +
                            "\n\\CVProject{Benchmark Toolkit}{Designed reproducible scripts and reports.}\n" * 3,
                            encoding="utf-8")
                    else:
                        experience = dest / "sections/experience.tex"
                        experience.write_text(
                            experience.read_text(encoding="utf-8") +
                            "\n\\cventry{2023}{Systems Assistant}{Example Lab}{}{}"
                            "{Built and tested a repeatable benchmark workflow.}\n" * 6,
                            encoding="utf-8")
                        projects = dest / "sections/projects.tex"
                        projects.write_text(
                            projects.read_text(encoding="utf-8") +
                            "\n\\cvitem{}{\\textbf{Benchmark Toolkit}. Designed reproducible scripts and reports.}\n" * 6,
                            encoding="utf-8")
                    result = compile_project(dest)
                    self.assertEqual(result.returncode, 0, result.stdout[-2000:])
                    self.assertGreaterEqual(page_count(dest), 2)
                    pages = [page for page in pdf_text(dest).split("\f") if page.strip()]
                    self.assertGreaterEqual(len(pages), 2)
                    last = pages[-1]
                    if template == "letter-fa":
                        normalized = unicodedata.normalize("NFKC", last)
                        self.assertIn("فرزان", normalized)
                        self.assertIn("احترام", normalized)
                    elif template == "letter-en":
                        self.assertIn("Mina Farzan", last)
                        self.assertIn("Sincerely", last)
                    else:
                        publication_pages = [page for page in pages
                                             if "publications" in page.lower()]
                        self.assertTrue(publication_pages)
                        self.assertTrue(all("Symposium" in page for page in publication_pages))


if __name__ == "__main__":
    unittest.main()
