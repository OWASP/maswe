---
title: Improper Verification of Cryptographic Signature
id: MASWE-0011
alias: improper-signature-verification
requirement: "The app properly verifies cryptographic signatures."
platform: [android, ios]
profiles: [L1, L2]
threat: MAS-THREAT-0011
attacks: [MAS-ATTACK-0031]
mappings:
  masvs-v1: [MSTG-CRYPTO-4]
  masvs-v2: [MASVS-CRYPTO-1]
  cwe: [295, 347]
  maswe-beta: [MASWE-0026]
refs:
- https://cwe.mitre.org/data/definitions/347.html
- https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-5.pdf
---

## Overview

This weakness occurs when an app fails to verify cryptographic signatures correctly, accepting forged or tampered data as authentic.

Signature verification protects the integrity and authenticity of data such as updates, configuration, licenses, or tokens. The guarantee breaks down when verification is skipped, when its result is ignored, when the signer's key is not validated against a trusted identity, or when the app lets the attacker influence which algorithm or key is used for verification.

## Modes of Introduction

- **Verification Skipped or Result Ignored**: Not verifying signatures on security-relevant data, or computing the verification but proceeding regardless of its result.
- **Untrusted or Unpinned Signer Keys**: Accepting signatures without validating the signer's key against a trusted set or certificate chain, or verifying against public keys that ship alongside the data and can be replaced by an attacker.
- **Algorithm Confusion**: Accepting the algorithm declared by the data being verified (e.g. a token header), including weak, deprecated, or "none" algorithms, instead of enforcing the expected one.

## Impact

- **Execution of Unauthorized Code**: Attackers can deliver tampered updates, plugins, or configuration that the app accepts as genuine, resulting in attacker-controlled code or behavior running within the app.
- **Authentication or Authorization Bypass**: Attackers can forge signed tokens or assertions (e.g. session or license tokens), resulting in unauthorized access to protected accounts, data, or functionality.
- **Compromise of Sensitive Data**: Attackers can substitute tampered data for authentic data without detection, resulting in the app processing or displaying manipulated information.

## Mitigations

- **Always Verify and Check the Result**: Verify signatures on all security-relevant data and treat any verification failure as fatal for the operation; never proceed on an ignored or swallowed result.
- **Validate the Signer's Identity**: Verify signatures only against keys anchored in a trusted set, such as pinned keys or a validated certificate chain, and never against keys delivered alongside the data itself.
- **Enforce the Expected Algorithm**: Allow-list the exact signature algorithms the app expects and reject anything else, including "none" or algorithms chosen by the data being verified.
- **Use Approved Schemes**: Verify with signature schemes approved in [NIST FIPS 186-5](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-5.pdf) and reject weak or deprecated ones.
