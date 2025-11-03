---
title: Improper Use of Message Authentication Code (MAC)
id: MASWE-0024
alias: improper-mac
platform: [android, ios]
profiles: [L1, L2]
mappings:
  masvs-v1: [MSTG-CRYPTO-4]
  masvs-v2: [MASVS-CRYPTO-1]
  cwe: [327, 807, 915]

refs:
- https://developer.android.com/privacy-and-security/cryptography#deprecated-functionality
- https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-131Ar2.pdf
- https://csrc.nist.gov/pubs/sp/800/224/ipd
- https://datatracker.ietf.org/doc/html/rfc6151
- https://web.archive.org/web/20170810051504/http://www.tcs.hut.fi/old/papers/aura/aura-csfws97.pdf
- https://en.wikipedia.org/wiki/Replay_attack
draft:
  description: Improper use of MACs in security sensitive contexts affecting data integrity.
  topics:
  - Using HMAC with keys with insufficient entropy
  - Using HMAC with missing timestamp (or nonce)
  - Using MAC‑then‑encrypt or encrypt‑then‑MAC incorrectly, leaking information via timing or error messages
  - Allowing predictors (users or attackers) to control data inputs, creating scenarios where forged or replayed tags bypass integrity checks.
  - Hash functions lacking collision resistance (e.g., MD5 or SHA‑1 used in HMAC)
  - Use of non‑cryptographic checksums (e.g., CRC‑32 instead of HMAC)
  - MAC constructions that fail outside narrow assumptions (e.g., raw CBC‑MAC on variable‑length messages)
  - Tags that are too short significantly lower the effort required for forgery
status: placeholder

---

## Overview

Improper use of a MAC by e.g., not using proper sequence numbers or timestamps, may allow MAC forgeries making it possible to compromiss the authenticity and integrity of the data.

Another common issue is using an HMAC with any type of general based hashing algorithm like MD5, SHA-1, SHA-2 or even SHA-3 on low-entropy input like user supplied passwords and pins. HMAC aren't designed for low-entropy inputs or low-entropy keys. Doing so will result in producing "weak" message digests that easily can be exploited.

A deprecated HMAC implementation may contain bugs that could compromise the authenticity of the data.

## Impact

- **Loss of authenticity**: Improper use of MAC may allow an attacker to compromise the authenticity of the data making the data appear authentic.
- **Loss of Integrity**: Improper use of MAC may allow an attacker to alter the data thereby compromising it's integrity.
- **Loss of Confidentiality**: Using MAC for other purposes than authentication may lead to a complete loss of confidentiality.

## Modes of Introduction

- **Not including a timestamp**: Creating a MAC for message authentication without using a proper timestamp that can be validated to protect against MAC forgery.
- **Using a MAC with low-entropy keys**: Using low-entropy inputs or low-entropy keys as input to a HMAC.

## Mitigations

- **Use MAC with a timestamp**: Generate the MAC over a message with the timestamp included. This should protect the application against replay attacks within a reasonable amount of time. Reasonable, meaning a time frame that is short enough to prevent an attacker from sending an identical message and long enough to allow the message to be sent and digested.
- **Do not use HMAC together with a low-entropy key**: Ensure the keys used are generated using cryptographically secure PRNGs (CSPRNG) generate random numbers that pass statistical randomness tests, and are resilient against prediction attacks.
- **Do not use deprecated HMAC implementations**: Deprecated HMAC implementations could contain errors that allow for collision attacks. Therefore, only use recommended libraries and functions.
