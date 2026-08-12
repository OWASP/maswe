---
title: Cryptographic Key Rotation Not Implemented
id: MASWE-0015
alias: no-key-rotation
requirement: "The app rotates cryptographic keys regularly."
platform: [android, ios]
profiles: [L2]
threat: MAS-THREAT-0015
attacks: [MAS-ATTACK-0001, MAS-ATTACK-0005]
mappings:
  masvs-v2: [MASVS-CRYPTO-2]
  cwe: [324]
  maswe-beta: [MASWE-0011]
refs:
- https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf
- https://developers.google.com/tink/managing-key-rotation
---

## Overview

This weakness occurs when an app uses cryptographic keys beyond their intended cryptoperiod without rotating them, so that a single key protects an ever-growing amount of data over an unbounded lifetime.

Cryptographic keys have a limited cryptoperiod, as defined in [NIST.SP.800-57pt1r5](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf), after which they should be retired and replaced. Key rotation limits the amount of data protected by any single key and bounds the impact of a key compromise. This is especially important for long-lived symmetric keys and asymmetric key pairs. Rotation must be implemented so that data protected under old keys can still be decrypted or verified, for example via keysets with versioned keys, while new operations use the current key.

## Modes of Introduction

- **No Rotation Mechanism**: Designing storage formats or protocols around a single static key, with no key versioning or keyset support that would allow the key to be replaced.
- **Unbounded Cryptoperiods**: Using keys indefinitely without defining a cryptoperiod or expiry after which they must be retired and replaced.
- **Superseded Keys Not Retired**: Keeping old keys active and usable for new operations after rotation, instead of restricting them to decryption or verification of existing data and eventually destroying them.

## Impact

- **Compromise of Sensitive Data**: Attackers can decrypt the entire history of data protected with the compromised key, resulting in a much larger disclosure than a rotation-bounded compromise would allow.
- **Authentication or Authorization Bypass**: Attackers can keep forging valid cryptographic values indefinitely with a long-lived compromised key, resulting in persistent unauthorized access that is not curtailed by key expiry.

## Mitigations

- **Define Cryptoperiods**: Assign each key a cryptoperiod appropriate to its type and usage as outlined in [NIST.SP.800-57pt1r5](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf), and replace keys when it elapses or upon suspicion of compromise.
- **Use Versioned Keysets**: Structure key material as a keyset with key versions (e.g. as implemented by [Tink key rotation](https://developers.google.com/tink/managing-key-rotation)), so that new data is protected with the current key while older data remains readable during migration.
- **Re-Encrypt and Retire Old Keys**: After rotating, re-encrypt or re-protect existing data under the new key where feasible, restrict superseded keys to decryption or verification only, and securely destroy them once they are no longer needed.
