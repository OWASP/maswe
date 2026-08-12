---
title: Cryptographic Keys Stored Outside of Platform Keystore
id: MASWE-0003
alias: crypto-keys-not-protected-at-rest
requirement: "The app stores cryptographic keys inside the platform-provided secure keystore."
platform: [android, ios]
profiles: [L1, L2]
threat: MAS-THREAT-0003
attacks: [MAS-ATTACK-0001, MAS-ATTACK-0005, MAS-ATTACK-0008]
mappings:
  masvs-v1: [MSTG-STORAGE-1, MSTG-CRYPTO-1]
  masvs-v2: [MASVS-STORAGE-1, MASVS-CRYPTO-2]
  cwe: [312, 318, 321]
  android-risks:
  - hardcoded-cryptographic-secrets
  maswe-beta: [MASWE-0013, MASWE-0014, MASWE-0016]
refs:
- https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf
- https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-175Br1.pdf
- https://developer.android.com/privacy-and-security/keystore#ImportingEncryptedKeys
- https://developer.apple.com/documentation/security/certificate_key_and_trust_services/keys/storing_keys_as_data
- https://developer.android.com/privacy-and-security/keystore#StrongBoxKeyMint
---

## Overview

This weakness occurs when cryptographic keys are stored outside the platform-provided secure keystore, in locations such as unencrypted preferences, unprotected files, or the application code itself.

Cryptographic keys are essential for securing sensitive data in mobile applications. Keys that are hardcoded in the app, included in source control and shipped in the final package, or written to insecure storage locations lack the access control and hardware-backed protection that platform keystores, such as the [Android Keystore](https://developer.android.com/training/articles/keystore) and the [iOS Keychain](https://developer.apple.com/documentation/security/keychain_services), are designed to provide.

## Modes of Introduction

- **Insecure Storage Locations**: Storing cryptographic keys in locations that are not designed for secure storage, such as regular configuration or user preferences files, application data directories, or other areas lacking encryption and access control mechanisms.
- **Hardcoded Cryptographic Keys**: Including cryptographic keys directly in the application code or in resources shipped with the app package.
- **Insecure Key Import**: Importing keys into the keystore in plaintext instead of using secure wrapped or encrypted import, exposing the key material outside the secure environment.

## Impact

- **Compromise of Sensitive Data**: Attackers can decrypt protected information or forge encrypted data, resulting in unauthorized disclosure or modification of sensitive data.
- **Authentication or Authorization Bypass**: Attackers can create valid cryptographic values or impersonate trusted parties, resulting in unauthorized access to protected accounts, data, or functionality.
- **Bypass of Protection Mechanisms**: Attackers can forge licensing, entitlement, or integrity tokens signed with a compromised key to unlock restricted features or defeat client-side checks, resulting in circumvention of the protections the app enforces.
- **Financial Loss**: Attackers can abuse a compromised key that authenticates to a paid or metered backend service to run up usage on the owner's account, resulting in unexpected charges to the app owner.

## Mitigations

- **Use Platform Keystores**: Where possible, generate cryptographic keys dynamically on the device, rather than using predefined keys, and ensure that they are securely stored after creation. For this you can use the platform-specific keystores, such as the [Android Keystore](https://developer.android.com/training/articles/keystore) or the [iOS Keychain](https://developer.apple.com/documentation/security/keychain_services).
- **Implement Strongest Hardware Security Solutions**: For the most critical cases and whenever [available and compatible](https://developer.android.com/privacy-and-security/keystore#HardwareSecurityModule) for the use case at hand, leverage the strongest hardware-backed security options such as [Android StrongBox](https://developer.android.com/privacy-and-security/keystore#StrongBoxKeyMint) or iOS's Secure Enclave [`kSecAttrTokenIDSecureEnclave`](https://developer.apple.com/documentation/security/ksecattrtokenidsecureenclave) option to ensure the highest protection including physical and side-channel attacks.
- **Use Cryptographic Key Management Systems**: Securely retrieve keys from server-side services that provide secure storage, access control, and auditing for sensitive data. For example, AWS Secrets Manager, Azure Key Vault, or Google Cloud Secret Manager are some popular managed secrets storage solutions. The app can securely retrieve the necessary secrets at runtime through secure, authenticated API calls.
- **Encrypt and Wrap Keys**: Whenever storing keys in platform keystores is not suitable for the use case or keys need to be exported, use envelope encryption (DEK+KEK) and key wrapping techniques as specified in [NIST.SP.800-175Br1 5.3.5](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-175Br1.pdf) to protect cryptographic keys before storing them.
- **Follow Standard Key Management Best Practices**: Implement proper key management practices, including key rotation and robust protection mechanisms for keys in storage as outlined in [NIST.SP.800-57pt1r5 6.2.2](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf), ensuring availability, integrity, confidentiality, and proper association with usage, entities, and related information.
