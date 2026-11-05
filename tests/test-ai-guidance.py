#!/usr/bin/env python3
"""Check offline AI guidance packaging against the current source snapshot."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
GENERATOR = ROOT / "scripts" / "new-project.py"
VARIANTS = (
    ("assignment", None, "assignment", "questions/question01.tex"),
    ("lab-report", None, "lab-report", "sections/01-objective.tex"),
    ("os-single-question", None, "os-single-question", "questions/question01.tex"),
    ("letter-fa", "classic", "letter-fa", "content/body.tex"),
    ("letter-fa", "modern", "letter-fa", "content/final-paragraph.tex"),
    ("letter-en", "classic", "letter-en", "content/body.tex"),
    ("letter-en", "modern", "letter-en", "content/final-paragraph.tex"),
    ("resume-en", None, "resume-article", "sections/education.tex"),
    ("resume-en", "article", "resume-article", "sections/experience.tex"),
    ("resume-en", "moderncv", "resume-moderncv", "sections/projects.tex"),
)


def generate(template: str, dest: Path, style: str | None = None):
    command = [sys.executable, "-B", str(GENERATOR), "--template", template,
               "--destination", str(dest)]
    if style:
        command += ["--style", style]
    return subprocess.run(command, capture_output=True, text=True, errors="replace")


class AIGuidanceTests(unittest.TestCase):
    def test_every_variant_has_local_scoped_onboarding(self):
        with tempfile.TemporaryDirectory(prefix="plk-ai-") as tmp:
            for index, (template, style, scope, content_file) in enumerate(VARIANTS):
                with self.subTest(template=template, style=style):
                    project = Path(tmp) / f"variant-{index}"
                    result = generate(template, project, style)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    start = (project / "AI_START_HERE.md").read_text(encoding="utf-8")
                    macros = (project / "AI_MACROS.md").read_text(encoding="utf-8")
                    self.assertTrue(start.startswith("# AI_START_HERE\n"))
                    self.assertTrue(macros.startswith("# AI_MACROS\n"))
                    self.assertIn(f"Project type: `{template}`", start)
                    self.assertIn(f"Selected style: `{style or ('article' if template == 'resume-en' else 'built-in')}`", start)
                    self.assertIn("Main source: `main.tex`", start)
                    self.assertIn(content_file, start)
                    for name in ("main.tex", "AGENTS.md", "config/metadata.tex",
                                 "config/fonts.tex", content_file):
                        self.assertTrue((project / name).is_file(), name)
                    self.assertIn("AI_MACROS.md", start)
                    self.assertNotIn("<!-- projects:", start + macros)
                    self.assertNotIn("](docs/", start + macros)
                    self.assertFalse((project / ".git").exists())
                    self.assertFalse((project / ".gitmodules").exists())
                    self.assertNotIn("## OS-specific content", macros if scope != "os-single-question" else "")
                    if scope == "os-single-question":
                        self.assertIn("## OS-specific content", macros)
                        self.assertNotIn("## Questions, answers, and assignment metadata", macros)
                    if scope == "resume-moderncv":
                        self.assertIn("\\cventry", macros)
                        self.assertNotIn("## Article CV sections", macros)
                    if scope == "resume-article":
                        self.assertIn("\\CVExperience", macros)
                        self.assertNotIn("## ModernCV sections", macros)

    def test_en_is_terminology_not_generic_latin(self):
        source = (ROOT / "tex/persian-kit.sty").read_text(encoding="utf-8")
        reference = (ROOT / "docs/MACRO_REFERENCE.md").read_text(encoding="utf-8")
        self.assertIn(r"\newcommand{\EN}[1]{\lr{(#1)}}", source)
        self.assertNotRegex(source, r"\\(?:newcommand|providecommand)\{\\En\}")
        self.assertIn("there is **no `\\En` command**", reference)
        self.assertIn("`\\lr{SVD}` is ordinary inline Latin", reference)
        self.assertIn("`\\EN{(SVD)}` doubles the parentheses", reference)
        self.assertIn("\\Term{تجزیهٔ مقادیر منفرد}", reference)
        self.assertIn("`\\textenglish{text}` is **not defined by this kit", reference)

    def test_os_renamed_question_is_named_in_guide(self):
        with tempfile.TemporaryDirectory(prefix="plk-ai-os-") as tmp:
            dest = Path(tmp) / "question-two"
            command = [sys.executable, "-B", str(GENERATOR), "--template",
                       "os-single-question", "--destination", str(dest),
                       "--question-number", "۲"]
            result = subprocess.run(command, capture_output=True, text=True,
                                    errors="replace")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((dest / "questions/question02.tex").is_file())
            self.assertIn("questions/question02.tex",
                          (dest / "AI_START_HERE.md").read_text(encoding="utf-8"))

    def test_documented_public_names_exist_in_source(self):
        reference = (ROOT / "docs/MACRO_REFERENCE.md").read_text(encoding="utf-8")
        sources = "\n".join((ROOT / path).read_text(encoding="utf-8") for path in (
            "tex/persian-kit.sty", "tex/persian-lab.sty", "tex/persian-os.sty",
            "templates/resume-en/main.tex", "templates/resume-en-moderncv/main.tex"))
        public_names = (
            "EN", "Term", "SmallNote", "HWActivateAssignmentLayout",
            "MakeHomeworkTitle", "HWQuestion", "HWPart", "HWSubpart",
            "HWTableHead", "HWTableStart", "HWTableEnd",
            "HWFigure", "MakeLabTitle", "LabFigure",
            "OSLatin", "OSParen", "OSBracketed", "OSDash",
            "OSDateRange", "OSTechnicalTerm", "OSMakeQuestionTitle",
            "OSAnswerHeading", "OSPart", "OSBodyText", "OSPlaceholder",
            "OSFigure", "CVSection", "CVDatedEntry", "CVExperience",
            "CVProject", "CVLine",
        )
        for name in public_names:
            with self.subTest(name=name):
                self.assertTrue("\\" + name in sources, f"Missing source: {name}")
                self.assertTrue("\\" + name in reference, f"Missing reference: {name}")
        for name in ("HWTable", "HWTip", "HWWarning", "LabTable"):
            self.assertTrue(name in sources and name in reference, name)
        self.assertRegex(reference, r"(?s)\\EN\{English equivalent\}.*?Not for every English word")

    def test_portable_prompt_and_existing_destination(self):
        prompt = (ROOT / "docs/CHAT_STARTER_PROMPT_FA.md").read_text(encoding="utf-8")
        for phrase in ("AI_START_HERE.md", "AI_MACROS.md", "main.tex",
                       "نامه", "رزومه", "XeLaTeX", "\\EN", "\\lr"):
            self.assertIn(phrase, prompt)
        with tempfile.TemporaryDirectory(prefix="plk-ai-existing-") as tmp:
            dest = Path(tmp) / "existing"
            dest.mkdir()
            sentinel = dest / "owner-file.txt"
            sentinel.write_text("preserve", encoding="utf-8")
            result = generate("assignment", dest)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "preserve")
            self.assertEqual(sorted(p.name for p in dest.iterdir()), ["owner-file.txt"])


if __name__ == "__main__":
    unittest.main()
