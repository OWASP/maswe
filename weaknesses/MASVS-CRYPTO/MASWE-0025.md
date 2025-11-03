---
title: Improper Generation of Cryptographic Signatures
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

Using deprecated, risky, or broken algorithms in signatures (such as MD5 or SHA-1) could enable an attacker to commit digital signature forgery, thereby undermining integrity, authenticity, and non-repudiation.

## Impact

- **Loss of Integrity and authenticity**: Signature forgery may allow the attacker to compromise the integrity and authenticity of the data by signing the data on behalf of another entity.
- **Loss of accountability**: Signature forgery allows for plausible deniability and diminishes accountability.

## Modes of Introduction

- **Using a deprecated, risky, or broken hashing algorithm**: e.g., MD5 and SHA-1 have been identified to be vulnerable to collision attacks that are faster than a birthday attack. Because of this, they are denounced as "broken".
- **Using an insufficiently collision-resistant hash**: Choosing a hashing algorithm of insufficient length may result in loss of integrity or confidentiality.

## Mitigations

- **Choose a collision-resistant algorithm**: Choose a signature algorithm that is sufficiently collision-resistant, like RSA (3072 bits and higher), ECDSA with NIST P-384, or EdDSA with Edwards448.
- **Choose a signing scheme that makes use of algorithms with sufficient bit-lengths**: As our computers get stronger, previously generated hashes get weaker. Therefore, make sure you can adjust the bit length (strength) of the algorithm you choose. When signatures are stored at rest, make sure to follow the software industry's long-term recommendations (e.g., ["NIST: Transition to Post-Quantum Cryptography Standards"](https://csrc.nist.gov/pubs/ir/8547/ipd)).
