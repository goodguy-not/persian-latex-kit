# AI editing guide — homework project

This is an individual assignment consuming the reusable `vendor/persian-latex-kit` Git submodule.

- Read `main.tex`, `config/metadata.tex`, relevant `questions/*.tex`, and `vendor/persian-latex-kit/tex/persian-kit.sty` before editing. Read `vendor/persian-latex-kit/docs/COMPONENTS_FA.md` if available.
- Use **XeLaTeX**. Text is Persian RTL; use `\EN{Latin}` or `\Term{فارسی}{Latin}` to avoid misplaced parentheses and punctuation. Prefer the shared kit's B Nazanin font selection.
- Edit assignment metadata only in `config/metadata.tex`. Write each question in a separate `questions/questionNN.tex`, included via `main.tex`.
- Use shared `\HWQuestion`, `\HWPart`, `\HWSubpart`, `HWTable`, `HWTip`, `HWWarning`, `\HWFigure`, and standard math environments where appropriate.
- Do not redefine global colors, heading formats, or fonts in a question. Never edit `vendor/persian-latex-kit` directly; propose generic components as changes to the library repository.
- Base answers on the supplied assignment statement. Include essential intermediate calculations, and indicate ambiguity rather than guessing. Do not pretend to have validated an unseen question or data.
- Keep personal metadata and solutions out of the *public library* repo. The user decides where individual assignments are shared.
- Compile `main.tex` with XeLaTeX, inspect for broken RTL, misplaced parentheses, overflowing tables/equations, and Persian page numerals before delivery. If unable to compile, say so explicitly.
