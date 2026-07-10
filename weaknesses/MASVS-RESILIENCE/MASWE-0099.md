---
title: Emulator Detection Not Implemented
id: MASWE-0099
alias: emulator-detection
platform: [android, ios]
profiles: [R]
mappings:
  masvs-v1: [MSTG-RESILIENCE-5]
  masvs-v2: [MASVS-RESILIENCE-1]
  cwe: [693]
observed_examples:
- https://doi.org/10.1007/978-3-030-00470-5_1
- https://ieeexplore.ieee.org/document/10935812
status: new
---

## Overview

Emulator detection aims to identify when an app runs inside an emulated environment. If an app does not implement these checks, attackers can run the app in controlled environments at scale and observe or automate behavior that would be harder to perform on physical devices.

Also, in the case of Android, as the AOSP operating system and kernel source code are available, the Android emulators can be arbitrairly modified to include platform instrumentation that is harder to detect than common application instrumentation.

## Impact

- **Bypass Protection Mechanisms**: Missing emulator detection allows execution in environments that simplify tampering and analysis and also allow for a deeper level of instrumentation in the case of Android.

## Modes of Introduction

- **Missing Requirement**: Emulator detection is not included in the security requirements or threat model for the application.
- **Disabled in Production**: Checks exist only in debug builds or are disabled through configuration, not being available in the release build.
- **Limited Coverage**: Checks run only at a certain time during the application logic (e.g, startup) and are not enforced throughout the app lifecycle (e.g., before sensitive actions).

## Mitigations

- Define emulator detection as a runtime risk signal for sensitive flows.
- Use multiple independent indicators and evaluate them together rather than relying on a single check.
- Combine client-side checks with server-side evaluation or integrity signals when feasible.
