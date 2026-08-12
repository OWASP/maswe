---
title: Compiler-Provided Security Features Not Used
id: MASWE-0045
alias: compiler-provided-security-features-not-implemented
requirement: "The app uses the compiler-provided security features of the platform."
platform: [android, ios]
profiles: [L2]
threat: MAS-THREAT-0045
attacks: [MAS-ATTACK-0001, MAS-ATTACK-0059]
mappings:
  masvs-v2: [MASVS-CODE-3, MASVS-CODE-4]
  android-risks:
  - use-of-native-code
  maswe-beta: [MASWE-0116]
refs:
- https://android.googlesource.com/platform/ndk/+/master/docs/BuildSystemMaintainers.md
- https://sensepost.com/blog/2021/on-ios-binary-protections/
- https://www.sans.org/blog/stack-canaries-gingerly-sidestepping-the-cage/
---

## Overview

This weakness occurs when an app's native code is built without the exploit-mitigation features that compilers and toolchains provide.

Mitigations such as stack canaries (stack-smashing protection), Address Space Layout Randomization (ASLR) via Position-Independent Executables (PIE/PIC), non-executable memory (NX/DEP), fortified (bounds-checked) libc functions, and Automatic Reference Counting (ARC) on iOS do not remove memory-corruption bugs, but they substantially raise the effort required to exploit them. Binaries built without these features make any memory-corruption vulnerability, in the app's own code or its native dependencies, far easier to turn into code execution.

## Modes of Introduction

- **Missing Stack Protection**: Compiling native code without stack canaries, leaving stack-based buffer overflows directly exploitable.
- **Missing PIE/ASLR Support**: Building binaries that are not position-independent, defeating address-space layout randomization. Note that on current Android versions the linker no longer loads non-PIE binaries, but legacy toolchains and other platforms can still produce them.
- **Missing Fortified Functions**: Building without fortify-source style bounds-checked replacements for risky libc functions.
- **Unsafe Memory Management Choices**: Disabling Automatic Reference Counting on iOS or otherwise opting out of memory-safety features where safer defaults exist.

## Impact

- **Execution of Unauthorized Code**: Attackers can convert memory-corruption bugs into reliable code execution in the app's context, resulting in full compromise of the app and its data.
- **Compromise of Sensitive Data**: Attackers can read process memory through exploited native bugs, resulting in exposure of credentials, keys, and user data held in memory.

## Mitigations

- **Enable Compiler Mitigations**: Build all native code and dependencies with stack canaries, PIE/PIC, non-executable memory, and fortified functions enabled, and verify the flags in release binaries rather than assuming toolchain defaults.
- **Keep Memory-Safety Features On**: Use Automatic Reference Counting on iOS and prefer memory-safe languages for new code where feasible.
