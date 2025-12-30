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
status: new
---

## Overview

Emulator detection aims to identify when an app runs inside an emulated environment. If an app does not implement these checks, attackers can run the app in controlled environments at scale and observe or automate behavior that would be harder to perform on physical devices.

## Impact

- **Bypass Protection Mechanism**: Missing emulator detection allows execution in environments that simplify tampering and analysis.
- **Scalable Abuse and Automation**: Emulators support large-scale automation, which can enable fraud or abuse that depends on high volume.
- **Increased Reverse Engineering Exposure**: Emulators reduce the cost of dynamic analysis and instrumentation, exposing sensitive logic or data.

## Modes of Introduction

- **Missing Requirement**: Emulator detection is not included in the security requirements or threat model.
- **Disabled in Production**: Checks exist only in debug builds or are disabled through configuration.
- **Limited Coverage**: Checks run only at startup and are not enforced before sensitive actions.

## Mitigations

- Define emulator detection as a runtime risk signal for sensitive flows and document how it influences access decisions.
- Use multiple independent indicators and evaluate them together rather than relying on a single check.
- Revalidate at critical actions or high-risk workflows to limit one-time bypasses.
- Combine client-side checks with server-side evaluation or integrity signals when feasible.
