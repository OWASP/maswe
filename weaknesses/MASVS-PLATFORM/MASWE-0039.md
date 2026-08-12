---
title: App Vulnerable to Overlay Attacks
id: MASWE-0039
alias: tapjacking-attacks
requirement: "The app protects its sensitive screens against overlay attacks."
platform: [android, ios]
profiles: [L2]
threat: MAS-THREAT-0039
attacks: [MAS-ATTACK-0036]
mappings:
  masvs-v1: [MSTG-PLATFORM-9]
  masvs-v2: [MASVS-PLATFORM-3, MASVS-CODE-1]
  cwe: [1021]
  android-risks:
  - tapjacking
  maswe-beta: [MASWE-0056]
refs:
- https://developer.android.com/topic/security/risks/tapjacking
---

## Overview

This weakness occurs when an app does not defend its sensitive screens against being fully or partially obscured by attacker-controlled windows.

In an overlay attack, a malicious app draws content on top of the target app to trick the user into interacting with it (tapjacking) or to capture their input. The user believes they are interacting with the visible overlay while their touches reach the app underneath, or vice versa. Sensitive confirmation screens, permission-like prompts, and input fields are the typical targets.

## Modes of Introduction

- **Touch Filtering Not Enabled**: Not enabling touch filtering on sensitive views (e.g. `setFilterTouchesWhenObscured(true)` or `android:filterTouchesWhenObscured="true"`) and not discarding touch events flagged as obscured (e.g. `FLAG_WINDOW_IS_PARTIALLY_OBSCURED`).
- **External Overlays Not Hidden**: Not using `setHideOverlayWindows(true)` to hide external overlays
- **Sensitive Screens Not Protected**: Presenting confirmation dialogs or security-relevant screens without any occlusion defense, so their content can be covered or mimicked by an overlay.

## Impact

- **Financial Loss**: Attackers can trick users into confirming payments or transfers they believe to be something else, resulting in direct financial harm to the user.
- **Authentication or Authorization Bypass**: Attackers can trick users into granting permissions or approving security prompts, resulting in unauthorized access to protected data or functionality.
- **Compromise of Sensitive Data**: Attackers can capture input entered into overlay-mimicked fields, resulting in the disclosure of credentials or other sensitive user input.

## Mitigations

- **Enable Touch Filtering on Sensitive Views**: Configure sensitive views to ignore touches delivered while the window is obscured, and discard motion events flagged as (partially) obscured.
- **Hide External Overlays**: Configure sensitive activities to hide all external overlays.
- **Protect Sensitive Screens**: Apply overlay defenses to confirmation and authentication screens specifically, and consider pausing or hiding sensitive content when the app detects it is being drawn over.
- **Use Trusted Confirmation Paths for Critical Actions**: For the most critical approvals, use hardware-protected confirmation mechanisms that overlays cannot forge (see @MASWE-0025).
