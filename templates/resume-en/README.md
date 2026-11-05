# English article CV

This is the default `resume-en` style; `--style article` selects it explicitly.
This standalone 11 pt article CV uses TeX Gyre Heros by default. Edit contact
details in `config/metadata.tex`, the installed font in `config/fonts.tex`, and
the individual `sections/*.tex` files. In `main.tex`, comment out optional
research, honors, or publications inputs to remove those sections. Repeat
`\CVExperience` and `\CVProject` as needed; add custom sections with
`\CVSection{Title}`. Keep enough content under a heading for a clean page break.

Compile from this project root with `xelatex -interaction=nonstopmode
-halt-on-error main.tex` (twice if references are added). See the toolkit's
`docs/DOCUMENT_TEMPLATES.md` for configuration details.
