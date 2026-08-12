---
title: Sensitive Data Stored Unencrypted in Private Storage
id: MASWE-0001
alias: data-unencrypted-private-storage
requirement: "The app encrypts sensitive data stored in private storage."
platform: [android, ios]
profiles: [L2]
threat: MAS-THREAT-0001
attacks: [MAS-ATTACK-0005, MAS-ATTACK-0007, MAS-ATTACK-0008]
mappings:
  masvs-v1: [MSTG-STORAGE-2]
  masvs-v2: [MASVS-STORAGE-1, MASVS-STORAGE-2, MASVS-CRYPTO-2]
  cwe: [200, 284, 312, 313, 732, 922]
  android-risks:
  - file-providers
  maswe-beta: [MASWE-0006, MASWE-0002, MASWE-0118]
refs:
- https://developer.apple.com/documentation/uikit/protecting_the_user_s_privacy/encrypting_your_app_s_files
- https://developer.android.com/about/versions/nougat/android-7.0-changes#permfilesys
- https://developer.android.com/privacy-and-security/security-tips#internal-storage
---

## Overview

This weakness occurs when an app stores sensitive data unencrypted in private storage locations, such as the application sandbox, where it can be exposed via incorrect file permissions, an app or device vulnerability, or data backup mechanisms.

Sensitive data may include personally identifiable information (PII), passwords, cryptographic keys, or session tokens.

## Modes of Introduction

- **Data Stored Unencrypted**: Writing sensitive data to the app's private data directory (sandbox) unencrypted.
- **Hardcoded Encryption Key**: Encrypting sensitive data with a key that is hardcoded inside the application.
- **Encryption Key Stored on Filesystem**: Encrypting sensitive data but storing the generated key alongside it or in another easily accessible location.
- **Insufficient Encryption**: Encrypting sensitive data with an algorithm or configuration that is not considered strong.
- **Insufficient Access Restrictions**: Exposing private files to other apps through incorrect file permissions (e.g. the deprecated `MODE_WORLD_READABLE`/`MODE_WORLD_WRITEABLE` file permission modes on Android), a misconfigured `FileProvider`, or Keychain items protected with weak accessibility attributes on iOS (e.g. `kSecAttrAccessibleAlways`).
- **Data Not Removed After Use**: Retaining sensitive data in private storage (including caches, temporary files, WebView state, and network caches) longer than needed.

## Impact

- **Compromise of Sensitive Data**: Attackers can extract PII and other user data from the application sandbox, resulting in unauthorized disclosure and enabling further attacks such as identity theft.
- **Authentication or Authorization Bypass**: Attackers can extract passwords, cryptographic keys, or session tokens, resulting in account takeover or unauthorized access to protected functionality.

## Mitigations

- **Minimize Local Storage of Sensitive Data**: Avoid storing sensitive data locally if it is not required for app functionality, e.g. keep PII server-side, render it at time of use, and remove any cached data on logout.
- **Restrict File Access**: Use platform APIs to restrict file access as much as possible (least privilege principle). On Android, share data through a properly configured `ContentProvider`/ `FileProvider` with per-grant permissions instead of the deprecated `MODE_WORLD_READABLE`/`MODE_WORLD_WRITEABLE` file permission modes. On iOS, store Keychain items with the strictest viable accessibility attribute (e.g. `kSecAttrAccessibleWhenUnlockedThisDeviceOnly`).
- **Remove Data When No Longer Needed**: Clear sensitive data, caches, and temporary files as soon as they are no longer needed (e.g. on logout or when leaving a sensitive flow) to limit the window during which they can be exposed.
- **Use Platform Keystores**: Store cryptographic keys exclusively using the platform's hardware-backed keystore solution, such as the Android Keystore or the iOS Keychain.
- **Encrypt Data at Rest**: For other files and preferences, use platform-provided features for encrypting data at rest or techniques implementing envelope encryption with Data Encryption Keys (DEK) and Key Encryption Keys (KEK) or equivalent methods. For example, on Android, use [`EncryptedFile`](https://developer.android.com/reference/androidx/security/crypto/EncryptedFile) or [`EncryptedSharedPreferences`](https://developer.android.com/reference/androidx/security/crypto/EncryptedSharedPreferences); on iOS, use [iOS Data Protection](https://developer.apple.com/documentation/uikit/protecting_the_user_s_privacy/encrypting_your_app_s_files).

!!! Warning

    The **Jetpack security crypto library**, including the `EncryptedFile` and `EncryptedSharedPreferences` classes, has been [deprecated](https://developer.android.com/privacy-and-security/cryptography#jetpack_security_crypto_library). However, since an official replacement has not yet been released, we recommend using these classes until one is available.
