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

---

Choosing a deprecated, risky, or broken hash algorithm that is insufficiently collision-resistant may compromise data integrity.

when performing key derivation together with predictable input or in password hashing, the digest (or hash) of an improper implemented or used hash function may allow an adversary to reasonably determine the original input (preimage attack), find another input that can produce the same hash (second preimage attack), or find multiple inputs that evaluate to the same hash (birthday attack/collision attack), given the actor can arbitrarily choose the inputs to be hashed and can do so a reasonable amount of times.

What is regarded as "reasonable" varies by context and threat model, but in general, "reasonable" could cover any attack that is more efficient than brute force (i.e., on average, attempting half of all possible combinations). Note that some attacks might be more efficient than brute force, but are still not regarded as achievable in the real world.

Any algorithm not meeting the above conditions will be considered risky or too "weak" for general use in hashing. When a collision attack is discovered and is found to be faster than a birthday attack, a hash function is often denounced as "broken". This is the case for MD5 and SHA-1.

Another common issue is using an HKDF for key derivation with any type of integrity-based hashing algorithm like MD5, SHA-1, SHA-2, or even SHA-3 on low-entropy input like user-supplied passwords and pins. HKDF isn't designed for low-entropy inputs. Doing so will produce "weak" hashes that can easily be broken.

## Impact

- **Loss of authenticity**: A hashing algorithm, known to be vulnerable to collision attacks, may compromise the authenticity of the data as it allows for two data sources to be identical.
- **Loss of integrity**: Algorithms that are susceptible to length extension attacks may allow an attacker to compromise the integrity of the data by appending data to the original data source.
- **Loss of confidentiality**: A hashing algorithm, known to be vulnerable to pre-image attacks, increases the likelihood that encrypted data can be leaked through using cryptoanalysis or brute-force.

## Modes of Introduction

- **using a deprecated, risky, or broken hashing algorithm**: E.g., MD5 and SHA-1 have been identified to be vulnerable to collision attacks that are faster than a birthday attack.
- **Using a hash susceptible to length extension attacks**: E.g., MD5 and SHA-1 have been identified to be vulnerable to length extension attacks.
- **Using non-resource-intensive algorithms on low-entropy input**: Using an integrity-based hashing algorithm to hash low-entropy input like pin numbers would make brute-force or dictionary attacks trivial.

## Mitigations

- **Choose collision-resistant algorithm**: Choose an algorithm that is sufficiently collision-resistant, like the integrity algorithms SHA-2 (with 256, 384, 512 bits), BLAKE3 and the SHA-3 family
- **Choose an algorithm with sufficient bit-lengths**: As our computers get stronger, the hashes get weaker, therefore, make sure that you can adjust the bit-length of the algorithm of your choosing. When hashes are stored at rest, make sure to follow the software industry's long-term recommendations (e.g, ["NIST: Transition to Post-Quantum Cryptography Standards](https://csrc.nist.gov/pubs/ir/8547/ipd)").
- **Choose an algorithm fit for its purpose**: To ensure the data's integrity, choose an integrity-based algorithm. When you want to hash low-entropy input, choose a password hash algorithm. Don't try to be clever. Follow recommendations and guidelines.
