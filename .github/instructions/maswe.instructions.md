---
applyTo: "weaknesses/**/*.md"
---

# Writing MASWE Weakness Files

Standards for authoring weakness pages under `weaknesses/`. These pages define the mobile application security weaknesses that are enumerated by the OWASP MASWE, aligned with the OWASP MASVS, and verified by the OWASP MASTG.

Follow the shared Markdown and style rules in
`.github/instructions/markdown.instructions.md`. If a rule here conflicts with that file, this file wins for weakness content.

## Scope and purpose of a MASWE

A MASWE entry describes a single mobile application security weakness in a **platform-agnostic** way. It is the bridge between:

- the high-level MASVS control(s) it helps verify, and
- the concrete MASTG tests, demos, knowledge, best practices, and apps that demonstrate, detect, or mitigate it.

A MASWE is **not**:

- a test (that is a MASTG-TEST under `tests/`)
- a demo (that is a MASTG-DEMO under `demos/`)
- a platform-specific deep dive (that is MASTG-KNOW under `knowledge/`)
- a countermeasure recipe (that is a MASTG-BEST under `best-practices/`)

Keep the MASWE general. Platform specifics are used in the MASTG content.

## File layout and naming

- Path: `weaknesses/<MASVS-CATEGORY>/MASWE-XXXX.md`
  - Example: `weaknesses/MASVS-PLATFORM/MASWE-0064.md`
- `<MASVS-CATEGORY>` must be one of: `MASVS-STORAGE`, `MASVS-CRYPTO`, `MASVS-AUTH`, `MASVS-NETWORK`, `MASVS-PLATFORM`, `MASVS-CODE`, `MASVS-RESILIENCE`, `MASVS-PRIVACY`.
- Filename defines the weakness ID: `MASWE-\d{4}\.md`.
- Use the next available four-digit number across the whole
  `weaknesses/` tree. Coordinate in the PR to avoid ID collisions.
  Never reuse or recycle a deprecated ID.
- The `id:` field is required in the YAML front matter and must match the filename.

## YAML front matter

Every MASWE file begins with a YAML front matter block. 

Required fields:

```yaml
---
title: <Short, specific weakness name>
id: MASWE-XXXX
alias: <shortened alias of the title, in lowercase with dashes instead of spaces>
platform: [android, ios]
profiles: [L1, L2]
mappings:
  masvs-v1: [MSTG-<CATEGORY>-<N>
  masvs-v2: [MASVS-<CATEGORY>-<N>]
  cwe:[CWE-ID, CWE-ID]
  android-risks:
    - If applicable
refs:
  - <stable-url-1>
  - <stable-url-2>
status: <new | draft | placeholder>
---
```

Field rules:

- **title**: Noun phrase naming the weakness, not a sentence. No trailing period. Use title case. Avoid vendor names unless they are part of the standardized term (e.g. "Android KeyStore").
- **alias**: Short, lowercase, dash-separated version of the title. This is used for cross-referencing the weakness in MASTG content. It should be unique across all weaknesses. Examples: `weak-crypto-key-derivation`, `no-key-rotation`.
- **platform**: List of affected platforms. Use `[android, ios]` if the weakness applies to both. Use a single-item list if it is platform-specific (e.g. `[android]` for StrandHogg).
- **profiles**: MAS Testing Profiles that the weakness is relevant for. Most weaknesses apply to `L1` and `L2`. Resilience weaknesses apply to `R` and Privacy to `P`. Use the current profile values defined in <https://github.com/OWASP/mastg/blob/master/Document/0x03b-Testing-Profiles.md>
- **mappings**: Cross-references to related controls and weaknesses in other standards. At least one MASVS v2 control is required. Mappings to MASVS v1, CWE, and Android risks are optional but encouraged when applicable.
  - **mappings.masvs-v1**: One or more MSTG v1 controls that covered this topic. This helps identify content to port from MASTG v1.
  - **mappings.masvs-v2**: One or more MASVS v2 controls this weakness helps verify. At least one entry is required.
  - **cwe**: One or more CWE IDs that correspond to this weakness. This helps link to the broader software security ecosystem.
  - **android-risks**: One or more specific risks from the Android developer documentation (https://developer.android.com/privacy-and-security/risks) that correspond to this weakness. This is an optional field that can help link to Android-specific guidance, but it should only be used when there is a clear match
- **refs**: External references. Prefer stable, vendor-neutral sources (official platform docs, CWE, NIST, academic papers).
- **status**: When you generate a new MASWE draft, set
`status: new`.

Do not invent additional front matter fields. If you believe a new field is needed, open an issue first.

## Required sections for a MASWE

Use exactly these top-level section headings, in this order, all at `##` level. Do not rename them. Do not add extra top-level sections.

1. `## Overview`
2. `## Modes of Introduction`
3. `## Impact`
4. `## Mitigations`

Some existing approved MASWEs order `## Impact` before
`## Modes of Introduction`. Prefer the order above for new content, but do not re-order existing approved pages in an unrelated PR.

### `## Overview`

- 2-5 short paragraphs in plain prose.
- First paragraph: a single-sentence definition of the weakness in the form "*<Weakness> occurs when ...*". Avoid restating the title.
- Explain what the weakness is, where it appears in a mobile app, and why it matters. Stay platform-agnostic; mention Android/iOS only when the weakness is platform-specific or when the mechanism
materially differs.
- Link to relevant class names in the documentation from iOS and Android or to relevant external references, but do not include code snippets or configuration examples here. Those belong in the MASTG content.
- Do not describe testing procedures here. Do not list mitigations here.

### `## Modes of Introduction`

- How the weakness gets introduced into an app. Typical causes: unsafe defaults, missing configuration, unsafe API usage, copy-pasted code, outdated libraries, insufficient input validation, misuse of platform features.
- Prefer a short bulleted list (3-5 bullets).
- Each bullet starts with a **bold short label** followed by a colon and then the explanation. For example:
  `- **Hardcoded Keys**: Including cryptographic keys directly in the application code, making them susceptible to extraction through decompilation and reverse-engineering.`
- Each bullet describes a developer-facing cause, not a consequence.
- If the weakness can be introduced through a third-party SDK or cross-platform framework, call that out explicitly.

### `## Impact`

- What an attacker can do, or what the user loses, if the weakness is present.
- Short bulleted list (3-5 bullets). Each bullet starts with a **bold short label** followed by a colon and then the concrete outcome. For example:
  `- **Loss of Confidentiality**: Sensitive information can be exposed, resulting in a loss of confidentiality. Once keys are exposed, all data encrypted with those keys is at risk.`
- Avoid vague risk labels. Each outcome should be specific and actionable.
- No CVSS numbers. Severity is context-dependent and cannot be universally assigned to a weakness. Instead, the impact section should provide enough detail for testers and developers to make their own informed severity assessments based on the specific app context.

### `## Mitigations`

- What developers must do to prevent or reduce the impact of the weakness.
- Short bulleted list. Each bullet starts with a **bold short label** followed by a colon and then an imperative sentence addressed to the developer. For example:
  `- **Use Platform Keystores**: Where possible, generate cryptographic keys dynamically on the device, rather than using predefined keys, and ensure that they are securely stored after creation.`
- When a mitigation is fully captured by a MASTG-BEST entry, link to it with `@MASTG-BEST-XXXX` and keep the bullet short. Do not duplicate the content of the best practice.
- Do not include testing steps here.
