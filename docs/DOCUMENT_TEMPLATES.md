# Letters and CV: generated projects

Run the shared generator from the toolkit root. Use Python 3 on Windows or Ubuntu:

```sh
python scripts/new-project.py --template letter-fa --style classic --destination "../my-persian-letter"
python scripts/new-project.py --template letter-fa --style modern --destination "../my-modern-persian-letter"
python scripts/new-project.py --template letter-en --style classic --destination "../my-english-letter"
python scripts/new-project.py --template letter-en --style modern --destination "../my-modern-english-letter"
python scripts/new-project.py --template resume-en --destination "../my-cv"
python scripts/new-project.py --template resume-en --style article --destination "../my-article-cv"
python scripts/new-project.py --template resume-en --style moderncv --destination "../my-moderncv"
```

On Ubuntu, use `python3` if `python` is not available. Destinations may contain
spaces or Unicode characters and must not already exist. Standalone is the
default: each generated project is a fixed snapshot with no `.git`, network
dependency, or link back to the toolkit. `--git --repository-url URL` remains an
optional submodule workflow. The new letters and CV have no shared `tex/*.sty`
dependencies; their source is copied directly into the project.

## Letter designs

| Template/style | Document class | Default main font |
|---|---|---|
| `letter-fa --style classic` | `article` + XePersian | Vazirmatn |
| `letter-fa --style modern` | `article` + XePersian | Vazirmatn |
| `letter-en --style classic` | `letter` | TeX Gyre Termes |
| `letter-en --style modern` | `scrlttr2` | TeX Gyre Heros |

Both styles of a language copy the same `config/metadata.tex`,
`content/body.tex`, and `content/final-paragraph.tex`. Edit the metadata commands
to set sender, recipient, date, subject, greeting, and closing. Put ordinary
body paragraphs in `content/body.tex`; put the **last** paragraph in
`content/final-paragraph.tex`. The latter stays with the closing and signature
where space permits. Long letters can span pages. Do not place the full letter
in an unbreakable box.

For Persian letters, leave optional `\LetterOpeningPhraseFa`,
`\SenderOrganizationFa`, `\SenderLogoFa`, `\SenderPhoneFa`, `\SenderEmailFa`,
`\LetterNumberFa`, and `\LetterAttachmentFa` empty for a personal letter.
For an organizational letter, set only fields the sender is authorized to use.
`\SenderLogoFa` is a path to a sender-owned image in the generated project's
`assets/` directory, for example `assets/logo.png`; a nonexistent path fails
compilation. The logo keeps its aspect ratio within 13 mm height and 40% of
the text width. Never put the recipient's logo in the sender header. Empty
optional fields do not produce labels or separators.

Use `config/fonts.tex` to set installed fonts. Persian letters use
`\LetterPersianFont` (Vazirmatn) and `\LetterLatinFont` (TeX Gyre Termes).
English letters use `\LetterSerifFont` (TeX Gyre Termes) and
`\LetterSansFont` (TeX Gyre Heros), depending on style. A missing selected
font produces a LaTeX package error; font binaries are not bundled.

On Linux, each selected family must be installed **and discoverable by
XeLaTeX/fontspec by name**. Having a TeX package installed does not necessarily
make that font family available to fontspec. Check local families with
`fc-list : family | sort -u` and inspect a specific match with, for example,
`fc-match 'Vazirmatn'`. `fc-match` may show a fallback, so confirm the reported
family is the one you intended. If a default is unavailable, edit the existing
font command in the generated project's `config/fonts.tex` to name an installed
alternative; for example, change `\CVFont` to `Liberation Sans` when that
family is present. The generator does not download, install, or silently
substitute fonts.

## CV styles

Without `--style`, `resume-en` generates the Article CV. `--style article`
selects the same design explicitly. It is a minimal one-column 11 pt article
with TeX Gyre Heros and few class dependencies. `--style moderncv` generates
the separately maintained ModernCV Classic design: a restrained header, aligned
date column, and built-in CV structure. It uses TeX Gyre Heros as well and
requires the installed `moderncv` class. Neither style guarantees ATS parsing
or suitability for every employer.

For either style, edit
`config/metadata.tex` for contact details and profile; edit individual files
under `sections/` for education, experience, projects, skills, and languages.
`main.tex` also inputs research, honors, and publications. Comment out any
optional `\input{sections/...}` line to omit it. Add a custom file and input it
in the desired position for more sections. Use `\CVSection{Title}` to start a
section; it stays with the beginning of the section when possible. In Article,
repeat
`\CVExperience{role}{organization}{dates}{description}` and
`\CVProject{title}{description}` for as many entries as needed. `\CVLine{label}{text}`
and `\CVDatedEntry{title}{subtitle}{dates}` provide simple rows. In ModernCV,
repeat its native `\cventry{dates}{role}{organization}{location}{grade}{description}`
and `\cvitem{label}{text}` commands. Both styles allow an empty phone, email,
and homepage without an empty label or separator. Set `\CVFont` in
`config/fonts.tex` to another installed professional font if needed; font
selections do not belong in `config/metadata.tex`.

## Build and review

Install XeLaTeX and the required LaTeX packages. Persian letters require
XePersian and Vazirmatn; English Modern requires KOMA-Script; ModernCV requires
`moderncv`. Letter and CV pagination uses `needspace`, and optional metadata
uses `etoolbox`. No packages or fonts are installed by the generator. From each
generated project root:

```sh
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

Open the PDF and inspect page breaks, Persian punctuation and digit shaping,
sender/recipient details, glyphs, and font embedding. Font and page layout may
change when installed fonts differ. Very long final paragraphs can exceed the
space reserved for a closing; split them into shorter paragraphs and place only
the last one in `final-paragraph.tex`.
