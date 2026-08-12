---
title: Improper Cryptographic Key Generation
id: MASWE-0013
alias: improper-crypto-key-generation
requirement: "The app securely generates cryptographic keys."
platform: [android, ios]
profiles: [L1, L2]
threat: MAS-THREAT-0013
attacks: [MAS-ATTACK-0018, MAS-ATTACK-0019, MAS-ATTACK-0020]
mappings:
  masvs-v1: [MSTG-CRYPTO-2]
  masvs-v2: [MASVS-CRYPTO-2]
  cwe: [331, 326, 337, 338, 522]
  android-risks:
  - weak-prng
  android-core-app-quality: [Cryptographic_Algorithms]
  maswe-beta: [MASWE-0009, MASWE-0017]
refs:
- https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf
- https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-131Ar2.pdf
- https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-175Br1.pdf
- https://developer.android.com/privacy-and-security/cryptography
- https://developer.android.com/reference/javax/crypto/KeyGenerator
- https://developer.android.com/reference/kotlin/android/security/keystore/KeyProtection
- https://developer.apple.com/documentation/cryptokit/aes/keywrap
---

## Overview

This weakness occurs when cryptographic keys are generated with insufficient length, insufficient entropy, or otherwise flawed generation processes, weakening every protection built on top of them.

In cryptography, security strength is heavily influenced by how keys are generated. One critical aspect is the key size (key length), measured in bits, which must comply with current security best practices: algorithms used with insufficient key sizes are vulnerable to attack. Even with a sufficiently large key size, security can be compromised if the generation process is flawed. Failing to use strong, cryptographically secure pseudorandom number generators (CSPRNGs) with sufficient entropy can produce predictable keys that are easier for attackers to guess or reproduce.

Mobile platforms provide additional layers of protection for key material, such as generating and storing keys in secure hardware or key attestation. Failing to use these mechanisms where required results in weak key protection.

## Modes of Introduction

- **Insufficient Entropy**: Generating keys from a source of randomness with insufficient entropy or from predictable seeds.
- **Insufficient Key Length**: Generating keys shorter than the lengths recommended by current standards for the chosen algorithm.
- **Risky or Broken Algorithms**: Generating keys using deprecated, risky, or inherently broken cryptographic algorithms, which often only support weak key lengths.
- **Insecure Key Export**: Exporting a key in plaintext when it must leave the secure environment in which it was created (for example, to be backed up or shared with another device), instead of "wrapping" it (encrypting it with another key) as specified in [NIST.SP.800-175Br1 5.3.5](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-175Br1.pdf), even when the key is sent over a secure channel.
- **Insecure Key Properties**: Generating keys with properties such as an unspecified or overly broad purpose, insecure storage location (e.g. not using secure hardware if available) or access requirements (see @MASWE-0016).

## Impact

- **Compromise of Sensitive Data**: Attackers can decrypt protected information or forge encrypted data, resulting in unauthorized disclosure or modification of sensitive data.
- **Authentication or Authorization Bypass**: Attackers can create valid cryptographic values or impersonate trusted parties, resulting in unauthorized access to protected accounts, data, or functionality.

## Mitigations

- **Use Established Cryptographic Libraries**: Always use modern, well-established cryptographic libraries and APIs that follow best practices for entropy generation and key management.
- **Wrap Keys Before Export**: When keys must be exported, protect them with key wrapping (e.g. AES Key Wrap or an equivalent authenticated scheme) so they are never exposed in plaintext outside a secure environment.
- **Use Sufficient Key Lengths**: Ensure that key lengths meet or exceed current standards for cryptographic security, such as 256-bit for AES encryption and 2048-bit for RSA (considering quantum computing attacks). See ["NIST Special Publication 800-57: Recommendation for Key Management: Part 1 – General"](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf), ["NIST Special Publication 800-131A: Transitioning the Use of Cryptographic Algorithms and Key Lengths"](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-131Ar2.pdf), and ["BlueKrypt's Cryptographic Key Length Recommendation"](https://www.keylength.com/) for more information on cryptographic key sizes.
- **Key Attestation**: Use platform key attestation to obtain cryptographic proof that a key was generated and is stored inside secure hardware (e.g. a hardware-backed keystore, TEE, or Secure Element) with the expected properties.
