# Persian LaTeX Kit: public macro reference

This is the canonical reference for the source in this repository. The generator
copies only the sections relevant to a new project into its `AI_MACROS.md`.
For an older standalone snapshot, **its own source and `AI_MACROS.md` take
precedence** over newer online documentation. LaTeX command names are case
sensitive. Examples assume XeLaTeX from the generated project's root.

Signatures: `{x}` is required; `[x]` is optional; `environment{...}` names the
arguments after `\begin{environment}`. A configuration command is set in
`config/metadata.tex` or `config/fonts.tex`, not called as document content.
Library styles are under `vendor/persian-latex-kit/tex/` in standalone projects.
Commands marked **external** are supplied by LaTeX, XePersian, or another
package, not by this kit. Commands marked **internal** are implementation
details, not a supported content API.

## Persian academic text and English terminology
<!-- projects: assignment,lab-report -->

Source: `tex/persian-kit.sty`, copied as `vendor/persian-latex-kit/tex/persian-kit.sty`.
Scope: assignments and lab reports only. This style loads XePersian, `fontspec`
through XePersian, and the packages listed in the other sections below.

| Command | Meaning, signature, and result | Correct example | Do not use / alternative |
|---|---|---|---|
| `\EN{English equivalent}` | One required argument. `\lr{(#1)}`: a left-to-right English equivalent **with its own parentheses** after a Persian term. | `تجزیهٔ مقادیر منفرد \EN{Singular Value Decomposition, SVD}` | Not for every English word or a standalone acronym; `\lr{SVD}` is ordinary inline Latin. Do not add another pair of parentheses. |
| `\Term{Persian}{English}` | Two required arguments. Bold Persian term, a space, then `\EN{English}`. | `\Term{تجزیهٔ مقادیر منفرد}{Singular Value Decomposition, SVD}` | Do not use when the Persian term should not be bold or when no English equivalent is being introduced; use ordinary text plus `\lr` or `\EN`. |
| `\SmallNote{text}` | One required argument. Smaller text in the kit's muted color; works in ordinary text. | `\SmallNote{فرض: ورودی معتبر است.}` | Not a footnote or citation; use standard `\footnote` when a real footnote is required. |

**Critical spelling:** there is **no `\En` command** in the current source.
Use uppercase `\EN`. `\EN{SVD}` after no Persian term merely adds parentheses;
`\EN{TCP}` as a replacement for every inline Latin acronym is a semantic
mistake. `\EN{(SVD)}` doubles the parentheses. The full term and abbreviation
can be introduced once as in the example above; later occurrences can use
`\lr{SVD}`. `\Term` already calls `\EN`, so do not wrap its second argument.

`\lr{text}` is an **external XePersian** direction command: inline Latin/LTR
text without punctuation added, e.g. `پروتکل \lr{TCP} بررسی شد.`
`\textenglish{text}` is **not defined by this kit or the XePersian source
loaded by these templates**. A different language package might provide it in
another document; do not assume it exists in a generated project. Use `\lr`
for short ordinary inline Latin here. Keep Persian punctuation `، ؛ ؟ « »` in Persian
RTL context, outside an LTR span. Neither `\EN` nor `\Term` is available in
OS, letters, or CVs unless that project's source explicitly defines it.

## Questions, answers, and assignment metadata
<!-- projects: assignment -->

Source: `tex/persian-kit.sty`; the assignment `main.tex` calls the first two
commands after loading `config/metadata.tex`.

| Command | Meaning, signature, and result | Correct example | Do not use / alternative |
|---|---|---|---|
| `\HWActivateAssignmentLayout` | No arguments. Selects the XePersian-aware plain page style and Persian footer page number. | `\HWActivateAssignmentLayout` once in `main.tex`. | Not a question heading; do not call for each question. |
| `\MakeHomeworkTitle` | No arguments. Renders the assignment title and metadata box using `\HW...` values. | `\MakeHomeworkTitle` once after `\begin{document}`. | Not a lab title; lab uses `\MakeLabTitle`. |
| `\HWQuestion[short title]` | Optional title, no required arguments. Advances the section counter and prints `سؤال N` with an optional muted subtitle. | `\HWQuestion[تحلیل الگوریتم]` | Not an OS heading. Each assignment question normally lives in its own `questions/questionNN.tex`. |
| `\HWPart{label}[short title]` | Required Persian part label, optional subtitle. Prints `قسمت label`. | `\HWPart{الف}[پیچیدگی زمانی]` | Do not expect automatic part letters; supply the label. |
| `\HWSubpart{heading}` | Required heading, rendered as an unnumbered third-level heading. | `\HWSubpart{حالت بدترین ورودی}` | Not for a new question; use `\HWQuestion`. |

## Shared kit metadata and font configuration
<!-- projects: assignment,lab-report -->

Metadata defaults are `\providecommand` definitions in `persian-kit.sty`;
the project overrides them with `\renewcommand{\Name}{value}` in
`config/metadata.tex`. Each has **no call-time arguments** and is consumed by
`\MakeHomeworkTitle`. The example form is
`\renewcommand{\HWCourse}{ساختمان داده}`. Set real identities only in a
private generated project. These are title fields, not content macros:

| Field | Purpose and output |
|---|---|
| `\HWStudentName` | Student name in the title box. |
| `\HWStudentID` | Student identifier in the title box. |
| `\HWCourse` | Course name. |
| `\HWProfessor` | Instructor name. |
| `\HWTerm` | Academic term. |
| `\HWAssignment` | Prominent assignment title. |
| `\HWInstitution` | Institution beneath the title. |
| `\HWDeadline` | Due date. |

The default Persian font is Vazirmatn. Define `\PLKPersianFont` and/or
`\PLKLatinFont` with `\newcommand{\PLKPersianFont}{Installed Family}` in
`config/fonts.tex` **before** loading the style; they take no call-time
arguments. The selected Persian family sets text and text/math digits;
an explicitly missing font causes a package error. Do not set fonts inside a
question. The Latin default is Times New Roman if found, otherwise Liberation
Serif. Font binaries are not included.

## Mathematics and equations
<!-- projects: assignment,lab-report,os-single-question -->

There is no kit-specific equation macro. `\[...\]`, `equation`, `align`,
`\frac`, `\sum`, and `\label`/`\ref` are **external** LaTeX/`amsmath`
commands; `amsmath` and `amssymb` are loaded by the Persian styles. Example:

```latex
\[
  \overline{W}=\frac{1}{n}\sum_{i=1}^{n}W_i
\]
```

Put math in math mode. Do not invent a kit `\Formula` command. Text labels
inside math need the appropriate text command, and Latin technical terms in
Persian prose still need direction handling. `\UseMathForPositioningText` in
the Persian styles is an **internal bidi compatibility hook**, not a formula
command or a user-facing API.

## Tables
<!-- projects: assignment,lab-report -->

Source: `tex/persian-kit.sty`; dependencies: `xcolor[table]`, `array`,
`tabularx`, `booktabs`, and `multirow` loaded by the style.

| Command/environment | Meaning, signature, and result | Correct example | Do not use / alternative |
|---|---|---|---|
| `HWTable{column spec}` | Required `tabularx` column specification, followed by table body between `\begin` and `\end`. Applies scoped stripes and column spacing to a width near `\linewidth`. | `\begin{HWTable}{CY} A & B\\ \end{HWTable}` | Does not create a floating table, caption, number, or label. Use `LabTable` in a lab for those. |
| `\HWTableHead{cell text}` | One required argument. White bold text for a colored header cell. | `\rowcolor{HWNavy}\HWTableHead{ردیف} & \HWTableHead{نتیجه}\\` | Set an appropriate row color; white text on a white row is unreadable. |
| `Y`, `C` | Kit column types inside a `tabularx` column spec. `Y` is right-aligned flexible text; `C` centered flexible text. | `\begin{HWTable}{CY}` | Not commands in prose; standard `p{}`, `l`, `c`, etc. remain available. |
| `\HWTableStart`, `\HWTableEnd` | No arguments. Legacy pair to enable alternating row color and increased row height in a hand-written table, then stop row coloring. | `\HWTableStart\begin{tabular}{cc} ... \end{tabular}\HWTableEnd` | Prefer scoped `HWTable`; do not omit `\HWTableEnd` when using the pair. |

`\rowcolor`, `tabularx`, and `\arraybackslash` are **external** package
commands. Escape literal `&` as `\&` in cells. Long data tables may need a
different standard environment; `HWTable` does not span pages.

## Figures, diagrams, and note boxes
<!-- projects: assignment,lab-report -->

Source: `tex/persian-kit.sty`; `graphicx`, `float`, `tcolorbox`, and `xcolor`
are loaded by the style. Image paths refer to assets in the generated project.

| Command/environment | Meaning, signature, and result | Correct example | Do not use / alternative |
|---|---|---|---|
| `\HWFigure[width fraction]{path}{caption text}` | Optional fraction defaults to `0.85`; two required arguments. Floating centered image at fraction of `\linewidth`, then a small muted **unnumbered** caption-like line. | `\HWFigure[0.7]{assets/diagram.png}{نمودار معماری}` | Not for numbered figure references; use `\LabFigure` in lab or a standard `figure` with `\caption`/`\label`. File must exist. |
| `HWTip[box options]` | Optional `tcolorbox` options. Breakable light box with a teal rule. | `\begin{HWTip}فرض مسئله روشن است.\end{HWTip}` | Not a mathematical theorem environment or a citation. |
| `HWWarning[box options]` | Optional `tcolorbox` options. Breakable light box with a blue rule. | `\begin{HWWarning}واحدها را بررسی کنید.\end{HWWarning}` | Not a compiler warning mechanism. |

## Lab reports
<!-- projects: lab-report -->

Sources: `tex/persian-lab.sty` **after** `tex/persian-kit.sty`, plus the kit
commands described in the shared sections above. The lab `main.tex` includes
one of two section files depending on `\ifLabFinal`.

| Command/environment | Meaning, signature, and result | Correct example | Do not use / alternative |
|---|---|---|---|
| `\LabFinalfalse`, `\LabFinaltrue` | No arguments. Select prelab evaluation-plan section or final results section. | `\LabFinalfalse` in `config/metadata.tex` before results exist. | Do not claim a final experiment or measurements without evidence. These switches do not create results. |
| `\MakeLabTitle` | No arguments. Lab-specific title and metadata box; says prelab or final report according to the switch. | `\MakeLabTitle` once in `main.tex`. | Do not also render `\MakeHomeworkTitle`. |
| `\LabFigure[width fraction]{path}{caption}{label}` | Optional fraction defaults to `0.85`; three required arguments. Floating image with numbered caption **below** and cross-reference label. | `\LabFigure[0.75]{assets/schematic.png}{شماتیک مدار}{fig:schematic}` | Not for an image without a real asset; `\HWFigure` is unnumbered. |
| `LabTable{caption}{label}{column spec}` | Three required arguments, then table body. Floating numbered table with caption **above** and an inner `HWTable`. | `\begin{LabTable}{نتایج}{tab:results}{CY} ۱ & مقدار\\ \end{LabTable}` | Not for multi-page tables; use `\ref{tab:results}` only after compiling references. |

The four lab fields `\LabExperimentNumber`, `\LabExperimentName`,
`\LabSessionDate`, and `\LabReportDate` are no-argument values defined in
`persian-lab.sty` and overridden in `config/metadata.tex`, e.g.
`\renewcommand{\LabExperimentName}{آزمایش مدار منطقی}`. They print in the lab
title; the name also appears as its heading. Do not put measured results in a
metadata field. The lab also uses the `\HWInstitution`, `\HWCourse`,
`\HWProfessor`, `\HWStudentName`, `\HWStudentID`, and `\HWTerm` fields from
`persian-kit.sty`; see the assignment metadata table above. Its default font
variables are the same `\PLKPersianFont` and `\PLKLatinFont`, set before the
style in `config/fonts.tex`. The lab does **not** use `\HWQuestion` headings.

## OS-specific content and code
<!-- projects: os-single-question -->

Source: `tex/persian-os.sty` only, copied under `vendor/`; it does not load
`persian-kit.sty` or `persian-lab.sty`. Dependencies loaded by the style include
XePersian, `listings`, `fancyhdr`, `graphicx`, `tabularx`, and `amsmath`.
One project and PDF contain one question.

| Command/environment | Meaning, signature, and result | Correct example | Do not use / alternative |
|---|---|---|---|
| `\OSLatin{text}` | One required argument; exactly `\lr{#1}` for inline LTR technical text, with no parentheses. | `فرایند \OSLatin{fork()} اجرا شد.` | No English-equivalent semantics; `\EN` and `\Term` are unavailable here. |
| `\OSParen{Persian text}` | One required argument. Visually mirrored parentheses around RTL Persian text using Latin glyphs. | `\OSParen{بخش آ}` | Not for Latin function calls; use `\OSLatin{fork()}`. |
| `\OSBracketed{Persian text}` | One required argument. Visually mirrored square brackets around RTL Persian text. | `\OSBracketed{توضیح اختیاری}` | Do not type raw ASCII brackets around Persian prose. |
| `\OSDash` | No arguments. Em dash glyph with the style's reliable direction handling. | `بخش اول \OSDash{} بخش دوم` | Not a date-range dash; use `\OSDateRange`. |
| `\OSDateRange{start}{end}` | Two required arguments. Prints start, a direction-safe en dash, end. | `\OSDateRange{۱۴۰۵}{۱۴۰۶}` | Not for arbitrary arithmetic subtraction. |
| `\OSTechnicalTerm{Persian}{English}` | Two required arguments. Bold Persian, space, then LTR parenthesized English. | `\OSTechnicalTerm{بن‌بست}{Deadlock}` | Do not use for ordinary standalone English; use `\OSLatin`. This is OS-only, not `\Term`. |
| `\OSMakeQuestionTitle` | No arguments. Renders the one-question title, assignment/term/instructor line, and two-student table. | `\OSMakeQuestionTitle` once in `main.tex`. | Not the multi-question homework title. |
| `\OSAnswerHeading` | No arguments. Renders the “descriptive answer” heading and rule. | `\OSAnswerHeading` after the title. | Not a part heading; use `\OSPart`. |
| `\OSPart{label}[title]` | Required Persian part label, optional title. Prints `بخش (label)` and, if supplied, a dash plus title. | `\OSPart{آ}[تعریف بن‌بست]` | Not `\HWPart`; use once per actual part. |
| `\OSBodyText{text}` | One required argument. Body-colored paragraph before and after the supplied text. | `\OSBodyText{این زمان‌بندی از بن‌بست جلوگیری می‌کند.}` | Not required for every ordinary paragraph; plain Persian paragraphs also work. |
| `\OSPlaceholder{text}` | One required argument. Muted placeholder paragraph. | `\OSPlaceholder{پاسخ بررسی‌شده اینجا قرار می‌گیرد.}` | Remove placeholders from a final answer; never represent them as evidence. |
| `\OSFigure[width fraction]{path}{caption}` | Optional fraction defaults to `0.85`; two required arguments. Floating numbered figure with caption below. | `\OSFigure[0.7]{assets/process.png}{درخت فرایندها}` | File must exist; not `\HWFigure` (unavailable here). |

The style defines `OSCode` for **external `listings`**. For C source use
`\begin{latin}\begin{lstlisting}[style=OSCode] ... \end{lstlisting}\end{latin}`.
`latin` is from XePersian, `lstlisting` from `listings`; neither is a kit
environment. Do not put code inside `\OSLatin` or invent `\OSCode{...}`.
`\OSStudentTable`, `\OSSetPageStyle`, and `\OSGlyph` are **internal** helpers:
the title or document startup calls them. Do not invoke them in answer files.

OS metadata are no-argument values from `persian-os.sty`, overridden with
`\renewcommand{\Name}{value}` in `config/metadata.tex` (e.g.
`\renewcommand{\OSCourse}{سیستم‌عامل}`). They are consumed by the header,
footer, or one-question title, not called in answer text:

| Field | Purpose and output |
|---|---|
| `\OSFaculty` | Faculty in the running header. |
| `\OSCourse` | Course in the header and footer. |
| `\OSProfessor` | Instructor in the question title. |
| `\OSTerm` | Term in the question title. |
| `\OSAssignment` | Assignment series in the title and footer. |
| `\OSQuestionNumber` | The sole question number in the title. |
| `\OSStudentOneName`, `\OSStudentOneID` | First row of the two-student title table. |
| `\OSStudentTwoName`, `\OSStudentTwoID` | Second row of that table. |

`\PLKPersianFont`/`\PLKLatinFont` are selected in `config/fonts.tex` as for
the assignment, before loading this OS style. The OS-only
`\OSVazirmatnPath` instead selects two local files, `Vazirmatn-Regular.ttf`
and `Vazirmatn-Bold.ttf`, relative to the project root; define it as
`\newcommand{\OSVazirmatnPath}{fonts}`. Do not define it together with
`\PLKPersianFont`; never put font binaries into the public kit. The default
Persian font is Vazirmatn. Do not use assignment/lab macros in an OS project.

## Persian letter metadata and content
<!-- projects: letter-fa -->

Defining kit sources: `templates/letter-fa/common/config/metadata.tex`,
`templates/letter-fa/common/config/fonts.tex`,
`templates/letter-fa/common/letter-parts.tex`, and the selected
`templates/letter-fa/styles/{classic,modern}/main.tex`. The generated project
contains their copies as `config/metadata.tex`, `config/fonts.tex`,
`letter-parts.tex`, `main.tex`, `content/body.tex`, and
`content/final-paragraph.tex`; it has **no `persian-kit.sty`**. Both styles
use `article` with XePersian, `graphicx`, `etoolbox`, and `needspace`.

All fields below are no-argument configuration values created with
`\newcommand{\Field}{value}` in `config/metadata.tex`. Edit the **value** in
that file; do not add a second definition in content. Example:
`\newcommand{\LetterSubjectFa}{درخواست معرفی‌نامه}`. The style inserts them
in the letter; empty optional values suppress their associated output.

| Field | Meaning and printed result | When not / caution |
|---|---|---|
| `\SenderNameFa`, `\SenderRoleFa` | Sender name and role in heading/signature. | Use actual authorized sender data only in a private project. |
| `\SenderOrganizationFa` | Optional organization line in letterhead. | Leave empty for a personal letter; do not invent affiliation. |
| `\SenderAddressFa`, `\SenderEmailFa`, `\SenderPhoneFa` | Optional contact line; separators appear only between nonempty values. Email/phone are LTR. | No placeholder contact details in a final letter. |
| `\SenderLogoFa` | Optional sender-owned image path, e.g. `assets/logo.png`; constrained to 13 mm height and 40% text width, preserving ratio. | Leave empty without an authorized asset; no recipient logo in sender header. Missing file errors. |
| `\RecipientRoleFa`, `\RecipientOrgFa`, `\RecipientAddressFa` | Recipient block. | Verify official names and address; do not conflate sender/recipient. |
| `\LetterDateFa` | Date in administrative details. | Use an appropriate Persian date, not a fabricated submission date. |
| `\LetterNumberFa`, `\LetterAttachmentFa` | Optional administrative number and attachment labels. | Leave empty when none; do not invent official numbers. |
| `\LetterOpeningPhraseFa` | Optional centered opening phrase above letterhead. | Leave empty if not required by sender. |
| `\LetterSubjectFa`, `\LetterGreetingFa` | Subject and greeting before body. | Do not place the greeting again in `body.tex`. |
| `\LetterClosingFa`, `\SignatureTitleFa` | Closing phrase and optional signature title after final paragraph. | Do not duplicate the sign-off in `final-paragraph.tex`. |

Font fields in `config/fonts.tex`: `\LetterPersianFont` defaults to
`Vazirmatn`; `\LetterLatinFont` defaults to `TeX Gyre Termes`. They have no
arguments and are set before the style selects fonts. Missing selected fonts
produce errors; use installed families, never silent substitutions. Use
XePersian's external `\lr{...}` for ordinary Latin in Persian prose, not
`\EN` (unavailable). Put ordinary paragraphs in `content/body.tex` and the
last paragraph in `content/final-paragraph.tex` so `\Needspace` and `samepage`
can keep it with the closing when practical. Split an exceptionally long final
paragraph manually; the entire letter is not made unbreakable. The `\Fa...`
commands in `letter-parts.tex` are **internal layout helpers**, not content API.

## English letter metadata and content
<!-- projects: letter-en -->

Defining kit sources: `templates/letter-en/common/config/metadata.tex`,
`templates/letter-en/common/config/fonts.tex`,
`templates/letter-en/common/letter-parts.tex`, and the selected
`templates/letter-en/styles/{classic,modern}/main.tex`. Their generated copies
are `config/metadata.tex`, `config/fonts.tex`, `letter-parts.tex`, and `main.tex`.
Classic uses standard `letter`; Modern uses KOMA-Script `scrlttr2`.
Both use `fontspec`, `etoolbox`, and `needspace`, with no Persian kit style.

The following are no-argument `\newcommand{\Field}{value}` values in
`config/metadata.tex`; edit their existing definitions. Example:
`\newcommand{\LetterSubjectEn}{Request for a project meeting}`.

| Field | Meaning and printed result | When not / caution |
|---|---|---|
| `\SenderNameEn`, `\SenderRoleEn` | Sender name and role in sender block/signature. | Use the actual sender only in the private project. |
| `\SenderOrganizationEn` | Optional sender organization. | Leave empty for personal correspondence. |
| `\SenderAddressEn`, `\SenderEmailEn`, `\SenderPhoneEn` | Sender contact lines; empty values are omitted. | Do not duplicate contact lines in body. |
| `\RecipientRoleEn`, `\RecipientOrgEn`, `\RecipientAddressEn` | Recipient address block. | Verify address and recipient title. |
| `\LetterDateEn`, `\LetterSubjectEn`, `\LetterGreetingEn` | Date, subject, and salutation. | Do not repeat in `body.tex`. |
| `\LetterClosingEn`, `\SignatureTitleEn` | Closing and optional signature title. | Do not repeat in final paragraph. |

`\LetterSerifFont` defaults to TeX Gyre Termes for Classic;
`\LetterSansFont` defaults to TeX Gyre Heros for Modern. Set the relevant
no-argument value in `config/fonts.tex` to an installed font if necessary.
Put prose in `content/body.tex`, the final paragraph in
`content/final-paragraph.tex`; the selected `main.tex` adds the greeting,
closing, and signature. `\English...` commands in `letter-parts.tex` are
**internal** formatting helpers. `\opening`, `\closing`, `\address`, and
`\signature` come from the selected **external document class**, not the kit.
`\EN`, `\Term`, and OS commands are unavailable.

## Article CV sections and entries
<!-- projects: resume-article -->

Defining kit source: `templates/resume-en/main.tex`, copied as the project's
`main.tex`; generated as `resume-en` by default
or with `--style article`. The document is an 11 pt `article` with `fontspec`,
`enumitem`, `needspace`, and `etoolbox`, not `moderncv`.

| Command | Meaning, signature, and result | Correct example | Do not use / alternative |
|---|---|---|---|
| `\CVSection{title}` | Required title. Uppercase colored heading and rule, with space reserved for first content. | `\CVSection{Education}` | Do not use `\section` if you need the template's visual hierarchy. |
| `\CVDatedEntry{title}{subtitle}{dates}` | Three required arguments. Bold title left, small dates right, subtitle below. | `\CVDatedEntry{B.Sc. in Computing}{Example Polytechnic}{2022--2026}` | Does not create a section; call `\CVSection` first. Long titles/dates may need editing for line fit. |
| `\CVExperience{role}{organization}{dates}{description}` | Four required arguments. Reserves space, uses a dated entry, then one bullet. Repeat for multiple positions. | `\CVExperience{Developer Intern}{Example Studio}{2025}{Built a tested import tool.}` | Not a ModernCV command; do not pack an entire CV into one argument. |
| `\CVProject{title}{description}` | Two required arguments. Bold title and inline description. | `\CVProject{Compiler Lab}{Implemented a parser in Python.}` | Use `\CVExperience` for a role and dates. |
| `\CVLine{label}{text}` | Two required arguments. Bold label followed by colon and text. | `\CVLine{Languages}{Persian, English}` | Not a section heading. |

Article CV metadata are no-argument values in `config/metadata.tex`, e.g.
`\newcommand{\CandidateName}{Sample Candidate}`. `\CandidateName` prints in
the header; `\CandidateLocation`, `\CandidatePhone`, and
`\CandidateEmail` form an optional separator-aware contact line;
`\CandidateHomepage` prints on its own line if set; `\CandidateSummary`
prints under Profile. Leave optional values empty when absent; never claim
fictitious qualifications. The font value `\CVFont` in `config/fonts.tex`
defaults to TeX Gyre Heros. It is a no-argument configuration value; an
unavailable selected font errors. The internal `\CVContactItem` manages
separators and should not be called in a section. Section files under
`sections/` are input by `main.tex`; comment an optional input there to omit
that section. Keep entries readable rather than shrinking text to one page.

## ModernCV sections and entries
<!-- projects: resume-moderncv -->

Defining kit source: `templates/resume-en-moderncv/main.tex`, copied as the
project's `main.tex`; generated with
`--template resume-en --style moderncv`. It loads the **external** `moderncv`
class (Classic visual style), `fontspec`, `needspace`, and `etoolbox`.
The kit defines only `\CVSection{title}` here: one required title, a standard
ModernCV section with five baselines of reserved space, e.g.
`\CVSection{Education}`. Do not call the Article-only `\CVDatedEntry`,
`\CVExperience`, `\CVProject`, or `\CVLine` in this variant.

Use class commands **from ModernCV**, not kit macros:

| External command | Signature, result, and example | Caution |
|---|---|---|
| `\cventry{dates}{role}{organization}{location}{grade}{description}` | Six required arguments. Dated CV row; `\cventry{2022--2026}{B.Sc.}{Example Polytechnic}{Sample City}{}{GPA 3.8/4.0}`. | Empty grade is allowed; do not assume this is an Article macro. |
| `\cvitem{label}{text}` | Two required arguments. Short labeled row; `\cvitem{Languages}{Persian, English}`. | For section heading, use `\CVSection`. |

No-argument metadata values in `config/metadata.tex` are
`\CandidateGiven`, `\CandidateFamily` (combined by `\name`),
`\CandidateCity`, `\CandidateCountry` (optional address),
`\CandidatePhone`, `\CandidateEmail`, `\CandidateHomepage` (optional class
contact commands), and `\CandidateSummary` (Profile text). Example:
`\newcommand{\CandidateGiven}{Sample}`. Edit existing definitions; do not
create a second one. Empty optional contact values do not create labels.
`\CVFont` is set in `config/fonts.tex`, defaults to TeX Gyre Heros, and must
name an installed font. `\name`, `\address`, `\phone`, `\email`, and
`\homepage` in `main.tex` are **external ModernCV** commands wired to the
metadata. The `sections/*.tex` files use ModernCV syntax; omit optional
`\input` lines in `main.tex` if a section is unused. No ATS guarantee is made.
