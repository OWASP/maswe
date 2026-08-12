---
title: Code Obfuscation Not Implemented
id: MASWE-0059
alias: code-obfuscation
requirement: "The app implements code obfuscation."
platform: [android, ios]
profiles: [R]
threat: MAS-THREAT-0059
attacks: [MAS-ATTACK-0001]
mappings:
  masvs-v1: [MSTG-RESILIENCE-9, MSTG-RESILIENCE-12]
  masvs-v2: [MASVS-RESILIENCE-3]
  cwe: [693]
  maswe-beta: [MASWE-0089, MASWE-0091, MASWE-0092]
refs:
- https://developer.android.com/topic/performance/app-optimization/enable-app-optimization#overview
---

## Overview

This weakness occurs when an app's code, particularly its security-relevant logic, ships without effective obfuscation, facilitating reverse engineering and static analysis.

Obfuscation does not prevent reverse engineering, but it raises its cost. Identifier renaming or string encryption are easier to implement and are considered common obfuscation techniques. However, there are other obfuscation techniques, like control-flow transformations, opaque predicates, instruction substitution, instruction block chopping, and method inlining, as well as hindering decompilers from producing usable output. Most of these techniques can be combined together.

## Modes of Introduction

- **No Obfuscation Applied**: Shipping release builds without any minification or obfuscation, leaving class, method, and symbol names intact.
- **Security-Relevant Logic Left Readable**: Not applying enough obfuscation to security-relevant code, leaving code sections like security checks, licensing logic, and proprietary algorithms trivially analyzable.
- **Obfuscation Without Hardening**: Applying standard obfuscation whose transformations are automatically reversible by publicly available tooling.

## Impact

- **Bypass of Protection Mechanisms**: Attackers can quickly locate and defeat client-side checks such as root detection, licensing, or anti-tampering logic, resulting in the circumvention of the app's defenses.
- **Compromise of Sensitive Data**: Attackers can recover proprietary algorithms and embedded secrets from readable code, resulting in intellectual property theft and easier planning of further attacks.

## Mitigations

- **Enable Obfuscation for Release Builds**: Apply the platform's minification and obfuscation tooling or established commercial obfuscators to all release builds.
- **Harden Security-Relevant Code**: Apply stronger transformations (opaque predicates, instruction substitution, control-flow obfuscation, method inlining) to the security-relevant code.
- **Implement Lossy Obfuscation**: Implement obfuscation in a way that intentionally removes information from the code, rather than only shift things around.
- **Assess Obfuscation Effectiveness**: Regularly attempt to reverse engineer the release build with state-of-the-art decompilers and deobfuscators to validate that the protection meets its goal.
- **Combine with Runtime Protections**: Pair obfuscation with runtime integrity and anti-instrumentation checks (see the mitigations in @MASWE-0055, @MASWE-0065, @MASWE-0058), since obfuscation alone only delays attackers.
