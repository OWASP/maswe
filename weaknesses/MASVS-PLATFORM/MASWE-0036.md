---
title: Unnecessary Exposure of Sensitive Data via the User Interface
id: MASWE-0036
alias: data-leak-ui
requirement: "The app does not unnecessarily expose sensitive data through its user interface."
platform: [android, ios]
profiles: [L2]
threat: MAS-THREAT-0036
attacks: [MAS-ATTACK-0005, MAS-ATTACK-0041, MAS-ATTACK-0043]
mappings:
  masvs-v1: [MSTG-STORAGE-7]
  masvs-v2: [MASVS-PLATFORM-3, MASVS-STORAGE-2]
  cwe: [200, 359]
  maswe-beta: [MASWE-0053]
refs:
- https://developer.android.com/develop/ui/views/touch-and-input/keyboard-input/style#Type
- https://developer.apple.com/documentation/uikit/uitextinputtraits/1624427-issecuretextentry
---

## Overview

This weakness occurs when an app exposes sensitive data beyond what is required for the user's current task, or exposes required data without protections proportionate to its sensitivity through its user interface.

The typical exposure path involves displaying secrets or sensitive information in cleartext when masking or a partial representation would suffice, (e.g., using unprotected input fields for passwords or PINs).

## Modes of Introduction

- **Non-Secure Text Entry**: Building password or PIN fields without inserting them in platform-specific fields that mask sensitive data (e.g. [`isSecureTextEntry`](https://developer.apple.com/documentation/uikit/uitextinputtraits/issecuretextentry) on iOS, [`textPassword`](https://developer.android.com/develop/ui/views/touch-and-input/keyboard-input/style#Type) input types on Android), so the input is shown in cleartext.
- **Unmasked Sensitive Values**: Displaying full values (e.g. complete card numbers or personal identifiers) where a masked or partial representation would suffice.

## Impact

- **Compromise of Sensitive Data**: Sensitive information may be observed from the screen and captured by other user.
- **Authentication or Authorization Bypass**: Attackers can capture credentials, PINs, or one-time codes exposed through the UI, resulting in unauthorized access to the user's accounts.

## Mitigations

- **Use Secure Text Entry for Secrets**: Configure passwords, PINs, and other secrets using the platform's secure text-entry controls, such as [`textPassword` on Android Views](https://developer.android.com/develop/ui/views/touch-and-input/keyboard-input/style), [`SecureTextField` in Jetpack Compose](https://developer.android.com/develop/ui/compose/text/user-input), or [`isSecureTextEntry` on iOS](https://developer.apple.com/documentation/uikit/uitextinputtraits/issecuretextentry). Do not rely solely on custom visual masking when a platform-provided secure text-entry control is available.
- **Minimize Visual Disclosure**: Display only the portion of a sensitive value required for the user's current task. When revealing the full value is necessary, reveal it only after an explicit user action (see @MASWE-0023) and for a limited duration.
