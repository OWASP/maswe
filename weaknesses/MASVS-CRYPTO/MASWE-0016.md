---
title: Cryptographic Key Access Not Restricted
id: MASWE-0016
alias: crypto-key-access-not-restricted
requirement: "The app restricts access to cryptographic keys."
platform: [android, ios]
profiles: [L2]
threat: MAS-THREAT-0016
attacks: [MAS-ATTACK-0002, MAS-ATTACK-0003, MAS-ATTACK-0027]
mappings:
  masvs-v2: [MASVS-CRYPTO-2, MASVS-AUTH-2, MASVS-AUTH-3]
  cwe: [284, 306]
  maswe-beta: [MASWE-0018]
refs:
- https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setUnlockedDeviceRequired(boolean)
- https://developer.apple.com/documentation/security/ksecattraccessiblewhenunlockedthisdeviceonly
- https://developer.android.com/training/sign-in/biometric-auth#prompt-the-user-to-authenticate-with-biometrics
- https://developer.apple.com/documentation/security/restricting-keychain-item-accessibility
- https://developer.android.com/privacy-and-security/keystore#StrongBoxKeyMint
- https://developer.apple.com/documentation/security/ksecattrtokenidsecureenclave
---

## Overview

This weakness occurs when cryptographic keys can be used without restrictions on who may use them, under which device conditions, and for how long.

Platform keystores allow developers to bind key usage to strict conditions, such as requiring user authentication, requiring the device to be unlocked, binding the key to the current device, or limiting the validity of an authorization to a short period or a single operation.

When these restrictions are not configured, any code running as the app, or any actor in possession of the unlocked device, can use the keys freely. This applies even to keys generated inside a hardware security module such as Android StrongBox or the iOS Secure Enclave: hardware backing protects the key material from extraction, but usage restrictions must still be configured explicitly.

## Modes of Introduction

- **No User Authentication Requirement**: Creating keys that can be used without requiring the user to authenticate (e.g. with biometrics or device credentials) for each sensitive operation.
- **Usable While the Device Is Locked**: Not restricting key or Keychain item availability to the unlocked device state (e.g. `setUnlockedDeviceRequired` on Android or `kSecAttrAccessibleWhenUnlockedThisDeviceOnly` on iOS).
- **Not Device-Bound**: Allowing key material to migrate to other devices via backups or transfers instead of using device-only protection classes.
- **Unbounded Authorization Validity**: Configuring long authentication validity durations so that a single user authentication authorizes key use indefinitely, rather than for a short window or a single operation.
- **Assuming Hardware Implies Restriction**: Generating keys inside StrongBox or the Secure Enclave without configuring access restrictions, assuming the hardware alone limits who can use the key.

## Impact

- **Compromise of Sensitive Data**: Attackers can decrypt protected information or forge encrypted data without ever extracting the key, resulting in unauthorized disclosure or modification of sensitive data.
- **Authentication or Authorization Bypass**: Attackers can perform signing or authentication operations reserved for the legitimate user, resulting in unauthorized transactions or access to protected functionality.

## Mitigations

- **Require User Authentication for Key Use**: Bind keys used for sensitive operations to user authentication, e.g. biometric or device-credential authentication on Android (`setUserAuthenticationRequired`) or Keychain access control flags on iOS, so each use requires the user's presence.
- **Restrict Keys to Unlocked Devices**: Configure keys and Keychain items so they are only available while the device is unlocked (e.g. `setUnlockedDeviceRequired(true)` on Android, `kSecAttrAccessibleWhenUnlockedThisDeviceOnly` on iOS).
- **Bind Keys to the Device**: Use device-only protection classes so key material cannot leave the device via backups or transfers.
- **Limit Authorization Validity**: Keep authentication validity durations short or require authentication per operation, so a single unlock does not authorize unlimited key use.
- **Configure Restrictions Even for Hardware-Backed Keys**: Apply the same user-authentication, unlocked-device, and validity restrictions to keys generated in StrongBox or the Secure Enclave; hardware backing protects against extraction, not against unauthorized use.
