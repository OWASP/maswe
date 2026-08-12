---
title: Crypto Keys Not Invalidated on New Biometric Enrollment
id: MASWE-0022
alias: crypto-keys-biometric-enrollment
requirement: "The app invalidates keys after any enrollment of new biometric data."
platform: [android, ios]
profiles: [L2]
threat: MAS-THREAT-0022
attacks: [MAS-ATTACK-0035]
mappings:
  masvs-v2: [MASVS-AUTH-2, MASVS-CRYPTO-2]
  cwe: [287, 522]
  maswe-beta: [MASWE-0046]
refs:
- https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setInvalidatedByBiometricEnrollment(boolean)
- https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/biometrycurrentset
---

## Overview

This weakness occurs when cryptographic keys gated by biometric authentication remain valid after the set of enrolled biometrics changes.

Biometric-bound keys are meant to be usable only by the person whose biometrics were enrolled when the key was created. If keys stay valid across enrollments, anyone who can add a new fingerprint or face to the device can unlock them. On Android, invalidation on new enrollment is enabled by default but can be disabled with `setInvalidatedByBiometricEnrollment(false)`; on iOS, it must be explicitly enabled by creating the access control with `SecAccessControlCreateFlags.biometryCurrentSet` (formerly `touchIDCurrentSet`), which invalidates the Keychain item when a biometric is added or removed.

## Modes of Introduction

- **Invalidation Disabled on Android**: Creating keys with `setInvalidatedByBiometricEnrollment(false)`, keeping them usable after new biometrics are enrolled.
- **Invalidation Not Enabled on iOS**: Protecting Keychain items without `biometryCurrentSet`, so items remain accessible with any enrolled biometric, including ones added later.
- **Unsafe Invalidation Recovery**: Silently re-creating an invalidated key or falling back to weaker authentication when invalidation occurs, instead of re-verifying the user's identity first.

## Impact

- **Authentication or Authorization Bypass**: Attackers can pass biometric prompts with their own newly enrolled biometrics, resulting in unauthorized approval of operations bound to the victim's identity.
- **Compromise of Sensitive Data**: Attackers can unlock data protected by biometric-bound keys, resulting in unauthorized disclosure of sensitive user information.

## Mitigations

- **Keep Enrollment Invalidation Enabled on Android**: Do not call `setInvalidatedByBiometricEnrollment(false)` for keys protecting sensitive data or operations.
- **Enable Enrollment Invalidation on iOS**: Create Keychain access controls with `SecAccessControlCreateFlags.biometryCurrentSet` so items are invalidated when the enrolled biometric set changes.
- **Handle Invalidation Safely**: When a key has been invalidated, require full re-authentication of the user (e.g. account credentials or a server-verified flow) before re-creating the key, and never silently fall back to weaker protection.
