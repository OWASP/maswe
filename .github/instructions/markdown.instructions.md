---
applyTo: "**/*.md"
---

# Markdown and Style Rules

This project follows the same Markdown and style conventions as the OWASP MASTG. The canonical rules are defined in the MASTG instruction
file:

<https://github.com/OWASP/mastg/blob/master/.github/instructions/markdown.instructions.md>

Read and apply that file in full. The sections below define only the rules that are **specific to MASWE** or that **override** the MASTG defaults.

## Content restrictions

MASWE weakness files contain plain text only. Do not include:

- **Images or screenshots.** Visual content belongs in the MASTG, not in weakness descriptions.
- **Code blocks.** Code samples, configuration snippets, and command examples belong in MASTG tests, demos, and best practices. Use inline backticks for identifiers (e.g. `SharedPreferences`, `NSUserDefaults`) but never fenced code blocks.
- **Cross-references to MASTG or MASVS in the body text.** Mappings to MASVS controls and links to MASTG content are defined in the YAML front matter. Do not duplicate them inline in the prose.
