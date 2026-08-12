---
title: Improper Use of Message Authentication Code (MAC)
id: MASWE-0009
alias: improper-mac
requirement: "The app properly uses Message Authentication Codes (MACs)."
platform: [android, ios]
profiles: [L1, L2]
threat: MAS-THREAT-0009
attacks: [MAS-ATTACK-0018, MAS-ATTACK-0021, MAS-ATTACK-0029, MAS-ATTACK-0090]
mappings:
  masvs-v1: [MSTG-CRYPTO-4, MSTG-CRYPTO-5]
  masvs-v2: [MASVS-CRYPTO-1, MASVS-CRYPTO-2]
  cwe: [208, 323, 327, 354, 807]
  maswe-beta: [MASWE-0024, MASWE-0012]
refs:
- https://developer.android.com/privacy-and-security/cryptography#deprecated-functionality
- https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-131Ar2.pdf
- https://csrc.nist.gov/pubs/sp/800/224/ipd
- https://datatracker.ietf.org/doc/html/rfc6151
- https://web.archive.org/web/20170810051504/http://www.tcs.hut.fi/old/papers/aura/aura-csfws97.pdf
- https://en.wikipedia.org/wiki/Replay_attack
---

## Overview

This weakness occurs when a Message Authentication Code (MAC) is missing, built on broken primitives, or used incorrectly in a security-sensitive context, so the integrity and authenticity of messages are no longer guaranteed.

A MAC provides integrity and authenticity for a message using a shared secret key. These guarantees only hold when the MAC algorithm is sound, the key is strong and used for a single purpose, the tag is long enough, verification does not leak information, and the protocol prevents captured messages from being accepted again.

## Modes of Introduction

- **Non-Cryptographic Checksums**: Using checksums such as CRC-32 where a MAC is required; checksums detect accidental corruption but can be trivially recomputed by an attacker.
- **MACs Built on Weak Hashes**: Building MACs on deprecated hash functions such as MD5 or SHA-1, or using naive constructions such as `hash(key ‖ message)` that are vulnerable to length-extension attacks.
- **Weak or Reused MAC Keys**: Using MAC keys with insufficient entropy, or using a MAC key for more than one purpose or with an unauthorized algorithm, violating key-separation principles.
- **Fragile Constructions**: Using constructions that fail outside narrow assumptions, such as raw CBC-MAC on variable-length messages, or composing encryption and authentication incorrectly (e.g. MAC-then-encrypt where encrypt-then-MAC is required).
- **Truncated Tags**: Using authentication tags that are too short, significantly lowering the effort required for forgery.
- **Missing Replay Protection**: Authenticating messages without a timestamp, nonce, or sequence number, so previously captured valid messages remain acceptable.
- **Observable Verification Failures**: Exposing timing differences or detailed error messages during MAC verification that can serve as an oracle.

## Impact

- **Compromise of Sensitive Data**: Attackers can modify protected messages or stored data without detection, resulting in undetected manipulation of sensitive information.
- **Authentication or Authorization Bypass**: Attackers can forge or replay authenticated messages, such as commands or transactions, resulting in unauthorized actions being executed on behalf of the user.

## Mitigations

- **Use Standard MAC Algorithms**: Use HMAC with an approved hash function (SHA-256 or stronger) or an approved authenticated mode, following [NIST SP 800-224](https://csrc.nist.gov/pubs/sp/800/224/ipd) and [NIST.SP.800-131Ar2](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-131Ar2.pdf); never use non-cryptographic checksums for security purposes.
- **Use Strong, Single-Purpose Keys**: Generate MAC keys with a cryptographically secure random number generator and use each key for only one purpose and algorithm.
- **Prefer AEAD or Encrypt-then-MAC**: When combining encryption and authentication, use an AEAD mode (e.g. AES-GCM) or the encrypt-then-MAC composition.
- **Use Full-Length Tags**: Do not truncate authentication tags below the length required by the security level of the use case.
- **Add Replay Protection**: Include and verify a timestamp, nonce, or sequence number in authenticated messages so captured messages cannot be replayed.
- **Verify in Constant Time**: Compare tags using constant-time comparison and return uniform errors so verification cannot be used as an oracle.
