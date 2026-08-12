---
title: App Attestation Not Implemented
id: MASWE-0056
alias: app-integrity
requirement: "The app implements app attestation."
platform: [android, ios]
profiles: [R]
threat: MAS-THREAT-0056
attacks: [MAS-ATTACK-0040, MAS-ATTACK-0068, MAS-ATTACK-0069]
mappings:
  masvs-v1: [MSTG-CODE-1]
  masvs-v2: [MASVS-RESILIENCE-2]
  cwe: [347]
  maswe-beta: [MASWE-0104, MASWE-0106]
refs:
- https://developer.apple.com/documentation/xcode/using-the-latest-code-signature-format
- https://developer.apple.com/documentation/devicecheck/preparing-to-use-the-app-attest-service
- https://developer.apple.com/documentation/devicecheck/validating-apps-that-connect-to-your-server
- https://source.android.com/docs/security/features/apksigning
- https://developer.android.com/google/play/integrity/verdicts
- https://developer.android.com/reference/android/content/pm/SigningInfo
- https://github.com/android/keyattestation
- https://source.android.com/docs/security/features/keystore/attestation
- https://grapheneos.org/articles/attestation-compatibility-guide
---

## Overview

This weakness occurs when an app does not provide its backend with server-verifiable attestation evidence about the app instance (e.g. app signature), or when the backend does not validate and enforce that evidence to determine whether the app has the expected identity and integrity state.

App attestation mechanisms let a backend assess whether requests come from a recognized app instance. The app collects evidence about its signing identity and integrity, protects that evidence with a cryptographic signature or platform-provided token, and sends it to the backend for verification and enforcement. This can include platform services such as Play Integrity or App Attest, and can also include app-defined integrity reports based on local signals.

On Android, an app can use hardware-backed key attestation API to provide its backend with signed evidence of the app's package name, version code, and signing-certificate digests. Together with Android's enforcement of app signatures, this evidence lets the backend verify that the app was signed with an accepted key and detect copies that have been modified and re-signed. Alternatively, the app can use the Play Integrity API, which returns a Google-generated app-recognition verdict. Play Integrity requires Google Play services to be installed and available on the device.

On iOS, an app can use the App Attest service from the DeviceCheck framework. App Attest lets the app create a hardware-based key that Apple attests as belonging to a valid app instance. The backend validates the initial attestation and then uses the attested public key to verify request-bound assertions.

The code-signature format also affects platform-enforced integrity. Using outdated formats, such as Android V1-only signatures or an iOS CodeDirectory version below 20400, weaken the platform's own integrity guarantees.

## Modes of Introduction

- **No Packaged App Integrity Verification or Attestation**: Not verifying the app's signing identity, package identity, or packaged executable files.
- **No Server-Verified App Integrity Signal**: Not providing the app's backend with an app-integrity signal.
- **Missing or Partial Server Attestation Verification or Enforcement**: Not verifying the integrity signals received at the backend or not enforcing verdicts.
- **Outdated Signing Schemes**: Signing releases with outdated formats (e.g. Android V1-only signatures, iOS CodeDirectory below version 20400) that are easier to abuse.

## Impact

- **Bypass of Protection Mechanisms**: Attackers can strip resiliency controls from a repackaged copy, making it easier to further analyze and reverse-engineer the application.
- **Compromise of Sensitive Data**: Attackers can distribute trojanized versions of the app that harvest credentials and data from the users they deceive, resulting in account compromise attributed to the app.
- **Compromise of System Integrity and Business Operations**: Modified clients, cracked features, and cloned apps circulate under the app's brand, resulting in revenue loss and reputational damage for the app owner.

## Mitigations

- **Verify Packaged App Integrity**: Check the app's signing identity, package identity, and packaged executable files against expected values.
- **Use Platform App Attestation**: Integrate services such as iOS App Attest or Play Integrity app verdicts and verify their results server-side, so the backend rejects modified or repackaged clients.
- **Use Current Signing Schemes**: Sign releases with up-to-date signature formats and rotate away from deprecated ones.
- **Respond to Failed Checks**: Terminate, restrict functionality, or flag the session to the backend when integrity verification fails, and assess the checks against known bypass techniques.
