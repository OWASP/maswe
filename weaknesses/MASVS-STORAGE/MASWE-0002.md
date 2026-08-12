---
title: Sensitive Data Stored Unencrypted Outside of Private Storage
id: MASWE-0002
alias: data-unencrypted-shared-storage-no-user-interaction
requirement: "The app encrypts sensitive data stored outside of private storage."
platform: [android, ios]
profiles: [L1, L2]
threat: MAS-THREAT-0002
attacks: [MAS-ATTACK-0010, MAS-ATTACK-0011]
mappings:
  masvs-v1: [MSTG-STORAGE-2]
  masvs-v2: [MASVS-STORAGE-1, MASVS-STORAGE-2]
  cwe: [200, 284, 312, 313, 732, 921, 922]
  android-risks:
  - sensitive-data-external-storage
  android-core-app-quality: [Sensitive_Data_Storage]
  maswe-beta: [MASWE-0007, MASWE-0002]
refs:
- https://developer.android.com/training/data-storage
- https://developer.android.com/privacy-and-security/security-tips#external-storage
---

## Overview

This weakness occurs when an app stores sensitive data unencrypted in shared or external storage, where other apps can access it without any user interaction.

On Android, apps can store data explicitly in an app-specific external storage (`getExternalFilesDir()`), use the `MediaStore`-API  or Storage Access Framework (SAF) to access shared folders. The app-specific external storage can not be accessed by other apps. However, if the external storage is located on a physical SD card, it can be removed and read. If the external storage is emulated by the system, actors with access to an unlocked phone can access it using _Android Debug Bridge (ADB)_.

This weakness primarily concerns Android, which permits the explicit use of shared and external storage.  However, while it is not possible to directly read and write an external folder on iOS, apps can use the by default pre-installed Files app or the document picker to read and write to a system-wide shared location.

## Modes of Introduction

- **Data Stored Unencrypted**: Writing sensitive data to shared or external storage unencrypted. On Android, this also includes the app-specific external storage.
- **Hardcoded Encryption Key**: Encrypting sensitive data stored in external storage with a key that is hardcoded inside the application.
- **Encryption Key Stored on Filesystem**: Encrypting sensitive data stored in external storage but storing the key alongside it or in another easily accessible location.
- **Insufficient Encryption**: Encrypting sensitive data with an algorithm or configuration that is not considered strong.
- **Reuse of Encryption Key**: Sharing the encryption key between two devices owned by a single user, enabling data cloning between those devices via external storage.

## Impact

- **Compromise of Sensitive Data**: Attackers can extract personal information and media such as photos, documents, and audio files, resulting in unauthorized disclosure of user data.
- **Authentication or Authorization Bypass**: Attackers can extract passwords, cryptographic keys, and session tokens, resulting in identity theft or account takeover.
- **Bypass of Protection Mechanisms**: Attackers can tamper with data used by the app, e.g. a database describing the state of premium features, resulting in circumvention of business logic and revenue loss for the app owner.

## Mitigations

- **Prefer Private Storage**: Store files in the [private internal storage](https://developer.android.com/training/data-storage/app-specific#internal) whenever possible.
- **Limit Platform File Sharing**: Prohibit sensitive data to be shared using the platform's storage sharing frameworks such as Storage Access Framework (SAF) on Android or document picker on iOS whenever possible.
- **Encrypt Data Before Writing**: Encrypt any sensitive data stored in shared or external storage, e.g. using [Android's `EncryptedFile` API](https://developer.android.com/reference/androidx/security/crypto/EncryptedFile).
- **Protect Encryption Keys**: Protect any keys used for data encryption with the device's hardware-backed keystore where available, and never hardcode them inside the application.

!!! Warning

    The **Jetpack security crypto library**, including the `EncryptedFile` and `EncryptedSharedPreferences` classes, has been [deprecated](https://developer.android.com/privacy-and-security/cryptography#jetpack_security_crypto_library). However, since an official replacement has not yet been released, we recommend using these classes until one is available.
