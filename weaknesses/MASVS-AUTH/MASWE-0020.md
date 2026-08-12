---
title: Local Authentication Can Be Bypassed
id: MASWE-0020
alias: event-bound-biometric-auth
requirement: "The app implements local authentication securely."
platform: [android, ios]
profiles: [L2]
threat: MAS-THREAT-0020
attacks: [MAS-ATTACK-0002, MAS-ATTACK-0003, MAS-ATTACK-0027, MAS-ATTACK-0040]
mappings:
  masvs-v1: [MSTG-AUTH-8, MSTG-AUTH-1, MSTG-AUTH-12]
  masvs-v2: [MASVS-AUTH-2, MASVS-CRYPTO-2]
  cwe: [285, 287, 312, 319, 326, 602, 603, 863, 922]
  android-core-app-quality: [Biometric_Authentication]
  maswe-beta: [MASWE-0034, MASWE-0044, MASWE-0041, MASWE-0042, MASWE-0043]
refs:
- https://developer.android.com/training/sign-in/biometric-auth#crypto
- https://labs.withsecure.com/publications/how-secure-is-your-android-keystore-authentication
- https://developer.apple.com/documentation/localauthentication/accessing_keychain_items_with_face_id_or_touch_id
- https://github.com/sensepost/objection/issues/136#issuecomment-419664574
- https://github.com/sensepost/objection/wiki/Understanding-the-iOS-Biometrics-Bypass
- https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/applicationpassword
---

## Overview

This weakness occurs when local authentication, such as biometrics, device credentials, or a custom app PIN, can be bypassed because it is implemented as an event-bound check rather than being cryptographically tied to a protected resource.

Local authentication is only as strong as what it unlocks. When the app merely reacts to a "success" callback, an attacker who controls the app's execution can invoke the protected logic directly, without ever passing the check. To be effective, local authentication must require a cryptographic operation, such as decrypting a secret or signing a payload, using a key locked inside secure hardware like a Trusted Execution Environment or Secure Enclave. Because the hardware itself enforces user authentication before executing the operation, an attacker spoofing a successful callback cannot produce the required cryptographic proof or unencrypted data. For connected apps, authentication and authorization decisions that are enforced only locally, rather than on the server side, are similarly bypassable by tampering with the client.

## Modes of Introduction

- **Event-Bound Biometric Checks**: Acting on the biometric prompt's success result alone, without binding the protected operation to a keystore key that requires authentication (e.g. no `CryptoObject`).
- **Weak Keychain Access Control Flags**: Protecting Keychain items with flags that do not enforce the intended factor (e.g. `kSecAccessControlTouchIDAny` without additional constraints) or storing "protected" data retrievable without authentication.
- **Insecure Device-Credential Fallback**: Implementing Confirm Credentials or similar flows with long authentication validity durations or without binding them to keystore keys.
- **Local-Only Enforcement**: Enforcing authentication or authorization decisions solely in client code for apps that have a backend, instead of validating them server-side.
- **No Brute-Force Resistance**: Allowing unlimited attempts against a custom PIN or password because the app does not track failures.
- **Custom Credentials Hardcoded**: Implementing a custom app PIN or password as a plain comparison in code.

## Impact

- **Authentication or Authorization Bypass**: Attackers can trigger the protected functionality without valid biometrics or credentials, resulting in unauthorized access to the user's account and sensitive operations.
- **Compromise of Sensitive Data**: Attackers can retrieve data that was supposed to be gated by local authentication, resulting in unauthorized disclosure of sensitive user information.

## Mitigations

- **Bind Authentication to Keystore Keys**: Protect sensitive actions by requiring a cryptographic operation (such as decryption or signing) using keys stored in the platform keystore. Use mechanisms like `CryptoObject` on Android or Keychain access control on iOS (such as `.biometryCurrentSet`) so attackers cannot bypass authentication by hooking software callbacks.
- **Use Strict Access Control Flags**: Choose Keychain and keystore parameters that enforce the intended factor and invalidate on enrollment changes (see @MASWE-0022), avoiding weak flags and long authentication validity windows.
- **Enforce Authentication Server-Side**: For connected apps, gate server resources on server-verified evidence of authentication (e.g. a signed challenge produced with an authentication-bound key), never on a client-side boolean.
- **Bind Custom Credentials to the KeyChain**: For defining a custom PIN or password as an authentication factor, bind it to key material by using `applicationPassword` rather than comparing it in app code.
- **Require Explicit User Action**: For passive modalities such as face recognition, require explicit confirmation of the authentication prompt before proceeding with sensitive operations.
- **Resist Credential Guessing**: Keep each attempt dependent on hardware-backed key material so guesses cannot be parallelized off-device, and combine app-defined credentials with a biometric or device-credential constraint so every attempt also requires an OS-throttled factor.
