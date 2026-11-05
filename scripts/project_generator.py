"""Create isolated document projects from the repository's starter templates."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


KIT = Path(__file__).resolve().parent.parent
STYLES = {
    "assignment": ("persian-kit.sty",),
    "lab-report": ("persian-kit.sty", "persian-lab.sty"),
    "os-single-question": ("persian-os.sty",),
    "letter-fa": (),
    "letter-en": (),
    "resume-en": (),
}
LETTER_VARIANTS = {"letter-fa", "letter-en"}
ASSIGNMENT_LABELS = {
    "1": "اول", "2": "دوم", "3": "سوم", "4": "چهارم",
    "5": "پنجم", "6": "ششم", "7": "هفتم", "8": "هشتم",
}
PERSIAN_NUMBERS = str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789")


def run(*command: str, cwd: Path) -> None:
    result = subprocess.run(command, cwd=cwd, check=False)
    if result.returncode:
        raise RuntimeError(f"Command failed ({result.returncode}): {' '.join(command)}")


def origin_url(kit: Path) -> str:
    result = subprocess.run(["git", "remote", "get-url", "origin"], cwd=kit,
                            capture_output=True, text=True, check=False)
    if result.returncode or not result.stdout.strip():
        raise ValueError("No origin remote found. Supply --repository-url for Git mode.")
    return result.stdout.strip()


def replace_once(path: Path, before: str, after: str) -> None:
    text = path.read_text(encoding="utf-8")
    if text.count(before) != 1:
        raise RuntimeError(f"Template changed: expected one instance of {before!r} in {path}")
    path.write_text(text.replace(before, after), encoding="utf-8")


def configure_os(project: Path, question_number: str, assignment_number: str | None) -> str:
    metadata = project / "config" / "metadata.tex"
    if assignment_number is not None:
        number = assignment_number.translate(PERSIAN_NUMBERS)
        label = ASSIGNMENT_LABELS.get(number, assignment_number)
        replace_once(metadata, r"\renewcommand{\OSAssignment}{عنوان تمرین}",
                     rf"\renewcommand{{\OSAssignment}}{{تمرین سری {label}}}")
    replace_once(metadata, r"\renewcommand{\OSQuestionNumber}{۱}",
                 rf"\renewcommand{{\OSQuestionNumber}}{{{question_number}}}")
    normalized = question_number.translate(PERSIAN_NUMBERS)
    if normalized.isdigit() and 1 <= int(normalized) <= 999:
        source_name = f"question{int(normalized):02d}"
        if source_name != "question01":
            (project / "questions" / "question01.tex").rename(
                project / "questions" / f"{source_name}.tex")
            replace_once(project / "main.tex", r"\input{questions/question01}",
                         rf"\input{{questions/{source_name}}}")
        return source_name
    return "question01"


def required_files(project: Path, template: str) -> tuple[Path, ...]:
    common = (project / "main.tex", project / "config" / "metadata.tex",
              project / "config" / "fonts.tex")
    content = {
        "assignment": (project / "questions" / "question01.tex",),
        "lab-report": (project / "sections" / "01-objective.tex",
                       project / "sections" / "02-specification.tex",
                       project / "sections" / "03-design.tex",
                       project / "sections" / "04-tests.tex",
                       project / "sections" / "05-evaluation-plan.tex",
                       project / "sections" / "05-results.tex",
                       project / "sections" / "06-conclusion.tex"),
        "os-single-question": tuple((project / "questions").glob("question*.tex")),
        "letter-fa": (project / "letter-parts.tex",
                      project / "content" / "body.tex",
                      project / "content" / "final-paragraph.tex"),
        "letter-en": (project / "letter-parts.tex",
                      project / "content" / "body.tex",
                      project / "content" / "final-paragraph.tex"),
        "resume-en": (project / "sections" / "education.tex",
                      project / "sections" / "experience.tex",
                      project / "sections" / "projects.tex",
                      project / "sections" / "skills.tex",
                      project / "sections" / "languages.tex",
                      project / "sections" / "research.tex",
                      project / "sections" / "honors.tex",
                      project / "sections" / "publications.tex"),
    }
    return common + content[template] + tuple(
        project / "vendor" / "persian-latex-kit" / "tex" / style
        for style in STYLES[template]
    )


def build(args: argparse.Namespace) -> Path:
    template = args.template
    style = getattr(args, "style", None)
    if template in LETTER_VARIANTS and style not in ("classic", "modern"):
        raise ValueError("Letter templates require --style classic or --style modern")
    if template == "resume-en" and style not in (None, "article", "moderncv"):
        raise ValueError("Resume styles are article or moderncv")
    if template not in LETTER_VARIANTS and template != "resume-en" and style is not None:
        raise ValueError("--style applies only to letter-fa, letter-en, and resume-en")
    dest = Path(os.path.abspath(os.path.expanduser(args.destination)))
    if os.path.lexists(dest):
        raise ValueError(f"Destination already exists: {dest}")
    # Follow parent symlinks before deciding whether this path enters the kit.
    effective_dest = dest.resolve(strict=False)
    effective_kit = KIT.resolve()
    try:
        inside_kit = os.path.commonpath((effective_kit, effective_dest)) == str(effective_kit)
    except ValueError:  # Different Windows drives cannot share a parent.
        inside_kit = False
    if inside_kit:
        raise ValueError("Destination must be outside the toolkit repository")
    if args.offline and (args.git or args.repository_url):
        raise ValueError("--offline cannot be combined with Git mode or --repository-url")
    git_mode = bool(args.git or args.repository_url)
    if args.kit_path and git_mode:
        raise ValueError("--kit-path is only available for standalone projects")
    if template != "os-single-question" and args.assignment_number is not None:
        raise ValueError("--assignment-number applies only to the OS template")
    source_kit = Path(args.kit_path).expanduser().resolve() if args.kit_path else KIT
    starter_name = "resume-en-moderncv" if template == "resume-en" and style == "moderncv" else template
    starter = KIT / "templates" / starter_name
    base = starter / "common" if template in LETTER_VARIANTS else starter
    if not base.is_dir():
        raise FileNotFoundError(f"Missing template: {base}")
    if not (base / "config" / "fonts.tex").is_file():
        raise FileNotFoundError(f"Missing font configuration: {base / 'config' / 'fonts.tex'}")
    style_main = starter / "styles" / style / "main.tex" if template in LETTER_VARIANTS else None
    if style_main and not style_main.is_file():
        raise FileNotFoundError(f"Missing letter style: {style_main}")
    if not git_mode:
        for style in STYLES[template]:
            source = source_kit / "tex" / style
            if not source.is_file():
                raise FileNotFoundError(f"Missing required style: {source}")
    repository_url = (args.repository_url or origin_url(KIT)) if git_mode else None
    dest.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="plk-new-", dir=dest.parent) as work:
        project = Path(work) / "project"
        shutil.copytree(base, project)
        if style_main:
            shutil.copy2(style_main, project / "main.tex")
        source_name = None
        if template == "os-single-question":
            source_name = configure_os(project, args.question_number, args.assignment_number)
        vendor = project / "vendor" / "persian-latex-kit"
        if repository_url:
            run("git", "init", "-b", "main", cwd=project)
            run("git", "submodule", "add", repository_url,
                "vendor/persian-latex-kit", cwd=project)
            mode = "Git submodule"
        else:
            if STYLES[template]:
                tex = vendor / "tex"
                tex.mkdir(parents=True)
                for vendor_style in STYLES[template]:
                    shutil.copy2(source_kit / "tex" / vendor_style, tex / vendor_style)
            mode = "standalone snapshot"
        missing = [str(path.relative_to(project)) for path in required_files(project, template)
                   if not path.is_file()]
        if template == "os-single-question" and not (project / "questions" / f"{source_name}.tex").is_file():
            missing.append(f"questions/{source_name}.tex")
        if missing:
            raise RuntimeError("Required project files are missing: " + ", ".join(missing))
        if repository_url:
            # Local templates and cloned styles must come from the same source state.
            # Git may convert LF to CRLF on Windows; that does not change the style.
            for vendor_style in STYLES[template]:
                local_style = KIT / "tex" / vendor_style
                cloned_style = vendor / "tex" / vendor_style
                if not local_style.is_file():
                    raise FileNotFoundError(f"Missing local style for compatibility check: {local_style}")
                local_content = local_style.read_bytes().replace(b"\r\n", b"\n")
                cloned_content = cloned_style.read_bytes().replace(b"\r\n", b"\n")
                if cloned_content != local_content:
                    raise RuntimeError(
                        f"Incompatible Git submodule style: {vendor_style} differs from this toolkit. "
                        "Publish matching styles to the Git repository or generate a standalone project."
                    )
        if os.path.lexists(dest):
            raise ValueError(f"Destination appeared during generation: {dest}")
        project.rename(dest)

    print(f"Created {dest} [{mode}].")
    if source_name:
        print(f"Edit config/metadata.tex and questions/{source_name}.tex.")
    else:
        print("Edit config/metadata.tex and the document content files.")
    print("Choose fonts in config/fonts.tex; compile main.tex with XeLaTeX.")
    return dest


def main(argv: list[str] | None = None) -> int:
    # Windows terminals may advertise a legacy encoding even for Unicode paths.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(errors="backslashreplace")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--template", choices=tuple(STYLES), required=True)
    parser.add_argument("--style", choices=("classic", "modern", "article", "moderncv"),
                        help="Letters require classic or modern; resume-en defaults to article")
    parser.add_argument("--destination", required=True)
    parser.add_argument("--git", action="store_true", help="Use a Git submodule instead of a standalone snapshot")
    parser.add_argument("--repository-url", help="Git submodule URL; also enables Git mode")
    parser.add_argument("--offline", action="store_true", help="Legacy alias for standalone mode")
    parser.add_argument("--kit-path", help="Alternate source for standalone style files")
    parser.add_argument("--question-number", default="۱", help="OS question number")
    parser.add_argument("--assignment-number", help="Optional OS assignment series number")
    args = parser.parse_args(argv)
    try:
        build(args)
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0
