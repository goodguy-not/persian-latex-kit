# AI handbook: working with Persian LaTeX Kit

This guide is for assistants with or without repository access. A generated
project receives the relevant sections as `AI_START_HERE.md` and a matching
`AI_MACROS.md`; read those **inside the project** before its source. The
project's copied definitions are authoritative for that snapshot.

## Rules for every generated project
<!-- projects: all -->

Persian LaTeX Kit is a reusable library and a generator for assignments, lab
reports, a historical one-question OS layout, Persian and English letters, and
two English CV designs. The library repository owns reusable styles and starter
templates. A generated project is an independent document snapshot: edit its
content and metadata there, not in the public library. Standalone generation
needs no Git or network and does not auto-update. Some project types have
`vendor/persian-latex-kit/tex/*.sty`; letters and CVs do not.

**Read in order:** this `AI_START_HERE.md`, local `AI_MACROS.md`, local
`AGENTS.md`, `main.tex`, the relevant content file, `config/metadata.tex`,
`config/fonts.tex`, and any copied style or `letter-parts.tex` needed to check
a command. Read the user's assignment or document instructions as evidence.
Use only macros present in this project. `AI_MACROS.md` distinguishes kit
commands, template commands, and external LaTeX/package commands. Do not infer
behavior from a command's name. A missing command is not implemented merely
because newer online docs mention it.

Normally edit the named content files, `config/metadata.tex` for identity and
document facts, `config/fonts.tex` for installed font choices, and user-owned
assets under `assets/`. Edit `main.tex` only to include or omit an existing
section or when the task specifically requires a structural change. Preserve
the selected document class, layout, style files, `vendor/`, and other content.
Do not put real student data, answers, private assets, or font binaries into
the public kit. For a proposed reusable change, first check existing commands
and packages, distinguish a local need from a shared one, then describe the
name, arguments, source location, dependencies, RTL/LTR behavior, and
compatibility impact. A reusable change belongs in the canonical kit source,
not solely in a project's vendored snapshot. In a chat-only setting, describe
the proposal separately and never claim it is already installed.

Compile `main.tex` **from this project's root** with XeLaTeX, normally twice
for references: `xelatex -interaction=nonstopmode -halt-on-error main.tex`.
Persian projects require XePersian and an installed selected Persian font;
English projects use `fontspec` and their selected fonts. Font families must
be discoverable by XeLaTeX; no font is downloaded or silently substituted.
Keep Persian prose and punctuation in RTL; use an appropriate LTR command for
ordinary Latin spans. Review the PDF for glyphs, overflow, labels, page breaks,
and font embedding when a compiler and viewer are available.

If you only have uploaded files in a chat, inspect them and produce **complete
copyable source** for the exact existing destination file. If a file artifact
can actually be created, attach it too. For a request about one question or
section, return only that file unless more is requested. Put LaTeX in a fenced
`latex` code block so backslashes do not become chat math. State assumptions,
missing inputs, and whether compilation or visual PDF inspection actually
occurred. Never claim to have edited the user's computer or compiled a PDF
unless you did. Do not invent measurements, credentials, institutional logos,
or academic results.

## Assignment project
<!-- projects: assignment -->

**Identity:** multi-question Persian assignment, `main.tex` loads
`vendor/persian-latex-kit/tex/persian-kit.sty`. It inputs
`questions/question01.tex`; additional `questions/questionNN.tex` files are
included only when `main.tex` names them. Read the actual `\input` lines.
Metadata and fonts are in `config/metadata.tex` and `config/fonts.tex`.

For one requested question, return the complete replacement for that
`questions/questionNN.tex`, including its `\HWQuestion` heading and relevant
`\HWPart`/`\HWSubpart` headings. Do not return a second question or rewrite
`main.tex` unless asked. Use `\lr` for ordinary Latin; `\EN` only to introduce
a parenthesized English equivalent after Persian; `\Term` for a bold Persian
term with its English equivalent. **There is no `\En` command.** For math use
standard LaTeX math; for kit tables/figures/boxes use `AI_MACROS.md`. Preserve
the assignment title, fonts, and vendored style.

## Lab report project
<!-- projects: lab-report -->

**Identity:** Persian prelab or final lab report. `main.tex` loads
`vendor/persian-latex-kit/tex/persian-kit.sty` and then
`vendor/persian-latex-kit/tex/persian-lab.sty`. It inputs
`sections/01-objective.tex`, `sections/02-specification.tex`,
`sections/03-design.tex`, `sections/04-tests.tex`, then either
`sections/05-evaluation-plan.tex` (prelab) or `sections/05-results.tex`
(final), and `sections/06-conclusion.tex`. `\LabFinalfalse`/`\LabFinaltrue` in
`config/metadata.tex` selects the branch. Fonts are in `config/fonts.tex`.

For one requested section, return only its complete `sections/*.tex` content.
Use `\LabFigure`/`LabTable` for numbered floats. Do not present a planned
measurement as observed; switch to final only when supplied evidence supports
it. The lab shares the kit's text and table commands but uses `\MakeLabTitle`,
not the homework title or question headings. Consult `AI_MACROS.md` for scope.

## OS single-question project
<!-- projects: os-single-question -->

**Identity:** one Persian OS question per project and PDF. `main.tex` loads
`vendor/persian-latex-kit/tex/persian-os.sty` and inputs exactly one
`questions/questionNN.tex`; read the actual `\input` line because generation
may rename `question01.tex`. `config/metadata.tex` contains the question
number, course, and two-student title fields; `config/fonts.tex` contains
font choices. There is no `persian-kit.sty` in this design.

For one requested answer, return only the complete existing question file.
Use `\OSPart` for parts, `\OSLatin` or XePersian `\lr` for ordinary Latin,
`\OSParen`/`\OSBracketed` for Persian punctuation, and `latin` plus
`lstlisting[style=OSCode]` for C code. `\EN`, `\Term`, `\HWQuestion`, and
`\MakeHomeworkTitle` are unavailable. Remove sample placeholders from final
answers. Do not add a second question to this project.

## Persian letter project
<!-- projects: letter-fa -->

**Identity:** Persian `article` letter with XePersian. The selected Classic
or Modern presentation is already in `main.tex`; keep it. Edit
`content/body.tex` for ordinary paragraphs and
`content/final-paragraph.tex` for the last paragraph, which stays with the
closing/signature when practical. Edit sender, recipient, date, subject,
greeting, closing, optional organization, number, attachment, opening phrase,
and authorized logo path in `config/metadata.tex`. Fonts are in
`config/fonts.tex`; any sender-owned logo belongs in `assets/`.

For a request about only the body, return only the specified content file.
Do not duplicate the greeting or closing in content. Use XePersian `\lr` for
ordinary Latin; assignment `\EN` and `\Term` are unavailable. Leave optional
organizational fields empty when not provided. Preserve the selected layout
and check pagination and signature placement if a PDF can be inspected.

## English letter project
<!-- projects: letter-en -->

**Identity:** Classic uses standard `letter`; Modern uses KOMA-Script
`scrlttr2`. The selected class and layout are already in `main.tex`.
Ordinary paragraphs go in `content/body.tex`; the last paragraph goes in
`content/final-paragraph.tex` with the closing/signature. Edit identity,
recipient, subject, date, salutation, and sign-off values in
`config/metadata.tex`; fonts in `config/fonts.tex`.

Return only the requested content file for a one-section task. Do not paste a
new document class, greeting, or signature into body content. Preserve the
Classic Termes or Modern Heros default unless the user's actual formatting
requirements justify an installed alternative. Persian kit and OS macros are
unavailable. Check page breaks when a PDF can be inspected.

## Article CV project
<!-- projects: resume-article -->

**Identity:** `resume-en` default or `--style article`; `main.tex` uses
standard `article`, not ModernCV. Candidate identity and profile are in
`config/metadata.tex`; font choice is in `config/fonts.tex`. Content files are
`sections/education.tex`, `sections/experience.tex`,
`sections/projects.tex`, `sections/skills.tex`,
`sections/languages.tex`, `sections/research.tex`, `sections/honors.tex`, and
`sections/publications.tex`.
`main.tex` inputs them in that order; comment an optional `\input` to omit it.

Return only the requested `sections/*.tex` for a section task. Use local
`\CVSection`, `\CVDatedEntry`, `\CVExperience`, `\CVProject`, and `\CVLine`
as appropriate; these are detailed in `AI_MACROS.md`. Do not use ModernCV
`\cventry` unless the project actually loads ModernCV. Keep claims factual
and readable; there is no ATS guarantee.

## ModernCV project
<!-- projects: resume-moderncv -->

**Identity:** `resume-en --style moderncv`; `main.tex` loads the external
`moderncv` class. Candidate fields and profile are in `config/metadata.tex`,
font choice in `config/fonts.tex`. Content files are
`sections/education.tex`, `sections/experience.tex`,
`sections/projects.tex`, `sections/skills.tex`, `sections/languages.tex`,
`sections/research.tex`, `sections/honors.tex`, and
`sections/publications.tex`; `main.tex` inputs them. Their syntax follows
ModernCV, not the Article CV.

Return only the requested section file for a section task. Use the local
`\CVSection` heading and ModernCV's external `\cventry`/`\cvitem` rows.
Article `\CVExperience`, `\CVProject`, `\CVDatedEntry`, and `\CVLine` are
unavailable. Preserve the selected ModernCV class and style; omit an optional
section by changing its `\input` only when requested. There is no ATS guarantee.
