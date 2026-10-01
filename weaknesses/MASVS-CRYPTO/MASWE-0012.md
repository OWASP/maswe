---
title: Improper Random Number Generation
id: MASWE-0012
cves: [CVE-2024-47126]
alias: improper-random-number-generation
requirement: "The app properly generates random numbers."
platform: [android, ios]
profiles: [L1, L2, EUDIW]
threat: MAS-THREAT-0012
attacks: [MAS-ATTACK-0001, MAS-ATTACK-0019, MAS-ATTACK-0024]
mappings:
  masvs-v1: [MSTG-CRYPTO-6]
  masvs-v2: [MASVS-CRYPTO-1]
  cwe: [332, 337, 338]
  android-risks:
  - weak-prng
  android-core-app-quality: [Cryptographic_Algorithms]
  maswe-beta: [MASWE-0027]
refs:
- https://datatracker.ietf.org/doc/html/rfc4086
- https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html#secure-random-number-generation
- https://www.cisa.gov/news-events/ics-advisories/icsa-24-270-04
---

## Overview

This weakness occurs when random values used in a security context are produced by a non-cryptographic pseudorandom number generator (PRNG) or derived from predictable seeds.

A [PRNG](https://en.wikipedia.org/wiki/Pseudorandom_number_generator) generates sequences deterministically from a seed. Common implementations are not cryptographically secure; for example, they typically use a linear congruential formula whose future outputs can be predicted after observing enough previous outputs. Such generators are not suitable for security-critical purposes like generating session tokens, one-time passwords, or cryptographic key material.

## Modes of Introduction

- **Risky Random APIs**: Using general-purpose random APIs, which do not provide cryptographically secure output, in security-relevant contexts.
- **Non-Random Sources**: Using custom methods to create "supposedly random" values from non-random sources such as the current time.
- **Hardcoded or Predictable Seeds**: Seeding a generator deterministically, e.g. with a hardcoded seed value shipped in the app.

## Example Attack Scenario

In CVE-2024-47126, a vulnerable mobile communications app generated passwords for sharing cryptographic keys using a weak random-number generator.

1. An attacker within radio range captures a cryptographic key broadcast through the app's optional key-sharing feature.
2. The app protects the broadcast key with a password generated using a non-cryptographic random function.
3. Because the password is insufficiently unpredictable, the attacker brute-forces it with significantly less effort.
4. The attacker recovers the shared encryption key, compromising the confidentiality of data protected by that key.

## Impact

- **Authentication or Authorization Bypass**: Attackers can predict session tokens, one-time passwords, or password-reset codes, resulting in unauthorized access to user accounts or privileged functionality.
- **Compromise of Sensitive Data**: Attackers can reproduce cryptographic material derived from predictable values and decrypt protected information, resulting in unauthorized disclosure of sensitive data.

## Mitigations

- **Use Cryptographically Secure RNGs**: For security-relevant contexts, always generate random values with a cryptographically secure random number generator provided by the platform.
- **Avoid Deterministic Seeding**: Do not use any random function in a deterministic way, even a secure one, and especially avoid hardcoded seed values, which can be recovered by decompiling the app.
- **Follow Established Guidance**: Refer to [RFC 4086 - Randomness Requirements for Security](https://datatracker.ietf.org/doc/html/rfc4086) and the [OWASP Cryptographic Storage Cheat Sheet - Secure Random Number Generation](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html#secure-random-number-generation) for recommendations on random number generation.
