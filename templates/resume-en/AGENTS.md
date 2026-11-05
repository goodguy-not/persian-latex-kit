# English CV project guidance

Begin with `AI_START_HERE.md` and `AI_MACROS.md` in this generated project.

This is the default Article variant of `resume-en`; the separate ModernCV
variant is selected with `--style moderncv` during generation.

Preserve the article layout and TeX Gyre Heros default unless a document
requirement justifies a change. Edit fictional metadata and section files for
the actual candidate only in the generated project. Repeat `\CVExperience` and
`\CVProject` for arbitrary entries; omit optional section inputs in `main.tex`
when unused. Use `\CVSection` for custom sections so the heading stays with
the beginning of its content. Keep text readable instead of shrinking it to
force a single page. Compile with XeLaTeX and inspect every page and embedded
fonts.
