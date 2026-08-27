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
  - Example: `weaknesses/MASVS-PLATFORM/MASWE-0029.md`
- `<MASVS-CATEGORY>` must be one of: `MASVS-STORAGE`, `MASVS-CRYPTO`, `MASVS-AUTH`, `MASVS-NETWORK`, `MASVS-PLATFORM`, `MASVS-CODE`, `MASVS-RESILIENCE`, `MASVS-PRIVACY`.
- Filename defines the weakness ID: `MASWE-\d{4}\.md`.
- Use the next available four-digit number across the whole
  `weaknesses/` tree. Coordinate in the PR to avoid ID collisions.
  Never reuse or recycle a deprecated ID.
- The `id:` field is required in the YAML front matter and must match the filename.

## YAML front matter

Every MASWE file begins with a YAML front matter block. 

Use the following front matter structure. Omit `cves` when the weakness does not include a documented CVE case.

```yaml
---
title: <Short, specific weakness name>
id: MASWE-XXXX
cves: [CVE-YYYY-NNNN]
alias: <shortened alias of the title, in lowercase with dashes instead of spaces>
requirement: "<One-sentence positive requirement the app must fulfill>"
platform: [android, ios]
profiles: [L1, L2]
threat: MAS-THREAT-XXXX
attacks: [MAS-ATTACK-XXXX, MAS-ATTACK-YYYY]
mappings:
  masvs-v1: [MSTG-<CATEGORY>-<N>]
  masvs-v2: [MASVS-<CATEGORY>-<N>]
  cwe: [CWE-ID, CWE-ID]
  android-risks:
    - If applicable
refs:
  - <stable-url-1>
  - <stable-url-2>
status: <new | draft | placeholder>
---
```

YAML style: do not quote list items unless required (`[android, ios]`, not `["android", "ios"]`). Keep the fields in the order shown above, with `status` last.

Field rules:

- **title**: Noun phrase naming the weakness, not a sentence. No trailing period. Use title case. Avoid vendor names unless they are part of the standardized term (e.g. "Android KeyStore").
- **cves**: Optional list of CVE IDs for the documented real-world cases used in the weakness. Place it immediately after `id`, use the canonical `CVE-YYYY-NNNN` format, and list multiple IDs in ascending order.
- **alias**: Short, lowercase, dash-separated version of the title. This is used for cross-referencing the weakness in MASTG content. It should be unique across all weaknesses. Examples: `weak-crypto-key-derivation`, `no-key-rotation`.
- **requirement**: A single sentence, in quotes, stating the positive security requirement that the app must fulfill (the inverse of the weakness). Example: `"The app encrypts all network traffic."`
- **platform**: List of affected platforms. Use `[android, ios]` if the weakness applies to both. Use a single-item list if it is platform-specific (e.g. `[android]` for StrandHogg).
- **profiles**: MAS Testing Profiles that the weakness is relevant for. Most weaknesses apply to `L1` and `L2`. Resilience weaknesses apply to `R` and Privacy to `P`. Use the current profile values defined in <https://github.com/OWASP/mastg/blob/master/Document/0x03b-Testing-Profiles.md>
- **threat**: Exactly one threat ID from `.github/instructions/threats.yaml`. The threat states the immediate outcome attackers (or, for privacy weaknesses, apps and third-party components) can achieve when the weakness is present. Each MASWE references exactly one threat. If no existing threat fits, add a new one at the end of `threats.yaml` with the next free `MAS-THREAT-XXXX` ID and reference it here. Never reuse or renumber an existing ID.
- **attacks**: List of attack IDs from `.github/instructions/attacks.yaml`, describing the paths through which the threat can be realized. List them in ascending ID order, e.g. `attacks: [MAS-ATTACK-0005, MAS-ATTACK-0006]`. At least one entry is required. If no existing attack fits, add a new one at the end of `attacks.yaml` with the next free `MAS-ATTACK-XXXX` ID and reuse it, rather than inventing per-weakness wording. Never reuse or renumber an existing ID.
- **mappings**: Cross-references to related controls and weaknesses in other standards. At least one MASVS v2 control is required. Mappings to MASVS v1, CWE, and Android risks are optional but encouraged when applicable.
  - **masvs-v1**: One or more MSTG v1 controls that covered this topic. This helps identify content to port from MASTG v1.
  - **masvs-v2**: One or more MASVS v2 controls this weakness helps verify. At least one entry is required. Example: `masvs-v2: [MASVS-STORAGE-1]` which will be rendered as <https://mas.owasp.org/MASVS/controls/MASVS-STORAGE-1>
  - **maswe-beta**: One or more MASWE v0.x (pre-1.0.0-rc) weaknesses that this weakness supersedes or absorbs. This is optional but encouraged for traceability.
  - **cwe**: One or more CWE IDs that correspond to this weakness. This helps link to the broader software security ecosystem. Example: `cwe: [200]` which will be rendered as <https://cwe.mitre.org/data/definitions/200.html>
  - **android-risks**: One or more specific risks from the Android developer documentation (https://developer.android.com/privacy-and-security/risks/) that correspond to this weakness. This is an optional field that can help link to Android-specific guidance, but it should only be used when there is a clear match
  - **android-core-app-quality**: One or more checklist item IDs from the [Android Core App Quality guidelines](https://developer.android.com/docs/quality-guidelines/core-app-quality), using the current named IDs (e.g. `android-core-app-quality: [Network_Security_Traffic]` which will be rendered as <https://developer.android.com/docs/quality-guidelines/core-app-quality#Network_Security_Traffic>), not the legacy `SC-*`/`PS-*` numbering. Optional; only use when there is a clear match, and only for weaknesses whose `platform` includes `android`.
- **refs**: External references. Prefer stable, vendor-neutral sources (official platform docs, CWE, NIST, academic papers).
- **status**: When you generate a new MASWE draft, set `status: new`.

Do not invent additional front matter fields. If you believe a new field is needed, open an issue first.

## Required sections for a MASWE

Use exactly these top-level section headings, in this order, all at `##` level. Do not rename them. Do not add extra top-level sections.

1. `## Overview`
2. `## Modes of Introduction`
3. `## Example Attack Scenario`
4. `## Impact`
5. `## Mitigations`

### `## Overview`

- 2-5 short paragraphs in plain prose.
- First paragraph: a single-sentence definition of the weakness in the form "*<Weakness> occurs when ...*". Avoid restating the title.
- Explain what the weakness is, where it appears in a mobile app, and why it matters. Stay platform-agnostic; mention Android/iOS only when the weakness is platform-specific or when the mechanism
materially differs.
- Link to relevant class names in the documentation from iOS and Android or to relevant external references, but do not include code snippets or configuration examples here. Those belong in the MASTG content.
- Do not describe testing procedures here. Do not list mitigations here.

### `## Modes of Introduction`

- How the weakness gets introduced into an app. Typical causes: unsafe defaults, missing configuration, unsafe API usage, copy-pasted code, outdated libraries, insufficient input validation, misuse of platform features.
- They must reflect the testable aspects of the weakness, which is what developers introduced and can fix. Avoid describing the consequences of the weakness here.
- They must be **platform-agnostic** as much as possible. Only mention platform-specific details when it really matters to the introduction of the weakness or when the specific example is especially helpful to illustrate the weakness.
    - It is ok to mention the Android Keystore or iOS Keychain as examples of secure storage.
    - It is ok to mention Android's `SharedPreferences` or iOS's `UserDefaults` as examples of insecure storage.
    - It is not ok to mention Android's `WebView` or iOS's `WKWebView` as examples of web content containers. Mentioning WebView is sufficient.
- Use a short bulleted list where each bullet starts with a **bold short label** followed by a colon and then the explanation.

For example:

- `**Hardcoded Keys**: Including cryptographic keys directly in the application code, making them susceptible to extraction through decompilation and reverse-engineering.`
    - This should not contain the consequences (e.g. "making them susceptible to extraction through decompilation and reverse-engineering") — that belongs in the Impact section. Instead, it should describe how the weakness is introduced (e.g. "Including cryptographic keys directly in the application code").

### `## Example Attack Scenario`

- Illustrate one realistic way in which an actor could exploit the weakness in a mobile application. The scenario makes the weakness practical.
- Do not attempt to cover every possible attack path. Describe one representative scenario.
- Start with one or two sentences that identify the type of vulnerable app or component, the protected asset or operation, and the vulnerable design.
- Follow with a short numbered list, normally three to five steps, covering this cause-and-effect chain:
    1. State the actor's capability or precondition and how the attack begins.
    2. Describe the vulnerable behavior performed by the app or component.
    3. Explain how the missing security property gives the actor access or control.
    4. Name the specific data, operation, or functionality exposed to the actor.
- Ensure the scenario is consistent with at least one `attacks:` entry and the `threat:` entry in the front matter. If no existing attack or threat describes the scenario, propose a new reusable entry in `.github/instructions/attacks.yaml` or `.github/instructions/threats.yaml` by following the rules in [Writing threats and attacks](#writing-threats-and-attacks).
- State important attacker prerequisites explicitly, such as physical access, a rooted or jailbroken device, a malicious app installed on the device, access to a backup, or control over the app's execution environment. Do not imply that an application sandbox, cryptographic primitive, or platform security control is universally bypassable when exploitation depends on an additional condition.
- Prefer a platform-agnostic scenario. If the weakness or exploitation mechanism is platform-specific, use the platform named in the front matter and avoid presenting that behavior as applicable to other platforms.
- Prefer a documented real-world case that clearly demonstrates the weakness and identify it by its CVE ID when available. Do not name the affected app, vendor, or product in the scenario. Refer to it as "the vulnerable app" or "the vulnerable component" instead. Record the CVE ID in the front matter `cves:` list and add authoritative public evidence, such as a vendor advisory, CVE record, published security research report, or publicly disclosed bug bounty report, to the `refs:` list.
- Do not include affected app version numbers or version ranges in the scenario. Readers can find those details in the referenced advisory or vulnerability record.
- Frame the opening around the MASWE weakness. Explain any bugs that enable it in the numbered steps.
- Verify that the cited case actually demonstrates the MASWE weakness and supports every material claim in the scenario. Do not infer undocumented exploitation steps, attacker capabilities, or impact, and do not include details that remain confidential or were disclosed without authorization.
- If no suitable public case exists, use a realistic fictional scenario and clearly introduce it as hypothetical, for example with "Suppose a healthcare app..." Include only the details needed to explain the weakness.
- Keep the scenario concise, normally 80-150 words. Every step must advance the attack. Avoid introductory filler, sensational claims, and outcomes that are not supported by the described chain.
- Use plain, direct language. Distinguish the attacker-controlled app from the vulnerable app, and name the asset and storage location or interface precisely. Repeat "the vulnerable app" or "the attacker-controlled app" when a pronoun could refer to either one.
- Keep each numbered step focused on one part of the attack. Omit implementation details that do not help explain why the weakness is exploitable.
- Do not include commands, tool names, code, payloads, detailed testing instructions, or MASTG cross-references. Those belong in MASTG tests, techniques, and demos.
- Do not turn the scenario into mitigation guidance. Remediation belongs in `## Mitigations`.

Use this general pattern, adapting the wording to the weakness instead of copying it mechanically:

```md
## Example Attack Scenario

In <publicly documented case or CVE>, <the vulnerable app or component> exposed <asset or operation> through <the security failure represented by this MASWE>.

1. The actor <meets the prerequisite and initiates the attack>.
2. The vulnerable app or component <performs the vulnerable behavior>.
3. Because <the required security property is missing>, the actor <gains access or control>.
4. The actor <accesses specific data or functionality>.
```

The scenario must explain the weakness, not teach the reader how to perform a test.

### `## Impact`

What attackers can achieve and how they get there is **not** written in this section. It lives in the front matter.

- The immediate outcome is the `threat:` field, referencing `.github/instructions/threats.yaml`.
- The paths to that outcome are the `attacks:` field, referencing `.github/instructions/attacks.yaml`.

The `## Impact` section therefore contains **only** the consequences that follow, as a bulleted list. Do not add an opening sentence, do not repeat the threat or the attack paths, and do not add a `This can lead to:` line.

Use `.github/instructions/impact.yaml` for the canonical consequence labels. Reuse the same language and terms across MASWEs whenever a consequence is equivalent.

#### Structure

```md
- **[Canonical Impact Label]**: [Concrete attacker action or consequence], resulting in [specific harm].
```

Each consequence must.

- Use an exact label from `impact.yaml`.
- Explain what attackers can do after achieving the outcome stated by the weakness's `threat:`.
- Include a `resulting in` clause.
- Be specific to the affected user, app, service, or organization.
- Avoid unsupported, duplicate, or generic consequences.

#### Example 1

For a weakness with `threat: MAS-THREAT-0004` ("Attackers can extract hardcoded secrets, credentials, and internal information.") and `attacks: [MAS-ATTACK-0001]`:

```md
## Impact

- **Financial Loss**: Attackers can abuse compromised API keys to make unauthorized billed API calls (e.g., AI/ML services), resulting in unexpected charges to the app owner.
- **Compromise of System Integrity and Business Operations**: Attackers can use extracted credentials to access backend services, resulting in service disruption, policy-violation suspensions, or denial of service.
```

#### Example 2

For a weakness with `threat: MAS-THREAT-0016` ("Attackers can use the app's cryptographic keys without authorization.") and `attacks: [MAS-ATTACK-0002, MAS-ATTACK-0003, MAS-ATTACK-0027]`:

```md
## Impact

- **Compromise of Sensitive Data**: Attackers can decrypt protected information or forge encrypted data without ever extracting the key, resulting in unauthorized disclosure or modification of sensitive data.
- **Authentication or Authorization Bypass**: Attackers can perform signing or authentication operations reserved for the legitimate user, resulting in unauthorized transactions or access to protected functionality.
```

### Writing threats and attacks

New entries in `threats.yaml` and `attacks.yaml` are appended, never renumbered. Keep them reusable and platform-agnostic.

A threat states _what_ the actor achieves, as a full sentence ending in a period.

- Attacker-driven weaknesses: `Attackers can [obtain, expose, modify, bypass, or disrupt something].`
- Privacy weaknesses, where the app itself is the actor: `Apps and embedded third-party components can [collect, share, or track something].`

An attack states _how_ they get there, as a gerund phrase ending in a period. Each attack must.

- Name a concrete actor action or a precondition the actor needs (installing an app, accessing storage, obtaining the package, running the app in a controlled environment), never restate the outcome already given by the threat. The threat says _what_; the attack says _how_.
- Be an action someone could observe or attempt, not a property of the app. "Leveraging legacy platform behaviors applied to apps targeting outdated platform versions" describes the weakness; "Accessing app data exposed by legacy compatibility behaviors that the platform still applies to apps targeting an old version" describes the attack.
- Reuse the threat's verb only when the attack adds a distinct actor, interface, or precondition. An attack that repeats the threat's verb and its object (threat "Attackers can exploit flaws in non-standard security implementations." with attack "Exploiting flaws in custom or unproven security implementations.") is a restatement and must be rewritten or dropped.

### `## Mitigations`

- What developers must do to prevent or reduce the impact of the weakness.
- Mitigations typically correspond to the modes of introduction. Each mitigation should be actionable and specific, providing clear guidance on how to address the weakness.
- Short bulleted list. Each bullet starts with a **bold short label** followed by a colon and then an imperative sentence addressed to the developer. For example:
  `- **Use Platform Keystores**: Where possible, generate cryptographic keys dynamically on the device, rather than using predefined keys, and ensure that they are securely stored after creation.`
