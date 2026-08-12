---
title: Improper Generation of Cryptographic Signatures
id: MASWE-0010
alias: improper-signature-generation
requirement: "The app properly generates cryptographic signatures."
platform: [android, ios]
profiles: [L1, L2]
threat: MAS-THREAT-0010
attacks: [MAS-ATTACK-0018, MAS-ATTACK-0021, MAS-ATTACK-0030]
mappings:
  masvs-v1: [MSTG-CRYPTO-4, MSTG-CRYPTO-5]
  masvs-v2: [MASVS-CRYPTO-1, MASVS-CRYPTO-2]
  cwe: [323, 326, 327, 330]
  maswe-beta: [MASWE-0025, MASWE-0012]
refs:
- https://developer.android.com/privacy-and-security/cryptography#deprecated-functionality
- https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-131Ar2.pdf
- https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-5.pdf
- https://csrc.nist.gov/pubs/ir/8547/ipd
---

## Overview

This weakness occurs when cryptographic signatures are generated with weak algorithms, insufficient parameters, or flawed randomness, undermining the integrity and authenticity guarantees they are meant to provide.

Signatures are only as strong as the scheme and parameters behind them: deprecated combinations such as SHA1withRSA, keys that are too short, and signing keys reused for other purposes all weaken the guarantee. In addition, the randomness used during signing is critical: in (EC)DSA, a predictable or reused per-signature nonce allows the private key itself to be recovered from observed signatures.

## Modes of Introduction

- **Weak or Deprecated Signature Algorithms**: Generating signatures with deprecated schemes or digest combinations, such as SHA1withRSA.
- **Insufficient Key Length**: Using signing keys shorter than the lengths recommended by current standards for the chosen algorithm.
- **Predictable Signature Nonces**: Generating the per-signature nonce in (EC)DSA with insufficient entropy, or reusing it across signatures.
- **Key Reuse Across Purposes**: Using a signing key for other purposes, such as encryption or key agreement, violating key-separation principles.

## Impact

- **Authentication or Authorization Bypass**: Attackers can sign arbitrary data as the app or user, resulting in impersonation and unauthorized transactions or API calls accepted by peers that trust the signature.
- **Compromise of Sensitive Data**: Attackers can tamper with signed data while producing valid signatures for it, resulting in undetected manipulation of information whose integrity depends on the signature.

## Mitigations

- **Use Approved Signature Schemes**: Generate signatures with schemes approved in [NIST FIPS 186-5](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-5.pdf), such as ECDSA, RSA-PSS, or EdDSA, with approved digests, and follow post-quantum migration guidance such as [NIST IR 8547](https://csrc.nist.gov/pubs/ir/8547/ipd).
- **Use Sufficient Key Lengths**: Ensure signing keys meet or exceed the lengths recommended by [NIST.SP.800-131Ar2](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-131Ar2.pdf) for the chosen algorithm.
- **Ensure Nonce Uniqueness**: Generate (EC)DSA per-signature nonces with a cryptographically secure random number generator, or use deterministic schemes (e.g. RFC 6979 deterministic ECDSA or Ed25519) that eliminate nonce misuse.
- **Use Signing Keys for a Single Purpose**: Keep signing keys dedicated to signing and generate separate keys for other operations.
