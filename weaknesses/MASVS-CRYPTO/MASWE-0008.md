---
title: Improper Hashing
id: MASWE-0008
alias: improper-hashing
requirement: "The app properly hashes sensitive data."
platform: [android, ios]
profiles: [L1, L2]
threat: MAS-THREAT-0008
attacks: [MAS-ATTACK-0028]
mappings:
  masvs-v1: [MSTG-CRYPTO-4]
  masvs-v2: [MASVS-CRYPTO-1]
  cwe: [328]
  android-core-app-quality: [Cryptographic_Algorithms]
  maswe-beta: [MASWE-0021]
refs:
- https://developer.android.com/privacy-and-security/cryptography#deprecated-functionality
- https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-131Ar2.pdf
- https://en.wikipedia.org/wiki/Collision_attack
- https://csrc.nist.gov/pubs/ir/8547/ipd
---

## Overview

This weakness occurs when a broken or unsuitable hash function is used in a security-sensitive context, such as integrity checks, digital signatures, or certificate fingerprints.

Broken algorithms such as MD5 and SHA-1 have practical collision attacks, and NIST has deprecated both for all security purposes; they must not be used in any security-sensitive context. Using an otherwise sound hash function for the wrong job is equally problematic: passwords and passphrases require a dedicated password-based key derivation function rather than a plain hash (see @MASWE-0014), and non-cryptographic checksums provide no security at all.

## Modes of Introduction

- **Broken Hash Algorithms**: Using algorithms such as MD5 or SHA-1 in contexts that require collision or second-preimage resistance, e.g. digital signatures, integrity verification, or fingerprinting.
- **Wrong Hash for the Job**: Using a plain, fast hash for password storage or key derivation instead of a password-based KDF (see @MASWE-0014), or using non-cryptographic checksums such as CRC-32 where a cryptographic hash is required.
- **Truncated Digests**: Truncating hash output below the security strength required by the use case, reducing collision and preimage resistance.

## Impact

- **Compromise of Sensitive Data**: Attackers can substitute or modify data without invalidating its hash, resulting in undetected manipulation of sensitive information.
- **Authentication or Authorization Bypass**: Attackers can forge artifacts whose authenticity is established via hashes, such as signed payloads or fingerprinted certificates, resulting in impersonation or unauthorized access.

## Mitigations

- **Use Approved Hash Functions**: Use hash functions approved by current standards, such as SHA-256 or stronger members of the SHA-2 and SHA-3 families, per [NIST.SP.800-131Ar2](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-131Ar2.pdf), and follow emerging post-quantum guidance such as [NIST IR 8547](https://csrc.nist.gov/pubs/ir/8547/ipd).
- **Use Password-Based KDFs for Passwords**: Never hash passwords or passphrases directly; use a dedicated password-based KDF as described in @MASWE-0014.
- **Preserve Digest Length**: Do not truncate digests below the security strength required by the use case.
