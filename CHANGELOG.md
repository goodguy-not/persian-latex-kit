## Docs update — 2026-10-21
- Added a complete Windows / Git / XeLaTeX / AI-assisted assignment workflow in `docs/WORKFLOW_ZERO_TO_PDF_FA.md`.
- Added root and assignment-scoped `AGENTS.md` guidance for AI tools.
- No LaTeX API changes (compatible with v1.2.0).

# Changelog

## Unreleased — Default font changed to Vazirmatn
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
