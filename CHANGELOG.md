## Unreleased — AI-ready documentation and chat-only onboarding
- Document the source-verified public macro API, including the case-sensitive `\EN` semantics and project-specific availability.
- Add a chat-only handbook, Persian starter prompt, and workflow for proposing reusable components.
- Package project-specific `AI_START_HERE.md` and `AI_MACROS.md` from canonical documentation in each generated project; add focused regression checks.

## Unreleased — Letter and resume templates (2026-11-05)
- Reduce over-reservation of Persian letter closings and tighten optional Modern administrative letterhead spacing; document Linux font discovery for XeLaTeX.
- Add a second production English CV with ModernCV while preserving the Article CV as the default; `resume-en --style article|moderncv` selects either explicitly.
- Correct optional metadata checks in letters and CVs, constrain Persian logo height and width, and make pagination tests independent of an exact page count.
- Add classic and modern Persian/English letters with shared metadata and content, optional Persian letterhead fields, and pagination controls for final paragraphs and signatures.
- Add an article-based English CV with repeatable entries, optional sections, and section pagination controls.
- Extend the shared generator with `letter-fa`, `letter-en`, `resume-en`, and generation-time `--style` selection for letters; standalone remains the default.
- Add template guides, font configuration, generator and XeLaTeX tests, and rendered review artifacts. No font binaries are distributed.

## Unreleased — Foundation improvements (2026-11-04)
- Make generated assignment, lab, and OS projects standalone snapshots by default, with explicit Git submodule mode retained.
- Share a standard-library Python generator across templates and keep PowerShell entry points as thin wrappers; stage projects before final placement.
- Add pre-load project font configuration for installed Persian and Latin fonts while preserving Vazirmatn and existing Latin defaults.
- Clarify the current Vazirmatn OS default, neutralize OS starter metadata, and remove historical submission guidance from current docs.
- Generalize circuit-specific lab starter headings without changing its layout or two-stage behavior.
- Allow source PDF assets in generated Git projects and keep font binaries ignored.
- Add generator and font regression coverage; document Windows/Ubuntu creation and optional latexmk compilation.
- Resolve destination symlinks before toolkit-boundary checks and reject Git submodule styles that differ from the local template's required styles.

## Documentation: Latin text and English equivalents — 2026-11-01
- Clarify `\lr{}` for ordinary Latin without parentheses, `\EN{}` for a parenthesized English equivalent, and `\Term{}{}` for a Persian term with its parenthesized English equivalent.
- Update AI instructions, component examples and the Windows workflow guide. No changes to macros, fonts or public LaTeX API.

## OS single-question font consistency fix — 2026-10-27
- Restore Vazirmatn (Scale=1.05) as the default Persian, text-digit and math-digit font, exactly like `persian-kit.sty`.
- Keep font choice deterministic; no Noto Sans Arabic fallback or font binaries in the repository.
- Support explicitly supplied local Regular/Bold TTF files from each project's `fonts/` directory.
- Load the vendored style with `\input` to avoid the package-name mismatch warning.
- Keep the existing two-student layout and RTL punctuation commands intact.

## OS single-question RTL punctuation fix — 2026-10-27
- Mirror the Latin fallback font punctuation at the two edges of Persian parentheses and square brackets; direct `( ) [ ]` are not provided by the Noto Sans Arabic font in this setup.
- Extend the XeLaTeX RTL regression with multiline Persian bracketed text and embedded Latin `fork()`.
- Keep the original `persian-kit` and `persian-lab` typography unchanged.

## Docs update — 2026-10-21
- Added a complete Windows / Git / XeLaTeX / AI-assisted assignment workflow in `docs/WORKFLOW_ZERO_TO_PDF_FA.md`.
- Added root and assignment-scoped `AGENTS.md` guidance for AI tools.
- No LaTeX API changes (compatible with v1.2.0).

# Changelog

## Unreleased — Default font changed to Vazirmatn
- Removed obsolete `APPLY_PATCH_FA.txt` ZIP-update instructions; use the maintained Git workflow docs instead.
- Add a TeX Live 2026 `array`/`bidi` table-compatibility fallback and cover `HWTable` in the smoke test.
- Require Vazirmatn for Persian text and for text/math digits (XeLaTeX + XePersian).
- Remove the silent B Nazanin/Amiri fallback; missing Vazirmatn now triggers a clear package error.
- Refresh Windows setup, assignment workflow, AI instructions, and a dedicated font smoke test.
- No font binaries are distributed; existing templates and the new-assignment script use the kit automatically.

## 1.2.0 — Generic homework master template (2026-10-21)
- Added automatic question and part heading commands (HWQuestion, HWPart, HWSubpart).
- Improved assignment title, metadata card, Persian page footer and stable page layout.
- Added due date metadata and generic question 2 table example.
- Expanded Windows project setup workflow and usage documentation.
- No actual student/course data or font binaries are distributed.

## 1.1.0 — Git-ready course-neutral library (2026-10-19)
- Extracted the original XePersian design into `tex/persian-kit.sty`.
- Removed course-specific student data and assignment answers from the reusable library.
- Added generic homework starter, standalone showcase, reusable component snippets and Windows/Git instructions.
- Added scoped `HWTable` environment and Git-safe `.gitignore`.
- Documented Git submodules for reuse across courses.

## 1.0.0 — Original homework starter (2026-10-18)
- XePersian theme with preferred B Nazanin and Amiri fallback.
- Colored tables, note boxes, figures, formulas and heading hierarchy.

## Unreleased — Laboratory report starter (2026-10-27)
- Add generic two-stage lab-report template with separate predicted and observed sections.
- Add `persian-lab.sty` with numbered and referenceable `LabFigure` / `LabTable` wrappers, preserving homework APIs.
- Add Windows creation script, guide, snippet, and smoke test.
- No actual experiment answers or photographic evidence stored in the public kit.
- Provide a course-neutral, content-free lab starter with an independent report title.

## Unreleased — Word-compatible OS single-question template (2026-10-27)
- Add isolated `tex/persian-os.sty` with Noto Sans Arabic and Word-style OS header, footer, two-student table and section design.
- Add `templates/os-single-question` as a one-question/one-PDF project, independent of the generic multi-question assignment template.
- Add `scripts/new-os-homework.py` and PowerShell entry point with Git submodule by default and explicit `--offline` snapshot mode.
- Add visual layout and RTL/punctuation smoke tests, Git project-generator tests, and a Persian setup/delivery guide. No actual student names or answers in the shared kit.
- Existing `persian-kit.sty`, `persian-lab.sty` and their creation scripts remain unchanged.
