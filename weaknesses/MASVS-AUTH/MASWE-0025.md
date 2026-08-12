---
title: Lack of Non-Repudiation for Critical Actions
id: MASWE-0025
alias: lack-of-non-repudiation
requirement: "The app ensures non-repudiation for critical actions."
platform: [android, ios]
profiles: [L2]
threat: MAS-THREAT-0025
attacks: [MAS-ATTACK-0036, MAS-ATTACK-0037]
mappings:
  masvs-v2: [MASVS-AUTH-3]
  cwe: [451, 778]
  maswe-beta: [MASWE-0031]
refs:
- https://developer.android.com/training/articles/security-android-protected-confirmation
- https://source.android.com/docs/security/features/protected-confirmation
---

## Overview

This weakness occurs when critical actions, such as confirming a payment or a high-value transaction, can be approved without a trusted confirmation path that produces cryptographic evidence of what the user actually saw and approved.

For a critical action to be non-repudiable, the user must be shown exactly what they are approving through a trusted, hardware-protected confirmation path, and the app should obtain cryptographic evidence that this specific prompt was confirmed by the user.

This can be achieved by displaying a prompt and then signing the confirmed message with an attested hardware-backed key.

Note that it does not provide a secure information channel, so it must not be used to display sensitive information that wouldn't ordinarily be shown on the device. Equivalent trusted-confirmation paths on other platforms need to be evaluated case by case.

!!! Warning

    On Android, [Android Protected Confirmation](https://developer.android.com/training/articles/security-android-protected-confirmation) can display the prompt and sign the confirmed message with a hardware-backed key. However, while the API itself is not deprecated, its interface definition is [deprecated](https://android.googlesource.com/platform/system/security/+/07fec0ff). It is therefore not guaranteed that Android Protected Confirmation works properly on current devices.

Beyond the technical aspect, non-repudiation has a legal dimension: a signed, user-confirmed action carries evidentiary value that a plain in-app confirmation does not, which matters when transactions are later disputed.

## Modes of Introduction

- **No Trusted Confirmation Path**: Confirming critical actions through the regular app UI, which a compromised OS or a tampered app can render differently from what is actually executed.
- **No Cryptographic Evidence of Approval**: Completing critical actions without obtaining a hardware-backed signature that binds the displayed message to the user's approval, leaving the app owner unable to prove what was approved.

## Impact

- **Financial Loss**: Attackers can trick users into approving altered payments or transactions, resulting in funds being transferred to attacker-controlled destinations.
- **Compromise of System Integrity and Business Operations**: Users can plausibly repudiate transactions when the app owner holds no cryptographic proof of what was approved, resulting in disputes, chargebacks, and legal exposure for the app owner.

## Mitigations

- **Bind Cryptographic Evidence to the Action**: Have the confirmation produce a hardware-backed signature over the exact message shown to the user, verify it server-side, and retain it as evidence of the approval.
- **Use the Strongest Available Alternative**: Where no trusted-UI mechanism exists, bind transaction approval to a user-authenticated, hardware-backed signing key (e.g. biometric-bound transaction signing) as the closest available equivalent. Verify the key attestation certificate of the signing key on the server-side.
