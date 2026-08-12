---
title: Enforced Updating Not Implemented
id: MASWE-0043
alias: enforced-updating
requirement: "The app detects if it must be updated and reacts appropriately."
platform: [android, ios]
profiles: [L2]
threat: MAS-THREAT-0043
attacks: [MAS-ATTACK-0040, MAS-ATTACK-0053]
mappings:
  masvs-v1: [MSTG-ARCH-9]
  masvs-v2: [MASVS-CODE-2]
  cwe: [602, 693]
  maswe-beta: [MASWE-0075]
refs:
- https://developer.android.com/guide/playcore/in-app-updates
- https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager
- https://medium.com/swlh/updating-users-to-the-latest-app-release-on-ios-ed96e4c76705
- https://gist.github.com/DineshKachhot/f63fcebceca6351fc982cafd38f6f05c
---

## Overview

This weakness occurs when an app has no mechanism to force users to update to a more secure version after a critical vulnerability has been remediated.

When a critical vulnerability is found in a production app, the developer needs a way to migrate existing users to the latest version as quickly as possible. Platforms provide building blocks for this, such as Android In-App Updates (`AppUpdateManager`) and store version checks on iOS, but robust enforcement requires the backend to signal and enforce the minimum acceptable version.

## Modes of Introduction

- **No Enforced-Update Mechanism**: Shipping the app without any in-app or enforced update flow, so vulnerable versions keep working indefinitely.

## Impact

- **Compromise of Sensitive Data**: Attackers can exploit already-fixed vulnerabilities against users stuck on old versions, resulting in exposure of user data long after a patch was published.
- **Compromise of System Integrity and Business Operations**: The app owner cannot retire vulnerable versions from the installed base, resulting in a prolonged attack window.

## Mitigations

- **Implement an Enforced Update Flow**: Use platform mechanisms such as Android In-App Updates or a version check against the app store on iOS to require updating when a critical fix ships.
- **Enforce the Minimum Version Server-Side**: Have the backend declare the minimum supported app version and reject requests from older clients.
- **Distinguish Flexible and Immediate Updates**: Reserve blocking (immediate) updates for security-critical releases and use flexible updates otherwise, so users accept the mechanism when it matters.
