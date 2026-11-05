# English business letter

This standalone project uses the Classic standard `letter` class or the Modern
KOMA-Script `scrlttr2` class selected during generation. Edit
`config/metadata.tex`, `content/body.tex`, and `content/final-paragraph.tex`.
The final paragraph stays with the closing where space permits. Set installed
font names in `config/fonts.tex`; the Classic default is TeX Gyre Termes and
the Modern default is TeX Gyre Heros. Optional sender organization and phone
fields may be left empty.

Compile from this project root with `xelatex -interaction=nonstopmode
-halt-on-error main.tex` (twice if references are added). See the toolkit's
`docs/DOCUMENT_TEMPLATES.md` for configuration details.
