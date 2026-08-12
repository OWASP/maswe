---
title: Unsafe Dynamic Code Loading
id: MASWE-0049
alias: unsafe-code-loading
requirement: "The app loads dynamic code safely from trusted sources."
platform: [android, ios]
profiles: [L2]
threat: MAS-THREAT-0049
attacks: [MAS-ATTACK-0014, MAS-ATTACK-0057]
mappings:
  masvs-v2: [MASVS-CODE-4]
  cwe: [494]
  android-risks:
  - dynamic-code-loading
  - create-package-context
  android-core-app-quality: [App_Bundles]
  maswe-beta: [MASWE-0085]
refs:
- dynamic-code-loading
---

## Overview

This weakness occurs when an app loads and executes code resolved at runtime without verifying its source and integrity.

Dynamic code loading includes loading native libraries via `dlopen`, loading DEX/JAR files through class loaders, and downloading executable code or scripts at runtime. When the loaded code comes from writable or external locations, or is fetched without integrity and authenticity verification, an attacker who can modify or substitute it gains arbitrary code execution within the app's context, with all the app's permissions and data access.

## Modes of Introduction

- **Loading from Writable or External Locations**: Loading native libraries or DEX/JAR files from writable, external, or world-accessible storage where other malicious apps can replace them.
- **Downloaded Code Without Verification**: Downloading and executing code, plugins, or scripts without verifying their integrity and authenticity (e.g. signature verification, see @MASWE-0011).
- **Code from Other Packages**: Executing code from other installed packages (e.g. via package contexts with code inclusion) whose identity and integrity are not verified.

## Impact

- **Execution of Unauthorized Code**: Attackers can run attacker-controlled code with the app's identity, permissions, and data access, resulting in full compromise of the app's functionality on the device.
- **Compromise of Sensitive Data**: Attackers can use the injected code to read the app's private data and credentials, resulting in unauthorized disclosure of user and app data.

## Mitigations

- **Avoid Dynamic Code Loading**: Ship all executable code inside the signed app package whenever possible; app stores also restrict runtime code delivery.
- **Load Only from Protected Locations**: When loading is unavoidable, load code only from the app's protected, read-only installation directories, never from writable or external storage.
- **Verify Integrity and Authenticity**: Verify a cryptographic signature over any dynamically delivered code against a pinned trusted key before loading it, and deliver it only over secure channels.
