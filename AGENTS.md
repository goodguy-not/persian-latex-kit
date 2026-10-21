# Rules for AI assistants working on Persian LaTeX Kit

This repository is a reusable, course-independent LaTeX component library, NOT a place for individual homework answers or student personal data.

1. Read `README.md`, `tex/persian-kit.sty`, `docs/COMPONENTS_FA.md`, and `docs/WORKFLOW_ZERO_TO_PDF_FA.md` before edits.
2. Use XeLaTeX and XePersian. Prefer B Nazanin if installed; never commit font binaries. Keep Persian RTL and Latin spans isolated with `\EN{}` or `\Term{}{}`.
3. Never claim that a macro exists without checking the source. Reuse existing components rather than duplicating styles.
4. Put reusable components in library source, examples in `examples/snippets/`, documentation in `docs/`, and a change entry in `CHANGELOG.md`.
5. Keep course names, real student IDs, homework text, and attachments out of the library repository.
6. Do not edit a consumer project's `vendor/persian-latex-kit` directly; update the actual library repo and advance the submodule pointer only when requested.
7. Compile representative tests using XeLaTeX and visually inspect the PDF before calling a change complete. Tell the user explicitly when compilation is not possible.
8. Preserve Git history. Never force-push or overwrite uncommitted user changes without authorization.
