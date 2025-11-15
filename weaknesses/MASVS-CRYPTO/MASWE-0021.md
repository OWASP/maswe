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

- **Account compromise**: Storing passwords, PINs, tokens, or other low-entropy secrets using fast generic hash functions such as SHA-256 allows attackers who obtain the hashes to perform offline brute force attacks and recover credentials.
- **Loss of integrity**: If an app uses a collision-prone or structurally weak hash to protect configuration files or offline data, an attacker may modify the data and still pass integrity checks by generating a colliding value.
- **Loss of confidentiality**: If encryption keys or key encryption keys are derived by hashing low-entropy input, such as device identifiers or user passwords, attackers can brute force the hash, recover the key, and decrypt protected data.

## Modes of Introduction

- **Using a deprecated, risky, or broken hashing algorithm**: Examples include MD5 and SHA-1, which have practical collision attacks faster than the birthday bound.
- **Using raw hash constructions where a MAC is required**: For example computing SHA-256(secret || data) or SHA-256(data || secret) instead of using HMAC, making the scheme vulnerable to length extension and structural attacks.
- **Using non-resource-intensive algorithms on low-entropy input**: For example hashing passwords or PINs with a single SHA-256 call instead of using a proper password hashing function with salt and work factor.
- **Using unsafe or overly short truncation of hashes**: For instance truncating a message digest to below recommended lengths reduces its security strength. [NIST SP 800-107 Rev 1](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-107r1.pdf) indicates: "The length of truncated message digests used shall be at least twice the desired security strength required for the digital signature".

## Mitigations

- **Choose collision-resistant algorithm**: Choose an algorithm that is sufficiently collision-resistant, like the integrity algorithms SHA-2 (with 256, 384, 512 bits), BLAKE3 and the SHA-3 family
- **Choose an algorithm with sufficient bit-lengths**: As our computers get stronger, the hashes get weaker, therefore, make sure that you can adjust the bit-length of the algorithm of your choosing. When hashes are stored at rest, make sure to follow the software industry's long-term recommendations (e.g., ["NIST: Transition to Post-Quantum Cryptography Standards](https://csrc.nist.gov/pubs/ir/8547/ipd)").
- **Choose an algorithm fit for its purpose**: To ensure the data's integrity, choose an integrity-based algorithm. When you want to hash low-entropy input, choose a password hash algorithm. Don't try to be clever. Follow recommendations and guidelines.
