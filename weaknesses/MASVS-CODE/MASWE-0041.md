---
title: Running on a Recent Platform Version Not Ensured
id: MASWE-0041
alias: run-on-recent-platform-version
requirement: "The app detects if it is running on an unsupported OS version and reacts appropriately."
platform: [android, ios]
profiles: [L2]
threat: MAS-THREAT-0041
attacks: [MAS-ATTACK-0054, MAS-ATTACK-0055]
mappings:
  masvs-v2: [MASVS-CODE-1]
  cwe: [451, 693, 1104, 1357]
  android-risks:
  - strandhogg
  - unsafe-download-manager
  maswe-beta: [MASWE-0077, MASWE-0057]
refs:
- https://developer.android.com/topic/security/risks/strandhogg
---

## Overview

This weakness occurs when an app does not ensure that it runs on a sufficiently recent platform version, e.g. via `minSdkVersion` on Android or `MinimumOSVersion` on iOS.

Ensuring a recent minimum platform version guarantees the availability of security features and components the app relies on, such as hardware-backed key storage, runtime permissions, Network Security Configuration (Android 7.0+), and App Transport Security (iOS 9+), as well as secure WebView behavior. Supporting older versions also exposes users to platform-level vulnerabilities that were fixed in later releases, such as the StrandHogg task-affinity attacks on older Android versions, which the app cannot fix on its own.

## Modes of Introduction

- **Low Minimum Version with Modern Assumptions**: Setting a low minimum OS version to support older devices while implicitly or explicitly relying on security features (e.g. runtime permissions, hardware-backed keystore, network security policies) that do not exist on those versions.
- **Known-Vulnerable Platform Versions Supported**: Allowing the app to run on OS versions affected by relevant, unfixable platform vulnerabilities (e.g. StrandHogg v1/v2 task affinity and `allowTaskReparenting` abuse on older Android).

## Impact

- **Compromise of Sensitive Data**: Attackers can leverage missing platform protections or unpatched OS vulnerabilities to reach the app's data, resulting in exposure of user data on outdated devices.
- **Authentication or Authorization Bypass**: Attackers can abuse platform flaws such as task hijacking to phish credentials from the app's users on affected versions, resulting in account takeover.

## Mitigations

- **Raise the Minimum Platform Version**: Set `minSdkVersion` / `MinimumOSVersion` high enough that every security feature the app depends on is guaranteed to be present.
- **Gate Sensitive Features by Version**: Where supporting older versions is a hard business requirement, detect the platform version at runtime and disable sensitive functionality, or warn and terminate, on versions that cannot provide the required protections.
- **Reassess the Minimum Regularly**: Revisit the supported version floor as platform vulnerabilities are published and usage of old versions declines.
