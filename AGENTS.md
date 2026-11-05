# AI assistant rules for Persian LaTeX Kit

This repository is a reusable, course-independent LaTeX toolkit. Never put real
student details, homework answers, course attachments, or font binaries in it.
Keep individual documents in generated projects outside this library.

## Architecture and ownership

- `tex/persian-kit.sty`: shared Persian components for assignments.
- `tex/persian-lab.sty`: lab title, figure, and table extension; load after the kit.
- `tex/persian-os.sty`: isolated historical one-question layout. Do not merge it
  into the multi-question assignment design or change its header and footer
  merely to share code.
- `templates/`: starter projects and their local `AGENTS.md` instructions.
- `templates/letter-fa`, `templates/letter-en`: independent correspondence
  projects. Letter variants share content/metadata and choose their document
  class at generation time with `--style`.
- `templates/resume-en`: the default Article CV; keep its current structure.
- `templates/resume-en-moderncv`: the internal ModernCV starter selected by
  `--template resume-en --style moderncv`. The public default remains Article.
- `scripts/`: Python project generator and thin Windows PowerShell entry points.
- `examples/snippets/`, `docs/`, `tests/`: examples, guidance, and checks.
- `docs/MACRO_REFERENCE.md` is the source-checked public API reference;
  `docs/AI_HANDBOOK.md` and `docs/CHAT_STARTER_PROMPT_FA.md` guide chat-only work.
  New projects carry relevant snapshots as `AI_START_HERE.md` and `AI_MACROS.md`.

Generated projects are **standalone snapshots by default**. They copy only their
required styles, if any, into `vendor/persian-latex-kit/tex/`, create no Git repository,
and do not update automatically. `--git` / `-Git` explicitly selects the
submodule mode. A repository URL also selects that mode for old commands. Never
edit a consumer project's vendored copy when making a reusable library change.

## LaTeX and font conventions

Read `README.md`, relevant template `main.tex`/metadata, style source, and
`docs/MACRO_REFERENCE.md` before an edit. Check source before claiming a macro
exists. Use XeLaTeX and XePersian for these Persian templates; keep Persian RTL.
Use `\lr{}` for ordinary inline Latin, `\EN{}` for a parenthesized English
equivalent, and `\Term{}{}` for bold Persian with its English equivalent.
`\EN{}` adds its own parentheses.
There is no `\En` definition: command names are case-sensitive. See the
reference for exact scope, external package commands, and internal helpers.

**Current default in all three templates is Vazirmatn** for Persian text and
text/math digits. The OS layout used Noto Sans Arabic historically, but its
current source and default PDF use Vazirmatn. Noto Sans Arabic is an optional
installed-font override. Do not silently substitute a user-selected font or
commit font binaries. Font selections belong in the generated project's
`config/fonts.tex`; identity and document metadata remain in
`config/metadata.tex`. Assignment/lab/OS read font settings before their `.sty`
files; each letter and CV reads settings before selecting fonts. Preserve the
existing OS local Vazirmatn path option.
Do not place font selections in `config/metadata.tex`.
Publisher-controlled classes must not inherit these font overrides.

For Phase 2 letters and CV, read `docs/DOCUMENT_TEMPLATES.md` and the scoped
template `AGENTS.md`. Preserve the approved classes and fonts: Persian article
letters use Vazirmatn; English classic uses TeX Gyre Termes; English modern and
both CV styles use TeX Gyre Heros. Use `--style article` or `moderncv` for the
resume, with Article as the default. Keep letter final paragraphs with their closings and CV
section headings with their first content. Put optional letterhead assets only
in the generated document; never invent organization branding.

For OS text, test `، ؛ ؟ « »`, `\OSParen`, `\OSBracketed`, and `\OSDateRange`;
isolate Latin terms with `\OSLatin`. Avoid raw ASCII bracket glyphs in Persian
text. Preserve one question per OS project and PDF.

## Changes and verification

- Put reusable components in `tex/`, general examples in `examples/snippets/`,
  template-specific files in `templates/`, documentation in `docs/`, and a
  change entry in `CHANGELOG.md`. Follow `docs/EXTENDING_THE_KIT.md` before
  proposing a new public component. Reuse working components before adding one.
- Keep new templates separate where their language or document class requires
  different layout. Avoid a shared base class without demonstrated need.
- Test generators with `python tests/test-project-generator.py` and
  `python tests/test-new-os-homework.py` and `python tests/test-document-templates.py`.
  Compile representative documents with
  XeLaTeX from their project roots and inspect PDFs for font, RTL/LTR,
  punctuation, overflow, headers, figures, and tables. State when a required
  compiler, font, or visual check was unavailable.
- Preserve existing user changes and Git history. Do not force-push. Do not
  commit, push, merge, or release unless the owner authorizes it for the task.

Implement clearly scoped approved work without repeated permission requests.
Ask the owner before substantial architecture changes, public API removal,
unexpected compatibility breaks, major dependencies, or visual identity changes.
Report meaningful minor decisions and distinguish verified results from
assumptions. Do not widen the repository into assignment submission packaging.
