#!/usr/bin/env python3
"""Exercise each project generator without contacting GitHub or writing in the kit."""

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "new-project.py"
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / "scripts"))
import project_generator
STYLES = {
    "assignment": ("persian-kit.sty",),
    "lab-report": ("persian-kit.sty", "persian-lab.sty"),
    "os-single-question": ("persian-os.sty",),
}


def generate(template: str, destination: Path, *options: str,
             env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(SCRIPT), "--template", template,
                           "--destination", str(destination), *options],
                          capture_output=True, text=True, env=env)


class ProjectGeneratorTests(unittest.TestCase):
    def test_relative_destination_outside_toolkit(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "relative project"
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--template", "assignment",
                 "--destination", dest.name],
                cwd=tmp, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((dest / "main.tex").is_file())
            self.assertFalse((dest / ".git").exists())

    def test_symlink_destination_into_toolkit_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            kit = root / "kit"
            shutil.copytree(ROOT / "templates/assignment", kit / "templates/assignment")
            (kit / "tex").mkdir()
            shutil.copy2(ROOT / "tex/persian-kit.sty", kit / "tex/persian-kit.sty")
            alias = root / "kit-alias"
            try:
                os.symlink(kit, alias, target_is_directory=True)
            except (OSError, NotImplementedError) as exc:
                self.skipTest(f"Directory symlink creation unavailable: {exc}")
            old_cwd = Path.cwd()
            try:
                os.chdir(root)
                for destination in (alias / "absolute-project", Path("kit-alias/relative-project")):
                    with self.subTest(destination=str(destination)):
                        args = argparse.Namespace(
                            template="assignment", destination=str(destination),
                            offline=False, git=False, repository_url=None,
                            kit_path=None, assignment_number=None, question_number="۱")
                        with patch.object(project_generator, "KIT", kit):
                            with self.assertRaisesRegex(ValueError, "outside the toolkit repository"):
                                project_generator.build(args)
                self.assertFalse((kit / "absolute-project").exists())
                self.assertFalse((kit / "relative-project").exists())
            finally:
                os.chdir(old_cwd)

    def test_standalone_default_and_independent_compilation(self):
        with tempfile.TemporaryDirectory(prefix="plk test ") as tmp:
            root = Path(tmp)
            for template, styles in STYLES.items():
                with self.subTest(template=template):
                    dest = root / f"{template} نمونه"
                    result = generate(template, dest)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertTrue((dest / "main.tex").is_file())
                    self.assertTrue((dest / "config/fonts.tex").is_file())
                    self.assertFalse((dest / ".git").exists())
                    self.assertFalse((dest / ".gitmodules").exists())
                    for style in styles:
                        self.assertTrue((dest / "vendor/persian-latex-kit/tex" / style).is_file())
                    if shutil.which("xelatex"):
                        latex = subprocess.run(
                            ["xelatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
                            cwd=dest, capture_output=True, text=True, errors="replace")
                        self.assertEqual(latex.returncode, 0, latex.stdout[-1500:])
                        self.assertTrue((dest / "main.pdf").is_file())

    def test_existing_destination_and_failed_git_leave_no_partial_project(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            existing = root / "existing"
            existing.mkdir()
            (existing / "keep.txt").write_text("keep", encoding="utf-8")
            result = generate("assignment", existing)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual((existing / "keep.txt").read_text(encoding="utf-8"), "keep")
            failed = root / "failed"
            result = generate("lab-report", failed, "--repository-url", str(root / "absent"))
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(failed.exists())
            self.assertFalse(list(root.glob("plk-new-*")))

    def test_missing_style_fails_before_project_creation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "empty-kit"
            source.mkdir()
            dest = root / "not-created"
            result = generate("assignment", dest, "--kit-path", str(source))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Missing required style", result.stderr)
            self.assertFalse(dest.exists())

    def test_explicit_git_mode_with_local_fixture(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            remote = root / "library"
            (remote / "tex").mkdir(parents=True)
            for style in {style for styles in STYLES.values() for style in styles}:
                shutil.copy2(ROOT / "tex" / style, remote / "tex" / style)
            subprocess.run(["git", "init", "-b", "main"], cwd=remote,
                           check=True, capture_output=True)
            subprocess.run(["git", "add", "."], cwd=remote,
                           check=True, capture_output=True)
            subprocess.run(["git", "-c", "user.name=Test", "-c",
                            "user.email=test@example.org", "commit", "-m", "fixture"],
                           cwd=remote, check=True, capture_output=True)
            env = dict(os.environ, GIT_ALLOW_PROTOCOL="file")
            for template in STYLES:
                with self.subTest(template=template):
                    dest = root / f"{template}-git"
                    result = generate(template, dest, "--repository-url", str(remote), env=env)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertTrue((dest / ".git").exists())
                    self.assertTrue((dest / ".gitmodules").is_file())
                    for style in STYLES[template]:
                        self.assertTrue((dest / "vendor/persian-latex-kit/tex" / style).is_file())
                    output = subprocess.run(["git", "check-ignore", "-q", "main.pdf"],
                                            cwd=dest, check=False)
                    self.assertEqual(output.returncode, 0)
                    source_pdf = subprocess.run(
                        ["git", "check-ignore", "-q", "assets/diagram.pdf"],
                        cwd=dest, check=False)
                    self.assertEqual(source_pdf.returncode, 1)

    def test_git_mode_rejects_outdated_style(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            remote = root / "old-library"
            (remote / "tex").mkdir(parents=True)
            (remote / "tex/persian-kit.sty").write_text(
                "\\NeedsTeXFormat{LaTeX2e}\n"
                "\\ProvidesPackage{persian-kit}[2025/01/01 legacy]\n"
                "\\RequirePackage{xepersian}\n"
                "\\settextfont{Vazirmatn}\n",
                encoding="utf-8")
            subprocess.run(["git", "init", "-b", "main"], cwd=remote,
                           check=True, capture_output=True)
            subprocess.run(["git", "add", "."], cwd=remote,
                           check=True, capture_output=True)
            subprocess.run(["git", "-c", "user.name=Test", "-c",
                            "user.email=test@example.org", "commit", "-m", "old fixture"],
                           cwd=remote, check=True, capture_output=True)
            dest = root / "incompatible-project"
            result = generate("assignment", dest, "--repository-url", str(remote),
                              env=dict(os.environ, GIT_ALLOW_PROTOCOL="file"))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Incompatible Git submodule style: persian-kit.sty", result.stderr)
            self.assertIn("Publish matching styles", result.stderr)
            self.assertFalse(dest.exists())
            self.assertFalse(list(root.glob("plk-new-*")))

    def test_project_font_overrides_and_missing_font_error(self):
        if not shutil.which("xelatex"):
            self.skipTest("XeLaTeX is not installed")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            alternate_available = False
            if shutil.which("fc-match"):
                match = subprocess.run(["fc-match", "-f", "%{family}", "Amiri"],
                                       capture_output=True, text=True, errors="replace")
                alternate_available = match.returncode == 0 and "Amiri" in match.stdout
            if alternate_available:
                for template in STYLES:
                    with self.subTest(template=template):
                        dest = root / template
                        self.assertEqual(generate(template, dest).returncode, 0)
                        (dest / "config/fonts.tex").write_text(
                            r"\newcommand{\PLKPersianFont}{Amiri}" "\n"
                            r"\newcommand{\PLKLatinFont}{Latin Modern Roman}" "\n",
                            encoding="utf-8")
                        result = subprocess.run(
                            ["xelatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
                            cwd=dest, capture_output=True, text=True, errors="replace")
                        self.assertEqual(result.returncode, 0, result.stdout[-1500:])
            missing = root / "missing-font"
            self.assertEqual(generate("assignment", missing).returncode, 0)
            (missing / "config/fonts.tex").write_text(
                r"\newcommand{\PLKPersianFont}{Definitely Missing PLK Font}" "\n",
                encoding="utf-8")
            result = subprocess.run(
                ["xelatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
                cwd=missing, capture_output=True, text=True, errors="replace")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Required Persian font", result.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
