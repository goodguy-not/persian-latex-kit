# Rules for AI assistants working on Persian LaTeX Kit

This repository is a reusable, course-independent LaTeX component library, NOT a place for individual homework answers or student personal data.

1. Read `README.md`, `tex/persian-kit.sty`, `docs/COMPONENTS_FA.md`, and `docs/WORKFLOW_ZERO_TO_PDF_FA.md` before edits.
2. Use XeLaTeX and XePersian. Require Vazirmatn for Persian text and text/math digits; never commit font binaries or silently fall back to another font. Keep Persian RTL and Latin spans isolated with `\EN{}` or `\Term{}{}`.
3. Never claim that a macro exists without checking the source. Reuse existing components rather than duplicating styles.
4. Put reusable components in library source, examples in `examples/snippets/`, documentation in `docs/`, and a change entry in `CHANGELOG.md`.
5. Keep course names, real student IDs, homework text, and attachments out of the library repository.
6. Do not edit a consumer project's `vendor/persian-latex-kit` directly; update the actual library repo and advance the submodule pointer only when requested.
7. Compile representative tests using XeLaTeX and visually inspect the PDF before calling a change complete. Tell the user explicitly when compilation is not possible.
8. Preserve Git history. Never force-push or overwrite uncommitted user changes without authorization.

9. The historical Word-style operating-systems design lives ONLY in `tex/persian-os.sty` and `templates/os-single-question`. It intentionally uses `Noto Sans Arabic`; never substitute the generic kit's Vazirmatn or merge it with the multi-question layout. Avoid storing real student details in the shared template. Test Persian RTL punctuation (`، ؛ ؟ « »`), OSParen/OSBracketed and OSDateRange, and isolate Latin terms with OSLatin; avoid raw ASCII bracket glyphs with Noto Sans Arabic.
