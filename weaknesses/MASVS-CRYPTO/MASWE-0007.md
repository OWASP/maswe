---
title: Improper Encryption
id: MASWE-0007
alias: improper-encryption
requirement: "The app properly encrypts sensitive data."
platform: [android, ios]
profiles: [L1, L2]
threat: MAS-THREAT-0007
attacks: [MAS-ATTACK-0018, MAS-ATTACK-0021, MAS-ATTACK-0022, MAS-ATTACK-0023]
mappings:
  masvs-v1: [MSTG-CRYPTO-4, MSTG-CRYPTO-5]
  masvs-v2: [MASVS-CRYPTO-1, MASVS-CRYPTO-2]
  cwe: [208, 323, 325, 326, 327, 329, 780]
  android-risks:
  - broken-cryptographic-algorithm
  android-core-app-quality: [Cryptographic_Algorithms]
  maswe-beta: [MASWE-0020, MASWE-0012, MASWE-0022, MASWE-0023]
refs:
- https://support.google.com/faqs/answer/10046138?hl=en
- https://support.google.com/faqs/answer/9450925?hl=en
- https://developer.android.com/privacy-and-security/cryptography#deprecated-functionality
- https://developer.android.com/privacy-and-security/cryptography#pbe-without-iv
- https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-131Ar2.pdf
- https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-56Br2.pdf
- https://www.usenix.org/legacy/event/woot10/tech/full_papers/Rizzo.pdf
---

## Overview

This weakness occurs when encryption is implemented with broken algorithms, insecure modes or parameters, or non-cryptographic techniques, leaving the protected data recoverable or forgeable without the key.

Encryption is only as strong as its weakest component: the algorithm, the mode of operation, the padding scheme, the initialization vectors (IVs) or nonces, and the way keys are used all contribute to the actual security of the ciphertext.

## Modes of Introduction

- **Broken Algorithms**: Relying on broken encryption algorithms (i.e., that are deprecated or disallowed by NIST or other standards) such as RC4, DES, or 3DES.
- **Predictable or Reused Initialization Vectors (IVs)**: Using IVs that are hardcoded, null, predictable, or reused in modes like AES-CBC or AES-CTR, or reusing nonces or using authentication tags of insufficient length in AEAD modes like AES-GCM.
- **Risky Padding**: Using a padding scheme susceptible to padding oracle attacks (e.g. PKCS#7 with unauthenticated AES-CBC, or PKCS#1 v1.5 for RSA) in combination with observable padding-error signals.
- **Broken Modes of Operation**: Using modes that are considered broken. For example, NIST disallows AES-ECB because it is deterministic, meaning identical plaintext blocks yield identical ciphertext blocks, which leaks data patterns.
- **Insufficient Key Length**: Using key sizes below current recommendations for the chosen algorithm.
- **Insecure or Wrong Key Usage**: Reusing a single key for multiple purposes (e.g. encryption and signing) or with an unauthorized algorithm, violating key-separation principles. Per [NIST.SP.800-57pt1r5](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf), a single key should be used for only one purpose.
- **Non-Cryptographic Operations**: Relying on techniques such as XOR, Base64 encoding, or simple obfuscation methods for security purposes. These methods provide no actual encryption.

## Impact

- **Compromise of Sensitive Data**: Attackers can decipher protected information or alter it without detection, resulting in unauthorized disclosure or manipulation of sensitive data.
- **Authentication or Authorization Bypass**: Attackers can forge ciphertexts, tokens, or signatures accepted by the app or its backend, resulting in unauthorized access to protected accounts, data, or functionality.

## Mitigations

- **Use Secure Encryption Modes**: Choose secure, authenticated modes (e.g. approved by NIST) such as `AES/GCM/NoPadding`. If AES-CBC must be used, apply Encrypt-then-MAC (e.g. append HMAC) and, for RSA, prefer OAEP over PKCS#1 v1.5.
- **Ensure Proper Initialization Vector Management**: Generate IVs using cryptographically secure random number generators (with sufficient entropy) and ensure they are unique for every operation; never hardcode, null, or reuse them. On Android, use `GCMParameterSpec` (not the legacy `IvParameterSpec`) for GCM.
- **Use Sufficiently Long Keys**: Enforce sufficiently long keys such as those approved by NIST, e.g., a minimum of 128 bits for AES.
- **Use Each Key for a Single Purpose**: Derive or generate separate keys for encryption, authentication, and signing, and only use each key with its authorized algorithm.
- **Do Not Expose Cryptographic Errors**: Avoid leaking detailed padding or decryption error messages or timing differences that could serve as an oracle.
- **Rely on Proper Cryptographic Primitives**: Rely on well-vetted cryptographic primitives that have undergone rigorous peer review and formal validation. See @MASWE-0011 for signature verification.
