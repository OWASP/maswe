---
title: Improper Use of the Clipboard
id: MASWE-0030
alias: improper-clipboard
requirement: "The app uses the clipboard securely and only with user consent."
platform: [android, ios]
profiles: [L1, L2]
threat: MAS-THREAT-0030
attacks: [MAS-ATTACK-0041]
mappings:
  masvs-v2: [MASVS-PLATFORM-1, MASVS-STORAGE-2]
  cwe: [200, 668]
  android-risks:
  - secure-clipboard-handling
  maswe-beta: [MASWE-0059]
refs:
- https://developer.android.com/develop/ui/views/touch-and-input/copy-paste#PreventingSensitiveData
- https://developer.apple.com/documentation/uikit/uipasteboard
---

## Overview

This weakness occurs when an app places sensitive data on the system clipboard, or handles clipboard content insecurely, exposing that data beyond the app's control.

The clipboard is a shared resource: other apps can read its contents, and on some platforms, clipboard content synchronizes to nearby devices (e.g. the iOS [Universal Clipboard](https://support.apple.com/en-us/102430)). Copying sensitive data such as passwords, one-time codes, card numbers, or tokens to the clipboard, failing to mark it as sensitive, or leaving it there indefinitely can leak that data to other apps and devices.

## Modes of Introduction

- **Sensitive Data Copyable Without User Consent**: Copying sensitive values such as passwords, one-time codes, or card numbers to the clipboard without user consent.
- **Clipboard Content Not Marked Sensitive**: Not flagging copied sensitive content as sensitive where the platform supports it (e.g. `EXTRA_IS_SENSITIVE` on Android), so previews and clipboard history show it in cleartext.
- **Universal Clipboard Not Restricted**: Not restricting sensitive clipboard items to the local device or setting an expiration on iOS, letting them sync to other devices.
- **Clipboard Not Cleared**: Leaving sensitive content on the clipboard after it has served its purpose.
- **Untrusted Clipboard Input**: Processing pasted clipboard data without validation, even though any app can have written it.

## Impact

- **Compromise of Sensitive Data**: Attackers can read personal or financial data from the clipboard, resulting in unauthorized disclosure of user data.
- **Authentication or Authorization Bypass**: Attackers can capture copied credentials or one-time codes, resulting in unauthorized access to the user's accounts.

## Mitigations

- **Avoid the Clipboard for Secrets**: Disable copying for sensitive fields and provide secure alternatives such as auto-fill (see @MASWE-0019) so users never need to copy secrets.
- **Only Copy with User Consent**: If copying is required, ask the user for consent before placing sensitive data on the clipboard, or only act as a result of a user-chosen action (e.g. a "Copy" button).
- **Mark Clipboard Content as Sensitive**: When sensitive content must be copied, flag it as sensitive so the platform masks previews and treats it accordingly.
- **Specify an appropriate expiration**: When sensitive content must be copied, set an expiration so it is removed from the clipboard after a short time.
- **Restrict Clipboard Exposure**: When copying, follow the platform's [secure clipboard handling guidance on Android](https://developer.android.com/privacy-and-security/risks/secure-clipboard-handling) and mark the content using [`ClipDescription.EXTRA_IS_SENSITIVE`](https://developer.android.com/reference/android/content/ClipDescription#EXTRA_IS_SENSITIVE) to obscure clipboard previews. On iOS, use pasteboard options such as [`localOnly`](https://developer.apple.com/documentation/uikit/uipasteboard/optionskey/localonly) and [`expirationDate`](https://developer.apple.com/documentation/uikit/uipasteboard/optionskey/expirationdate) to limit cross-device propagation and content lifetime.
- **Validate Pasted Data**: Treat clipboard content as untrusted input and validate it before use.
