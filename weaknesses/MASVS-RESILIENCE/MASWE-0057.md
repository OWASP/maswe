---
title: App Resources Integrity Not Verified
id: MASWE-0057
alias: app-resources-integrity
requirement: "The app verifies the integrity of its resources."
platform: [android, ios]
profiles: [R]
threat: MAS-THREAT-0057
attacks: [MAS-ATTACK-0009, MAS-ATTACK-0070]
mappings:
  masvs-v1: [MSTG-RESILIENCE-3]
  masvs-v2: [MASVS-RESILIENCE-2, MASVS-CODE-4]
  cwe: [471]
  maswe-beta: [MASWE-0105]
refs:
- https://developer.android.com/privacy-and-security/cryptography
- https://developer.android.com/privacy-and-security/keystore
- https://developer.apple.com/documentation/cryptokit/hmac
- https://developer.apple.com/documentation/cryptokit/storing-cryptokit-keys-in-the-keychain
- https://developer.apple.com/documentation/security/restricting-keychain-item-accessibility
---

## Overview

This weakness occurs when an app does not verify that the resources it relies on have not been tampered with.

Beyond the app package, apps depend on non-executable resources whose integrity matters: files in the app sandbox, configuration, downloaded content, and data restored from backups. An attacker who can alter these resources can change the app's behavior or inject malicious content without modifying its packaged code, sidestepping package- and code-integrity checks (see @MASWE-0056, @MASWE-0058). Safe dynamic code loading is covered by @MASWE-0049.

## Modes of Introduction

- **Sandbox Files Not Verified**: Trusting files in the app's data directory without verifying their integrity.
- **Downloaded Resources Not Verified**: Using downloaded content or configuration without verifying its integrity and authenticity.
- **Restored Data Not Revalidated**: Using data restored from backups or device transfers without revalidating its integrity.
- **Verification Result Ignored**: Continuing to use a resource after its integrity verification fails.

## Impact

- **Bypass of Protection Mechanisms**: Attackers can modify configuration or state files that drive security-relevant behavior, resulting in the circumvention of controls without modifying any code.
- **Execution of Unauthorized Code**: Attackers can inject malicious content into resources the app renders or interprets (e.g. scripts or templates), resulting in attacker-controlled behavior inside the app.

## Mitigations

- **Verify Resource Integrity**: Compare security-relevant files against a trusted expected hash, HMAC, or digital signature before use. Protect keys and reference values from modification, and treat local verification as a defense-in-depth control on compromised devices.
- **Authenticate Downloaded Content**: Verify integrity and authenticity (e.g. a signature, see @MASWE-0011) of downloaded resources before use.
- **Treat Restored Data as Untrusted**: Re-validate data that reappears via backup restore or device transfer before acting on it (see @MASWE-0050).
- **Respond to Failed Checks**: Discard or re-fetch tampered resources, restrict functionality, or alert the backend when validation fails.
