# English ModernCV

This standalone project uses the `moderncv` class and the restrained Classic
style with TeX Gyre Heros by default. Install XeLaTeX, ModernCV, `fontspec`,
`geometry`, `needspace`, and `etoolbox` in your TeX distribution. No class or
font binaries are bundled. A missing class or selected font produces an error.

Edit contact details in `config/metadata.tex` and the installed font in
`config/fonts.tex`. Edit individual `sections/*.tex` files. Repeat `\cventry`
for as many experiences or education entries as needed, and `\cvitem` for
projects, skills, or other content. Add custom sections with `\CVSection`.
Comment out optional research, honors, or publications inputs in `main.tex`
to remove those sections entirely.

Compile from this project root with
`xelatex -interaction=nonstopmode -halt-on-error main.tex` twice. Inspect the
resulting PDF for pagination, legibility, and embedded fonts.
