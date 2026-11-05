# Persian business letter

This project was generated as a standalone snapshot. `main.tex` is the chosen
Classic or Modern article/XePersian presentation. Edit `config/metadata.tex`,
`content/body.tex`, and `content/final-paragraph.tex`; keep the last paragraph
with the closing by putting it in the latter file. Font overrides are in
`config/fonts.tex`. Optional personal or organizational letterhead fields are
empty by default. A sender-owned logo may be placed in `assets/` and referenced
through `\SenderLogoFa`; missing assets fail compilation.

Compile from this project root with `xelatex -interaction=nonstopmode
-halt-on-error main.tex` (twice if references are added). See the toolkit's
`docs/DOCUMENT_TEMPLATES.md` for configuration details.
