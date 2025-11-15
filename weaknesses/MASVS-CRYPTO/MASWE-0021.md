---
title: Improper Hashing
id: MASWE-0021
alias: improper-hashing
platform: [android, ios]
profiles: [L1, L2]
mappings:
  masvs-v1: [MSTG-CRYPTO-4]
  masvs-v2: [MASVS-CRYPTO-1]
  cwe: [328]

refs:
- https://developer.android.com/privacy-and-security/cryptography#deprecated-functionality
- https://cwe.mitre.org/data/definitions/328.html
- https://en.wikipedia.org/wiki/Collision_attack
- https://csrc.nist.gov/pubs/sp/800/131/a/r2/final
- https://csrc.nist.gov/pubs/sp/800/185/final
- https://csrc.nist.gov/pubs/fips/202/final
- https://csrc.nist.gov/pubs/fips/180-4/upd1/final
- https://csrc.nist.gov/pubs/ir/8547/ipd
status: new

---

## Overview

Using deprecated, risky, or broken hash algorithms may compromise data integrity and make offline attacks practical. In mobile apps this often appears in three areas: hashing for integrity of local data, hashing of passwords or PINs, and hashing or deriving keys from low-entropy identifiers. Weak or misused hash functions allow adversaries to tamper with data, find collisions, recover secrets, or brute force hashed values.

Hash functions that no longer provide adequate [collision](https://en.wikipedia.org/wiki/Collision_attack) or [preimage](https://en.wikipedia.org/wiki/Preimage_attack) resistance, such as MD5 and SHA-1, enable adversaries to craft different inputs that produce the same hash or to recover the original input more efficiently than brute force. Similarly, using generic fast hash functions for low-entropy inputs like passwords, PINs, device identifiers, or email addresses allows practical offline brute force or dictionary attacks.

Hash-based KDFs such as HKDF are suitable only when the input secret already has high entropy. They are not appropriate as substitutes for password hashing functions because they do not provide work factors or memory hardness.

## Impact

- **Loss of authenticity**: A hashing algorithm, known to be vulnerable to collision attacks, may compromise the authenticity of the data as it allows for two data sources to be identical.
- **Loss of integrity**: Algorithms that are susceptible to length extension attacks may allow an attacker to compromise the integrity of the data by appending data to the original data source.
- **Loss of confidentiality**: A hashing algorithm, known to be vulnerable to pre-image attacks, increases the likelihood that encrypted data can be leaked through using cryptoanalysis or brute-force.

## Modes of Introduction

- **Using a deprecated, risky, or broken hashing algorithm**: E.g., MD5 and SHA-1 have been identified to be vulnerable to collision attacks that are faster than a birthday attack.
- **Using a hash susceptible to length extension attacks**: E.g., MD5 and SHA-1 have been identified to be vulnerable to length extension attacks.
- **Using non-resource-intensive algorithms on low-entropy input**: Using an integrity-based hashing algorithm to hash low-entropy input like pin numbers would make brute-force or dictionary attacks trivial.

## Mitigations

- **Choose collision-resistant algorithm**: Choose an algorithm that is sufficiently collision-resistant, like the integrity algorithms SHA-2 (with 256, 384, 512 bits), BLAKE3 and the SHA-3 family
- **Choose an algorithm with sufficient bit-lengths**: As our computers get stronger, the hashes get weaker, therefore, make sure that you can adjust the bit-length of the algorithm of your choosing. When hashes are stored at rest, make sure to follow the software industry's long-term recommendations (e.g., ["NIST: Transition to Post-Quantum Cryptography Standards](https://csrc.nist.gov/pubs/ir/8547/ipd)").
- **Choose an algorithm fit for its purpose**: To ensure the data's integrity, choose an integrity-based algorithm. When you want to hash low-entropy input, choose a password hash algorithm. Don't try to be clever. Follow recommendations and guidelines.
