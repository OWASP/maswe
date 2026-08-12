---
title: Debugger Detection Not Implemented
id: MASWE-0064
alias: debugger-detection
requirement: "The app detects debugger attachment at runtime and responds to protect sensitive operations."
platform: [android, ios]
profiles: [R]
threat: MAS-THREAT-0064
attacks: [MAS-ATTACK-0002]
mappings:
  masvs-v1: [MSTG-RESILIENCE-2]
  masvs-v2: [MASVS-RESILIENCE-4]
  maswe-beta: [MASWE-0101]
refs:
- https://developer.android.com/reference/android/os/Debug#isDebuggerConnected()
- https://man7.org/linux/man-pages/man5/proc_pid_status.5.html
- https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/ptrace.2.html
- https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html
- https://www.youtube.com/watch?v=ih6gWZDuNME
---

## Overview

This weakness occurs when an app does not detect the presence of a debugger attached to it at runtime.

A debugger lets an attacker inspect memory, set breakpoints, and alter control flow to bypass client-side controls, even when the release build is not flagged as debuggable (see @MASWE-0063 for that case). Platforms offer detection primitives such as `Debug.isDebuggerConnected()` (Java debugging) and the `TracerPid` field in `/proc/self/status` on Android (Native debugging), or `sysctl`- and `ptrace`-based checks on iOS. Without such checks and a response, a debugger can be attached and used against the app unnoticed.

## Modes of Introduction

- **No Debugger Checks**: Shipping without any runtime verification that a debugger is attached to the process.
- **One-Time or Single-Point Checks**: Checking only at startup or in a single code path instead of around sensitive operations and throughout runtime.
- **No Response Strategy**: Detecting a debugger but not reacting in a way that protects the app's sensitive operations.

## Impact

- **Bypass of Protection Mechanisms**: Attackers can alter control flow at breakpoints to skip the app's client-side checks, resulting in the circumvention of its defenses.
- **Compromise of Sensitive Data**: Attackers can read secrets and user data from process memory during debugging, resulting in exposure of credentials, keys, and tokens.

## Mitigations

- **Implement Debugger Detection**: Use platform primitives (e.g. `Debug.isDebuggerConnected()`, `TracerPid`, `sysctl`/`ptrace`-based checks) implemented in multiple layers, including native code.
- **Check Continuously**: Run detection periodically and around sensitive operations, not only at startup, so late attachment is also caught.
- **Respond to Detection**: Terminate, wipe sensitive state, or restrict functionality when a debugger is detected, according to the app's risk profile.
- **Assess Effectiveness**: Test the checks against common anti-anti-debugging techniques and refine them over time.
