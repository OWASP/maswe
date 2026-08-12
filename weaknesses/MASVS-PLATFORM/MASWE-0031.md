---
title: Allowing Untrusted App Extensions
id: MASWE-0031
alias: insecure-app-extensions
requirement: "The app only permits trusted app extensions to interact with it."
platform: [ios]
profiles: [L1, L2]
threat: MAS-THREAT-0031
attacks: [MAS-ATTACK-0048]
mappings:
  masvs-v1: [MSTG-PLATFORM-11]
  masvs-v2: [MASVS-PLATFORM-1, MASVS-STORAGE-2]
  cwe: [829]
  maswe-beta: [MASWE-0061]
refs:
- https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623122-application
- https://developer.apple.com/documentation/uikit/uiapplication/extensionpointidentifier/keyboard
---

## Overview

This weakness occurs when an app allows untrusted app extensions, such as custom keyboards or share and action extensions, to interact with it and observe the data it handles.

On iOS, app extensions run third-party code that can interact with the host app and observe or exfiltrate the data the app hands to them. A custom keyboard, for example, sees every keystroke typed while it is active. An app that handles sensitive data should restrict which extension point identifiers it allows, for example by implementing `application(_:shouldAllowExtensionPointIdentifier:)` to reject untrusted extension categories, and by disabling third-party keyboards for sensitive input.

## Modes of Introduction

- **All Extension Points Allowed**: Not implementing `application(_:shouldAllowExtensionPointIdentifier:)`, so every extension category, including custom keyboards, can interact with the app.
- **Third-Party Keyboards Allowed for Sensitive Input**: Allowing custom keyboards (the `keyboard` extension point) while users enter credentials, payment data, or other secrets.
- **Sensitive Data Handed to Extensions**: Passing more data than necessary to share or action extensions, which can process and transmit it outside the app's control.

## Impact

- **Compromise of Sensitive Data**: Attackers can log keystrokes or read content handed to a malicious extension, resulting in unauthorized disclosure of personal data typed into or shared from the app.
- **Authentication or Authorization Bypass**: Attackers can capture credentials or one-time codes typed on a malicious keyboard, resulting in unauthorized access to the user's accounts.

## Mitigations

- **Restrict Extension Points**: Implement `application(_:shouldAllowExtensionPointIdentifier:)` and reject extension categories the app does not need to support.
- **Keep Sensitive Input on the System Keyboard**: Disable third-party keyboards for sensitive fields; secure text entry fields automatically use the system keyboard.
- **Minimize Data Shared with Extensions**: Hand share and action extensions only the specific items being shared, never broader app data.
