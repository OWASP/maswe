---
title: Improper Generation of Cryptographic Signatures
id: MASWE-0118
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

## Overview

Improper Key derivation functions will generate a key using a scheme or iteration count that does not provide a sufficient level of computational effort. This can open up the possibility for brute force password/secret cracking or dictionary attacks.
In cases where a user-supplied password or pin is used without a sufficiently random salt the resulting output will be identical or similar enough to allow an attacker to execute a brute force attack to find the original password/pin using the KDF (key derivation function) as an "oracle".
A similar issue happens when the salt is user-supplied or left out. Consider a mobile app that generates user keys from a master key on demand during installation. Let's say that a key used in the mobile app is derived from this master key using the username or other user supplied value as salt. Such an implementation can make it possible for an attacker to retrieve the derived key by using the username or supplied user value as input.

HKDFs or any other type of integrity based hashing algorithm like MD5, SHA-1, SHA-2 or even SHA-3 aren't designed for low-entropy inputs like in the username example above. Therefore, password crackers can fairly efficiently crack massive amounts of passwords for KDFs that aren't purposefully designed to be slow and memory-intensive.
A similar issue happens when using deprecated, risky or broken KDF- or password hashing algorithms known to the vulnerable to various types of attacks.
Also, cryptographic algorithms (such as symmetric encryption or some MACs) expect a secret input of a given size.

For example, AES uses a key of exactly 16 bytes. A naive implementation might use a username, a low entropy password or pin directly as an input key. Using a username, a low entropy password or pin as an input key has the following problems:

- If the password is smaller than the key, the full key space isn't used. The remaining space is padded, often with spaces or null bytes.
- A user-supplied password will realistically consist mostly of displayable and pronounceable characters. Therefore, only some of the possible 256 ASCII characters are used and entropy is decreased by approximately a factor of four.

## Impact

- **Risk of Brute-Force Attacks**: Improper Key derivation functions expose the app to brute force password- and secret cracking attacks, and key or dictionary attacks such as rainbow tables.
- **Loss of Confidentiality**: Improper Key derivation may allow an attacker to guess or find the input and therefore steal the user's password or cryptographic key.
- **Loss of Integrity**: Given that the attacker has access to the user's password or cryptographic key, the overall security of the app and mobile phone may be compromised.

## Modes of Introduction

- **Using static or predictable salt on low-entropy input**: Using an enumerable pin code or low entropy password together with a static or predictable salt makes it possible for the attacker to to pre-compute the hash value using dictionary attack, effectively disabling the protection that a salt would provide.
- **Using user-supplied salt**: Using a low entropy salt will make it possible for an attacker to extract all derived keys through a KDF by supplying the low entropy salt as an argument.
- **Using non-resource intensive algorithms on low-entropy input**: Using an enumerable pin code or low entropy password together with a HKDF makes it easy for password crackers to execute a preimage attack.
- **Use a hash function as a general-purpose KDF**: In scenarios where the information used during key derivation is attacker-controlled, using a integrity based hash function (e.g from the SHA family) as KDF can expose the application to brute force or length-extension attacks.
- **Using Deprecated, Risky or Broken Algorithms**: Relying on deprecated, risky or inherently broken cryptographic algorithms can result in the generation of weaker keys. As these algorithms often have vulnerabilities or support shorter key lengths, they are more susceptible to modern attacks, compromising the overall security of the app.

## Mitigations

- **Generate random salt using CSPRNGs with high entropy seeding**: Ensuring the use of strong, cryptographically secure PRNGs called CSPRNGs with high entropy seeding is essential for robust key security.
- **Use Recommended and Approved algorithms that are fit for purpose**: In cases where the input is user-controlled, use key derivation functions such as Argon2, scrypt, bcrypt or PBKDF2 that provide a sufficient level of computational effort. Otherwise, ensure the input is thoroughly random using a recommended CSPRNG that guarantees high entropy seeding.
- **Prefer HKDF and other KDFs that were designed specifically for key derivation**: HKDF and other KDFs specifically meant for key derivation will ensure the app isn't exposed to length-extension attacks.
=======
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
