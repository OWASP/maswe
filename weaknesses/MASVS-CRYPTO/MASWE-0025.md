---
title: Improper Generation of Digital Signatures
id: MASWE-0025
alias: improper-signature-generation
platform: [android, ios]
profiles: [L1, L2]
mappings:
  masvs-v1: [MSTG-CRYPTO-4]
  masvs-v2: [MASVS-CRYPTO-1]
  cwe: [327]

refs:
- https://developer.android.com/privacy-and-security/cryptography#deprecated-functionality
- https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-131Ar2.pdf
- https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-5.pdf
- https://csrc.nist.gov/pubs/ir/8547/ipd
status: new

---

## Overview

Using deprecated, risky, or broken hash or signature algorithms, such as MD5withRSA or SHA1withRSA, can allow attackers to forge digital signatures. In mobile apps this can enable tampering with locally verified data such as configuration files, licenses, feature flags, offline content, or cached responses while still passing signature checks, breaking authenticity, integrity, and accountability.

## Impact

- **Loss of authenticity**: Signature forgery may allow an attacker to sign data on behalf of another entity, so the app can no longer trust where the data originated.
- **Loss of integrity**: Signature forgery may allow an attacker to alter data while keeping the signature check passing, compromising its integrity.
- **Loss of accountability**: Signature forgery enables plausible deniability and weakens non repudiation when signatures are used as proof of approval or origin.

## Modes of Introduction

- **Using deprecated, risky, or broken algorithms**: For example, choosing RSA SHA1 or RSA MD5 algorithms, even when documentation marks them as deprecated.
- **Using insufficient key sizes**: For example, generating RSA keys of 1024 bits or using non standard elliptic curves below current security levels.
- **Using insufficiently collision-resistant hash functions**: Selecting MD5 or SHA1, which have known collision attacks, can allow attackers to craft different messages with the same digest.

## Mitigations

- **Choose a modern, collision-resistant algorithm with sufficient bit-lengths**: Choose a signature algorithm with at least 128 bits of security. Suitable choices include RSA with 3072 bit keys, ECDSA with NIST P256 or P384, and EdDSA with Ed25519 or Edwards448.
- **Design signatures with algorithm agility**: Adopt crypto agility-aware design as described in ["NIST.CSWP.39.2pd: Considerations for Achieving Crypto Agility"](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.39.2pd.pdf?). For example, include metadata or version fields that allow migration to stronger algorithms as recommended in documents like [NIST SP 800-131A: Transitioning the Use of Cryptographic Algorithms and Key Lengths](https://csrc.nist.gov/pubs/sp/800/131/a/r2/final) and post quantum transition guidance (["NIST IR 8547: Transition to Post-Quantum Cryptography Standards"](https://csrc.nist.gov/pubs/ir/8547/ipd)).
- **Do not rely on defaults**: Enforce minimum algorithm and key requirements **explicitly** in the code.
