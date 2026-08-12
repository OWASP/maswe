---
title: Runtime Code Integrity Not Verified
id: MASWE-0058
alias: runtime-code-integrity
requirement: "The app detects unauthorized changes to its code and execution flow at runtime."
platform: [android, ios]
profiles: [R]
threat: MAS-THREAT-0058
attacks: [MAS-ATTACK-0002, MAS-ATTACK-0003]
mappings:
  masvs-v1: [MSTG-RESILIENCE-6]
  masvs-v2: [MASVS-RESILIENCE-2]
  maswe-beta: [MASWE-0107]
---

## Overview

This weakness occurs when an app is running in an unsafe environment (rooted or jailbroken device) and does not verify the integrity of its own code at runtime, allowing in-memory patching, code injection, and hooking to go undetected.

Even a correctly signed app can be modified while it runs: attackers can patch instructions in memory, inject libraries into the process, or hook functions to change their behavior. Runtime code integrity verification, such as checking loaded code segments, detecting injected libraries, and spotting patched function prologues, complements packaged-app integrity verification (see @MASWE-0056) by covering tampering that happens after the app has launched.

Unlike dynamic-analysis tool detection (see @MASWE-0065), runtime integrity verification detects unauthorized changes to the app's memory and execution state without relying on tool-specific artifacts.

## Modes of Introduction

- **No Runtime Code Checks**: Not verifying the integrity of loaded code segments or executable memory at runtime.
- **Injected Libraries or Executable Mappings Not Detected**: Not inspecting the process for executable memory mappings or libraries that are unexpected for the app or platform.
- **Hooked Functions Not Detected**: Not checking security-critical functions for patched prologues or redirected implementations.
- **No Response to Tampering**: Detecting modifications but not reacting to protect sensitive operations.

## Impact

- **Bypass of Protection Mechanisms**: Attackers can patch or hook the functions implementing the app's security checks, resulting in the circumvention of its client-side defenses.
- **Compromise of Sensitive Data**: Attackers can redirect or wrap data-handling functions to siphon their inputs and outputs, resulting in exposure of credentials and user data processed by the app.

## Mitigations

- **Verify Code Segments at Runtime**: Periodically validate the integrity of the app's loaded code and executable memory, especially around sensitive operations.
- **Detect Injection and Hooking**: Check for foreign libraries in the process and for patched prologues or redirected implementations of security-critical functions.
- **Layer and Protect the Checks**: Implement checks in native code, diversify them, and protect them with obfuscation (see @MASWE-0059) so they cannot all be disabled with one patch.
- **Respond to Detection**: Terminate, restrict functionality, or signal the backend when runtime tampering is detected, and assess the checks against current hooking frameworks.
