# Extending the kit without inventing an API

Use this workflow when a requested capability is absent from the **actual
project snapshot**. A chat-only assistant can propose code, but cannot assume
it edited the repository or that the new command exists in the user's project.

1. **Search first.** Read the project's `AI_MACROS.md`, `main.tex`, copied
   styles, template-local source, and documented package dependencies. Confirm
   the desired command's exact definition and scope. The newest online docs
   may describe a later version than an uploaded standalone snapshot.
2. **Classify the need.** A one-off formatting requirement may use standard
   LaTeX or an existing supported package in that document. A broadly useful
   pattern may justify a new library command. Template-specific layout should
   remain local when it does not belong in every project.
3. **Propose the contract.** State the user-facing purpose, exact name and
   arguments, canonical source file and project scope, dependencies, expected
   output, alternatives, RTL/LTR and typography concerns, and compatibility
   impact. Ask the owner before significant public API or architecture changes.
4. **Implement in the right source after approval.** Shared assignment text
   components belong in `tex/persian-kit.sty`; lab extensions in
   `tex/persian-lab.sty`; the isolated historical OS layout in
   `tex/persian-os.sty`; letter/CV-specific commands in their source template.
   Do not make a generated project's `vendor/` copy the only implementation
   of a reusable feature. Do not silently break existing commands or change
   the OS design to imitate assignment layout.
5. **Teach and verify.** Add an exact entry and realistic example in
   `docs/MACRO_REFERENCE.md`, update a relevant snippet or `gallery.tex` when
   useful, add a focused regression/compilation check, update `CHANGELOG.md`,
   and make sure project-local AI onboarding will include the new API. A new
   command is not complete until a fresh assistant can identify when to use
   it and when not to use it.

**Example: a plot from numerical tabular data directly in LaTeX.** This kit
currently has figure and table helpers but no data-to-plot macro. First check
whether PGFPlots/PGFPlotstable (external packages) meet the document need.
For one assignment, a local package-based plot may suffice. A reusable wrapper
would require a separate contract covering input format, axes, labels, LTR
numbers within Persian text, dependencies, and compatibility, then owner
review before becoming a kit macro. This guide does not add plotting support.

For chat-only work, return the requested current-file solution separately
from an optional extension proposal or patch. Do not tell the user to call a
proposed macro until it is implemented in their project snapshot.
