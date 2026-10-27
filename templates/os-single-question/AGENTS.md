# AI instructions: one-question Operating Systems template

- Read `main.tex`, `config/metadata.tex`, `questions/questionNN.tex`, and `vendor/persian-latex-kit/tex/persian-os.sty` before making changes.
- Preserve the layout of the supplied OS Word template. Do not introduce the generic `\MakeHomeworkTitle` or `\HWQuestion` styles.
- Each independent project builds **one question only**. Edit only the answer in the single `questions/questionNN.tex`; create another project for a second question. Never concatenate several theoretical questions into the same PDF by default.
- Metadata are in `config/metadata.tex` only; keep private student information outside the public kit repository.
- Draft final answers in Persian. Isolate English technical names with `\lr{}` or `\OSLatin{}`; use `latin` + `lstlisting` for C code, and mathematical environments for formulas.
- Avoid making up assumptions, outputs or experiments. Verify the task statement, calculations, and process trees before handing in an answer.
- XeLaTeX must compile and the PDF must be visually reviewed for RTL, margins, long answers, code, table, and page footer. Never change the selected font to hide a compilation error.
