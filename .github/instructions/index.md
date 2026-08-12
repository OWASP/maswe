# Writing Guide for MASWE

This section contains comprehensive guidelines for writing MASWE (Mobile Application Security Weakness Enumeration) components. These guidelines are used by contributors and AI assistants to ensure consistency, quality, and completeness of the MASWE content.

The MASWE project includes specific requirements and formatting guidelines. Use these resources to understand how to properly structure and write each type of content.

## Available Guidelines

The following writing guidelines are available.

| File | Applies to | Purpose |
| ---- | ---------- | ------- |
| [markdown.instructions.md](markdown.instructions.md) | `**/*.md` | Shared writing style, cross-references, and LLM disclosure policy |
| [maswe.instructions.md](maswe.instructions.md) | `weaknesses/**/*.md` | MASWE weakness file structure, front matter, sections, and template |

## Shared Vocabularies

MASWE files reference these controlled vocabularies instead of restating their content.

| File | Referenced from | Purpose |
| ---- | --------------- | ------- |
| [threats.yaml](threats.yaml) | `threat:` front matter | `MAS-THREAT-XXXX` outcomes attackers can achieve |
| [attacks.yaml](attacks.yaml) | `attacks:` front matter | `MAS-ATTACK-XXXX` paths through which a threat is realized |
| [impact.yaml](impact.yaml) | `## Impact` bullets | Canonical consequence labels (no IDs) |

Entries in `threats.yaml` and `attacks.yaml` are append-only. Never reuse or renumber an existing ID.

## Before You Start

Before contributing content:

1. **Read the relevant guidelines** for the type of content you're writing
2. **Review existing examples** linked in each guideline document
3. **Understand the structure** and required metadata for your content type
4. **Follow the [Style Guide](https://mas.owasp.org/contributing/5_Style_Guide/)** for general writing and formatting conventions

## Getting Help

If you have questions about writing content or need clarification on these guidelines:

- Review the [Contributing Guidelines](https://mas.owasp.org/contributing/)
- Ask in the [MASTG Discussions](https://github.com/OWASP/mastg/discussions)
- Contact the [project maintainers](https://mas.owasp.org/contact/)

## Content Quality Standards

All contributed content must meet the MAS project quality standards:

- **Accuracy**: Content must be technically correct and thoroughly tested
- **Completeness**: All required sections and metadata must be included
- **Clarity**: Writing should be clear, concise, and easy to understand
- **Relevance**: Content must be relevant to mobile application security testing
- **Maintenance**: Content should be maintainable and up-to-date with current mobile platforms

These guidelines ensure that the MASWE remains a high-quality, authoritative resource for mobile application security testing.
