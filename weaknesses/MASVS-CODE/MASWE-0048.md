---
title: Malicious Code Included in the App
id: MASWE-0048
alias: malicious-code-included
requirement: "The app package does not contain malicious code."
platform: [android, ios]
profiles: [L1, L2]
threat: MAS-THREAT-0048
attacks: [MAS-ATTACK-0060, MAS-ATTACK-0061]
mappings:
  masvs-v2: [MASVS-CODE-3]
  cwe: [506, 507, 511]
refs:
- insecure-library
- https://support.google.com/googleplay/android-developer/answer/13326895
- https://developer.apple.com/support/third-party-SDK-requirements/
---

## Overview

This weakness occurs when an app ships with malicious code, introduced either intentionally by an insider or unintentionally through a compromised dependency, SDK, build tool, or other supply-chain attack.

Malicious code can exfiltrate data, execute hidden or backdoored functionality, display unwanted content, or perform actions against the user's interest. Because the developer is responsible for all code shipped in the app, including third-party SDKs, the codebase must be reviewed and the supply chain examined to detect and prevent the inclusion of malicious code. This complements @MASWE-0044, which covers dependencies with known vulnerabilities, and @MASWE-0075, which covers the inability to verify what was actually built.

## Modes of Introduction

- **Malicious Developer**: Malicious code committed intentionally by someone with access to the codebase or through a compromised developer account.
- **Compromised Dependencies**: Malicious or trojanized third-party SDKs and libraries pulled into the app, including through typosquatting or hijacked packages.
- **Compromised Build Pipeline**: Build tools, plugins, or CI/CD infrastructure that inject code into the app during compilation or packaging.
- **Hidden Functionality**: Backdoors, hidden switches, or undisclosed capabilities shipped in the app or its components.

## Impact

- **Compromise of Sensitive Data**: Attackers can exfiltrate user data and credentials from inside the app's trust boundary, resulting in large-scale disclosure across the entire user base.
- **Execution of Unauthorized Code**: Attackers can trigger backdoored or hidden functionality at will, resulting in attacker-controlled behavior running with the app's identity and permissions.
- **Compromise of System Integrity and Business Operations**: The app owner distributes malware to their own users, resulting in app-store removal, incident response costs, and severe reputational damage.

## Mitigations

- **Review Code and Changes**: Enforce code review for all changes, restrict and monitor access to the codebase, and require strong authentication for developer accounts.
- **Examine the Supply Chain**: Pin dependency versions, verify package integrity and provenance, source components only from reputable publishers, and monitor them with Software Composition Analysis (see @MASWE-0044).
- **Protect the Build Pipeline**: Harden and monitor CI/CD infrastructure, restrict who and what can alter build configurations, and generate build provenance attestations (see @MASWE-0075).
- **Analyze the Shipped Artifact**: Scan and behaviorally analyze release builds to detect unexpected code, permissions, or network endpoints before distribution.
