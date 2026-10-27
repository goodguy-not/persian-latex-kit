#!/usr/bin/env python3
"""Create a Persian single-question homework project using the shared LaTeX kit.

Default: pin the shared library's origin remote as a Git submodule.
Offline mode: explicit --offline snapshot of the OS style (no automatic updates).
"""
from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
KIT = HERE.parent
ASSIGNMENT_LABELS = {
    "1": "اول", "2": "دوم", "3": "سوم", "4": "چهارم",
    "5": "پنجم", "6": "ششم", "7": "هفتم", "8": "هشتم",
}
PERSIAN_NUMBERS = str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789")


def run(*cmd: str, cwd: Path) -> None:
    proc = subprocess.run(cmd, cwd=cwd, check=False)
    if proc.returncode:
        raise RuntimeError(f"Command failed ({proc.returncode}): {' '.join(cmd)}")


def origin_url(kit: Path) -> str:
    proc = subprocess.run(["git", "remote", "get-url", "origin"], cwd=kit,
                          check=False, capture_output=True, text=True)
    url = proc.stdout.strip() if proc.returncode == 0 else ""
    if not url:
        raise ValueError("No origin remote found. Supply --repository-url "
                         "or use --offline explicitly.")
    return url


def replace_once(path: Path, before: str, after: str) -> None:
    txt = path.read_text(encoding="utf-8")
    if txt.count(before) != 1:
        raise RuntimeError(f"Template changed: expected one instance of {before!r}")
    path.write_text(txt.replace(before, after), encoding="utf-8")


def build(args: argparse.Namespace) -> Path:
    dest = Path(args.destination).expanduser().resolve()
    if dest.exists():
        raise ValueError(f"Destination already exists: {dest}")
    if args.offline and args.repository_url:
        raise ValueError("Choose --offline OR --repository-url, not both")
    if args.kit_path and not args.offline:
        raise ValueError("--kit-path requires --offline")
    template = KIT / "templates" / "os-single-question"
    source_kit = Path(args.kit_path).expanduser().resolve() if args.kit_path else KIT
    if args.offline and not (source_kit / "tex" / "persian-os.sty").is_file():
        raise FileNotFoundError(f"Missing OS style in {source_kit}/tex/")
    repository_url = None if args.offline else (args.repository_url or origin_url(KIT))
    dest.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="os-new-", dir=dest.parent) as work:
        project = Path(work) / "project"
        shutil.copytree(template, project)
        meta = project / "config" / "metadata.tex"
        num = args.assignment_number.translate(PERSIAN_NUMBERS)
        label = ASSIGNMENT_LABELS.get(num, args.assignment_number)
        replace_once(meta, r"\renewcommand{\OSAssignment}{تمرین سری دوم}",
                     rf"\renewcommand{{\OSAssignment}}{{تمرین سری {label}}}")
        replace_once(meta, r"\renewcommand{\OSQuestionNumber}{۱}",
                     rf"\renewcommand{{\OSQuestionNumber}}{{{args.question_number}}}")
        normalized = args.question_number.translate(PERSIAN_NUMBERS)
        if normalized.isdigit() and 1 <= int(normalized) <= 999:
            source_name = f"question{int(normalized):02d}"
            if source_name != "question01":
                (project / "questions/question01.tex").rename(
                    project / "questions" / f"{source_name}.tex")
                replace_once(project / "main.tex", r"\input{questions/question01}",
                             rf"\input{{questions/{source_name}}}")
        else:
            source_name = "question01"
        (project / "build").mkdir()
        run("git", "init", "-b", "main", cwd=project)
        if repository_url:
            run("git", "submodule", "add", repository_url,
                "vendor/persian-latex-kit", cwd=project)
            if not (project / "vendor/persian-latex-kit/tex/persian-os.sty").is_file():
                raise RuntimeError("Remote library lacks tex/persian-os.sty. "
                                   "Commit and push the library patch first.")
            mode = "Git submodule (pinned shared library)"
        else:
            vendor = project / "vendor" / "persian-latex-kit" / "tex"
            vendor.mkdir(parents=True)
            shutil.copy2(source_kit / "tex" / "persian-os.sty", vendor / "persian-os.sty")
            mode = "explicit offline snapshot (not auto-updated)"
        project.rename(dest)
    print(f"Created {dest} [{mode}].")
    print(f"Edit config/metadata.tex and questions/{source_name}.tex.")
    print("Compile main.tex twice using XeLaTeX from the project root.")
    return dest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", required=True, help="New project path")
    parser.add_argument("--question-number", default="۱", help="Shown in title (e.g. ۲)")
    parser.add_argument("--assignment-number", default="۲", help="Series number (e.g. ۲)")
    parser.add_argument("--repository-url", help="Override shared kit's origin Git remote")
    parser.add_argument("--offline", action="store_true", help="Opt in to a local style snapshot")
    parser.add_argument("--kit-path", help="Offline style source checkout (requires --offline)")
    args = parser.parse_args()
    try:
        build(args)
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
