---
title: Latest Platform Version Not Targeted
id: MASWE-0042
alias: target-latest-platform-version
requirement: "The app targets the latest platform version."
platform: [android, ios]
profiles: [L1, L2]
threat: MAS-THREAT-0042
attacks: [MAS-ATTACK-0056]
mappings:
  masvs-v2: [MASVS-CODE-1]
  cwe: [693, 1357]
  android-core-app-quality: [Target_SDK_Version, Compile_SDK_Version]
  maswe-beta: [MASWE-0078]
refs:
- https://developer.android.com/google/play/requirements/target-sdk
- https://developer.apple.com/news/upcoming-requirements/
---

## Overview

This weakness occurs when an app does not target the latest platform version, missing the newest platform-enforced security protections and behavior changes.

Targeting the latest platform version, via `targetSdkVersion` on Android or by building with the latest Xcode/SDK on iOS, opts the app into protections such as scoped storage, stricter runtime-permission handling, permission auto-reset, and modern TLS defaults. When an app targets an old version, the OS applies backward-compatibility behaviors and the app silently misses these protections. This is distinct from the minimum supported version (see @MASWE-0041): here the concern is the target/compiled version.

## Modes of Introduction

- **Outdated Target Version**: Keeping `targetSdkVersion` on Android, or the Xcode/SDK used to build on iOS, below current requirements, so newer platform-enforced protections never apply to the app.
- **Compatibility Behaviors Left in Place**: Relying on legacy behaviors (e.g. broad storage access or lenient permission handling) that only continue to work because the app targets an old version.

## Impact

- **Compromise of Sensitive Data**: Attackers can take advantage of legacy behaviors, such as broader file-system or permission access, resulting in exposure of user data that current platform defaults would have protected.
- **Compromise of System Integrity and Business Operations**: The app can fall below app-store target-version requirements, resulting in blocked updates or removal from distribution for the app owner.

## Mitigations

- **Target the Latest Platform Version**: Update `targetSdkVersion` and build with the latest SDK promptly each platform cycle, following the store requirements for [Android](https://developer.android.com/google/play/requirements/target-sdk) and [iOS](https://developer.apple.com/news/upcoming-requirements/).
- **Adopt New Protections**: Review each platform release's behavior changes and migrate off legacy behaviors.
