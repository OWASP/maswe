---
title: App Virtualization Environment Detection Not Implemented
id: MASWE-0052
alias: app-virtualization-detection
requirement: "The app detects when it is running inside an app-virtualization environment."
platform: [android, ios]
profiles: [R]
threat: MAS-THREAT-0052
attacks: [MAS-ATTACK-0067]
mappings:
  masvs-v2: [MASVS-RESILIENCE-1]
  cwe: [693]
  maswe-beta: [MASWE-0098]
---

## Overview

This weakness occurs when an app does not detect that it is running inside an app-virtualization or cloning environment.

App virtualization and "dual-app" container frameworks run an app inside another app's process, letting the hosting app intercept its calls, access its data, and instrument it, all without rooting the device. They also enable running multiple cloned instances of the same app. An app that does not check for anomalies in its process path and package structure, or for known virtualization frameworks, cannot respond to running in such a hostile host.

## Modes of Introduction

- **No Virtualization Checks**: Not verifying the app's process path, package structure, or runtime environment for signs of running inside another app's process.
- **Known Frameworks Not Detected**: Not checking for artifacts of known virtualization and cloning frameworks.
- **No Response Strategy**: Detecting a virtualized environment but continuing to operate normally with sensitive functionality enabled.

## Impact

- **Compromise of Sensitive Data**: Attackers can intercept the virtualized app's files, credentials, and API calls from the hosting app, resulting in exposure of user data without requiring root access.
- **Bypass of Protection Mechanisms**: Attackers can instrument the app inside the container to defeat its client-side controls, resulting in the circumvention of its defenses on unrooted devices.
- **Compromise of System Integrity and Business Operations**: Attackers can run multiple cloned instances to abuse promotions or multi-account limits, resulting in fraud against the app owner.
- **Lack of Server-Verified Platform Attestation**: Failing to validate the app's package identity, signing certificate via hardware-backed platform attestation (e.g., Play Integrity or App Attest) on a backend server, allowing the app to execute unchecked inside virtual containers or cloned spaces.

## Mitigations

- **Detect Environment Anomalies**: Verify the app's process path, data directory, and package structure at runtime and treat mismatches as indicators of virtualization.
- **Check for Known Frameworks**: Detect artifacts of known virtualization and cloning frameworks and their hosting packages.
- **Respond to Detection**: Restrict sensitive functionality, notify the backend, or terminate when a virtualized environment is detected, according to the app's risk profile.
- **Assess Effectiveness**: Test the detection against current virtualization frameworks and update it as they evolve.
- **Attest Application Integrity**: Use platform attestation frameworks such as Play Integrity on Android or App Attest on iOS (see @MASWE-0054) with backend nonce verification to validate the official package name, signing certificate, and application integrity.
