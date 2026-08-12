---
title: Improper Cryptographic Key Derivation
id: MASWE-0014
alias: improper-crypto-key-derivation
requirement: "The app derives cryptographic keys using approved key derivation functions."
platform: [android, ios]
profiles: [L1, L2]
threat: MAS-THREAT-0014
attacks: [MAS-ATTACK-0025, MAS-ATTACK-0026]
mappings:
  masvs-v1: [MSTG-CRYPTO-2]
  masvs-v2: [MASVS-CRYPTO-2]
  cwe: [326, 327, 759, 760, 916]
  maswe-beta: [MASWE-0010]
refs:
- https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf
- https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-132.pdf
- https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
---

## Overview

This weakness occurs when cryptographic keys are derived from passwords, passphrases, or other low-entropy inputs using a key derivation function (KDF) that is missing, unsuitable, or misconfigured.

Dedicated password-based KDFs, such as PBKDF2, scrypt, or Argon2, are deliberately expensive to compute and combine the input with a unique random salt, so that each guess costs the attacker significant effort and precomputed tables become useless. When a fast, general-purpose hash is used instead, or when the KDF is configured with a weak work factor or salt, the derived key is far weaker than its nominal length suggests and can be recovered with far less effort than intended.

## Modes of Introduction

- **Plain Hash Instead of a KDF**: Deriving keys by applying a fast, general-purpose hash function to a password or passphrase instead of using a dedicated password-based KDF.
- **Insufficient Work Factor**: Configuring the KDF with too few iterations or with memory and parallelism parameters below current recommendations.
- **Missing or Predictable Salt**: Omitting the salt, hardcoding it in the app, or reusing the same salt across users or installations.
- **Low-Entropy Input**: Deriving keys from inputs with insufficient entropy, such as short PINs or predictable device values, without combining them with additional secret material.

## Impact

- **Compromise of Sensitive Data**: Attackers can decrypt protected information or forge encrypted data, resulting in unauthorized disclosure or modification of sensitive data.
- **Authentication or Authorization Bypass**: Attackers can recover passwords or derived credentials, resulting in unauthorized access to protected accounts, data, or functionality.

## Mitigations

- **Use a Password-Based KDF**: Derive keys from passwords or passphrases only with a dedicated password-based KDF such as PBKDF2, scrypt, or Argon2, following [NIST.SP.800-132](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-132.pdf) and the current [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) recommendations.
- **Use an Adequate Work Factor**: Configure iteration counts, memory, and parallelism parameters according to current guidance, and revisit them periodically as hardware improves.
- **Use Unique Random Salts**: Generate a unique salt with a cryptographically secure random number generator for every derivation and store it alongside the derived material; never hardcode or reuse salts.
- **Strengthen Low-Entropy Inputs**: When the input has low entropy (e.g. a PIN), combine the derived key with additional secret material, such as a random key stored in the platform keystore, so the result cannot be brute-forced from the user input alone.
