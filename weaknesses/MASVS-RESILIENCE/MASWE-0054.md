---
title: Device Attestation Not Implemented
id: MASWE-0054
alias: device-attestation
requirement: "The app implements device attestation."
platform: [android, ios]
profiles: [R]
threat: MAS-THREAT-0054
attacks: [MAS-ATTACK-0065, MAS-ATTACK-0066, MAS-ATTACK-0068]
mappings:
  masvs-v1: [MSTG-RESILIENCE-10]
  masvs-v2: [MASVS-RESILIENCE-1]
  maswe-beta: [MASWE-0100]
refs:
- https://developer.android.com/google/play/integrity
- https://developer.android.com/google/play/integrity/verdicts
- https://developer.android.com/google/play/integrity/standard
- https://developer.android.com/google/play/integrity/classic
- https://github.com/android/keyattestation
- https://source.android.com/docs/security/features/keystore/attestation
- https://grapheneos.org/articles/attestation-compatibility-guide
- https://developer.apple.com/documentation/devicecheck
- https://developer.apple.com/documentation/devicecheck/accessing-and-modifying-per-device-data
- https://developer.apple.com/documentation/devicecheck/establishing-your-app-s-integrity
- https://developer.apple.com/documentation/devicecheck/validating-apps-that-connect-to-your-server
- https://github.com/Oliver-Binns/app-attest
- https://github.com/VisionR1/KeyAttestation
- https://github.com/JingMatrix/TEESimulator
- https://github.com/5ec1cff/TrickyStore
---

## Overview

This weakness occurs when an app does not implement device attestation, so its backend cannot distinguish requests made from genuine, uncompromised devices from those coming from rooted, emulated, tampered, or automated environments.

Device attestation uses platform services, such as the standard Android hardware attestation API, the Play Integrity API or iOS DeviceCheck and App Attest, to provide the backend with cryptographically verifiable evidence about the device associated with a request. The evidence and security properties differ by platform and service. Without device attestation, the backend cannot independently verify device-origin claims made by the client. The backend must validate attestation evidence and apply the service-specific request-binding, freshness, and replay protections; client-side evaluation is another bypassable local check.

On Android, both the hardware-backed attestation and Play Integrity APIs can provide server-verifiable assurance that the device has not been compromised in ways covered by its device-integrity verdicts or signals, such as an unlocked bootloader, an unrecognized operating-system image or an outdated security patch level. Their main differences include:

- **Google Mobile Services (GMS) Requirement**: Direct hardware-backed key attestation uses Android Keystore and does not require Google Play services on the device to request an attestation. Play Integrity depends on Google Play components and Google services.
- **Verdict Generation and Policy Enforcement**: With direct key attestation, the backend receives signed properties and defines which boot states, operating-system signing keys, patch levels, and application identities it accepts. Play Integrity evaluates the available signals and returns Google-defined verdict labels. In both cases, the developer decides how the backend responds.

On iOS, DeviceCheck and App Attest do not provide equivalent assurance about operating-system compromise. They can establish that evidence originates from genuine Apple hardware; App Attest also binds that evidence to a legitimate app instance, but neither service attests the integrity of iOS.

## Modes of Introduction

- **No Attestation Integrated**: Not using the platform's attestation services at all, leaving the backend with no device-integrity signal.
- **Client-Side-Only Verification**: Requesting attestation but evaluating the verdict in the app instead of verifying it server-side.
- **Missing Freshness Guarantees**: Verifying attestation without a server-issued nonce or timeliness check, allowing verdicts to be replayed.
- **Verdicts Not Enforced**: Collecting attestation results but not gating sensitive operations on them.
- **Incomplete Evidence Validation**: Accepting device-attestation evidence without applying the service-specific checks for request binding, replay protection, and the device claims required by the backend's policy.

## Impact

- **Compromise of System Integrity and Business Operations**: Attackers can drive the backend with automated or tampered clients, resulting in fraud, scraping, fake accounts, and abuse of the app owner's services.
- **Bypass of Protection Mechanisms**: Attackers can leverage tampered running environments to bypass the app's security checks or feature restrictions, resulting in unauthorized access to protected app functionality.
- **Financial Loss**: Attackers can abuse promotions, premium features, or transaction flows from unattested environments, resulting in direct monetary loss to the app owner.

## Mitigations

- **Integrate Platform Attestation**: Validate the [rootOfTrust](https://source.android.com/docs/security/features/keystore/attestation#rootoftrust-fields) fields from the key attestation extension or use Play Integrity API and iOS DeviceCheck / App Attest to obtain device- and app-integrity verdicts.
- **Verify Server-Side with Freshness**: Have the backend verify attestation tokens cryptographically, bind them to a server-issued nonce, and check timeliness before trusting them.
- **Gate Sensitive Operations on Verdicts**: Require valid attestation for high-risk API calls and degrade or deny service to unattested clients.
- **Layer with Local Checks**: Combine attestation with local environment checks (see @MASWE-0051, @MASWE-0053) for defense in depth, and assess the overall scheme against known bypasses.
