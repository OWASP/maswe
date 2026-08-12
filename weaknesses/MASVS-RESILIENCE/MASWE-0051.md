---
title: Root/Jailbreak Detection Not Implemented
id: MASWE-0051
alias: root-jailbreak-detection
requirement: "The app detects if it runs on a rooted/jailbroken device and reacts appropriately."
platform: [android, ios]
profiles: [R]
threat: MAS-THREAT-0051
attacks: [MAS-ATTACK-0003, MAS-ATTACK-0005, MAS-ATTACK-0065]
mappings:
  masvs-v1: [MSTG-RESILIENCE-1, MSTG-RESILIENCE-8]
  masvs-v2: [MASVS-RESILIENCE-1, MASVS-RESILIENCE-4]
  cwe: [1326]
---

## Overview

This weakness occurs when an app does not implement effective techniques to detect whether the device it runs on is rooted or jailbroken.

On a rooted or jailbroken device, the platform's sandboxing and permission guarantees no longer hold: privileged users and tools (e.g. Magisk, SuperSU, Xposed, or jailbreak toolchains and their managers) can access the app's private data, instrument its process, and defeat its client-side controls. More broadly, the app should apply Runtime Application Self-Protection (RASP) techniques that detect a compromised environment and trigger appropriate responses.

## Modes of Introduction

- **No Detection Implemented**: Shipping without any checks for rooting or jailbreak artifacts, such as management apps, su binaries, hooking frameworks, modified system properties, or writable system partitions.
- **Naive or Single-Point Checks**: Implementing one easily located check whose removal or hooking disables the entire defense.
- **No Response Strategy**: Detecting a compromised environment but not responding to it in a way appropriate to the app's risk profile.

## Impact

- **Bypass of Protection Mechanisms**: Attackers can use elevated privileges to defeat the app's client-side security controls, resulting in the circumvention of protections such as anti-tampering, licensing, or fraud controls.
- **Compromise of Sensitive Data**: Attackers can read the app's private data and intercept its runtime state without sandbox restrictions, resulting in exposure of user data, keys, and tokens.

## Mitigations

- **Implement Layered Detection**: Combine multiple, varied checks (file-system artifacts, system properties, management apps, behavioral probes) implemented in different layers (e.g. native code) so no single patch disables them all.
- **Respond Appropriately**: Define graded responses to detection, from warning the user to restricting sensitive functionality or terminating, matched to the app's risk profile.
- **Combine with Attestation**: Back local checks with server-verified device attestation (see @MASWE-0054) so the backend can act on integrity signals even if local checks are bypassed.
- **Assess Effectiveness**: Regularly test the detection against publicly available bypass tools and update it as evasion techniques evolve.
