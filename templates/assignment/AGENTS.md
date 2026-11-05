# AI editing guide — homework project

Begin with this generated project's `AI_START_HERE.md` and `AI_MACROS.md`.

This is an individual assignment with a frozen copy of the required style in `vendor/persian-latex-kit` (or an explicitly selected Git submodule).

- Read `main.tex`, `config/metadata.tex`, relevant `questions/*.tex`, and `vendor/persian-latex-kit/tex/persian-kit.sty` before editing. The project-local `AI_MACROS.md` documents this snapshot's usable API.
- Use **XeLaTeX**. Text is Persian RTL. Use `\lr{TCP}` for ordinary Latin text without parentheses; use `\EN{Transmission Control Protocol}` only for an English equivalent in parentheses; use `\Term{کنترل ازدحام}{Congestion Control}` for a Persian term with its English equivalent. `\EN{}` inserts parentheses automatically. Default Persian font is Vazirmatn; optional installed-font choices belong only in `config/fonts.tex`, never in question files.
- Edit assignment metadata only in `config/metadata.tex`. Write each question in a separate `questions/questionNN.tex`, included via `main.tex`.
- Use shared `\HWQuestion`, `\HWPart`, `\HWSubpart`, `HWTable`, `HWTip`, `HWWarning`, `\HWFigure`, and standard math environments where appropriate.
- Do not redefine global colors, heading formats, or fonts in a question. Never edit `vendor/persian-latex-kit` directly; propose generic components as changes to the library repository.
- Base answers on the supplied assignment statement. Include essential intermediate calculations, and indicate ambiguity rather than guessing. Do not pretend to have validated an unseen question or data.
- Keep personal metadata and solutions out of the *public library* repo. The user decides where individual assignments are shared.
- Compile `main.tex` with XeLaTeX, inspect for broken RTL, misplaced parentheses, overflowing tables/equations, and Persian page numerals before delivery. If unable to compile, say so explicitly.
