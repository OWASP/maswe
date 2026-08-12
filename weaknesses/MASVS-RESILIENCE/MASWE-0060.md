---
title: Resource Obfuscation Not Implemented
id: MASWE-0060
alias: resource-obfuscation
requirement: "The app applies resource obfuscation to hinder reverse engineering."
platform: [android, ios]
profiles: [R]
threat: MAS-THREAT-0060
attacks: [MAS-ATTACK-0001]
mappings:
  masvs-v1: [MSTG-RESILIENCE-11]
  masvs-v2: [MASVS-RESILIENCE-3]
  cwe: [693]
  maswe-beta: [MASWE-0090]
---

## Overview

This weakness occurs when an app's resources and assets are left in clear, unprotected form, revealing how the app works and aiding reverse engineering.

In addition to application code, various artifacts such as strings, layouts, configuration files and bundled data all contain information about the app's inner workings. Attackers mining the package can use them to map features, find security-relevant configuration, and identify targets for tampering. Note that obfuscation or encryption applied without integrity validation can itself be tampered with, so resource protection should complement, not replace, integrity checks (see @MASWE-0057).

## Modes of Introduction

- **Resources Left in Clear**: Shipping strings, configuration, and other assets unobfuscated and unencrypted in the application package.
- **Identifiers Left Meaningful**: Keeping descriptive resource and string identifiers that map directly to features and security controls.

## Impact

- **Bypass of Protection Mechanisms**: Attackers can locate security-relevant configuration and assets and use cross-references to target the app's security-relevant code locations, resulting in easier circumvention of its protections.
- **Compromise of Sensitive Data**: Attackers can extract proprietary content and internal information from clear resources, resulting in intellectual property exposure.

## Mitigations

- **Obfuscate Sensitive Resources**: Obfuscate strings, configuration, and assets that reveal security-relevant behavior.
- **Obfuscate Resource Identifiers**: Replace meaningful resource and string identifiers with non-descriptive ones in release builds.
- **Validate Resource Integrity**: Combine resource protection with integrity verification (see @MASWE-0057) so protected resources cannot simply be replaced.
