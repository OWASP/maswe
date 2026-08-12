---
title: Lack of Authentication or Authorization on App Components
id: MASWE-0018
alias: missing-auth-app-components
requirement: "The app enforces authentication and authorization on its components."
platform: [android, ios]
profiles: [L1, L2]
threat: MAS-THREAT-0018
attacks: [MAS-ATTACK-0038, MAS-ATTACK-0039]
mappings:
  masvs-v1: [MSTG-PLATFORM-4, MSTG-AUTH-3, MSTG-NETWORK-2, MSTG-STORAGE-6]
  masvs-v2: [MASVS-AUTH-1, MASVS-PLATFORM-1, MASVS-STORAGE-2]
  cwe: [306, 749, 862, 863, 923, 926, 939, 940]
  android-risks:
  - content-resolver
  - insecure-broadcast-receiver
  - access-control-to-exported-components
  - android-exported
  - custom-permissions
  android-core-app-quality: [Component_Export, Component_Permissions, Component_Protection]
  maswe-beta: [MASWE-0033, MASWE-0038, MASWE-0040, MASWE-0051, MASWE-0059, MASWE-0062, MASWE-0063, MASWE-0064, MASWE-0065, MASWE-0119]
refs:
- https://developer.android.com/privacy-and-security/security-tips#IPNetworking
- https://developer.android.com/privacy-and-security/security-tips#Services
- https://developer.android.com/privacy-and-security/security-tips#BroadcastReceivers
- https://developer.android.com/privacy-and-security/security-tips#ContentProviders
- https://developer.android.com/privacy-and-security/security-tips#binder-and-messenger-interfaces
- https://developer.android.com/topic/security/risks/content-resolver
- https://developer.android.com/topic/security/risks/file-providers
---

## Overview

This weakness occurs when app components that expose functionality or data do not enforce proper authentication or authorization on their callers.

It covers any component reachable by other apps or processes without adequate access control, including services, broadcast receivers, activities, and content providers, as well as local web services or open ports exposed by the app. It also covers the handling of authentication material on such surfaces, for example authentication tokens accepted without validation or authentication flows handled insecurely inside WebViews.

## Modes of Introduction

- **Unintentionally Exported Components**: Exporting services, broadcast receivers, activities, or content providers through defaults or misconfiguration when they are only meant for internal use.
- **Missing or Weak Permissions on Exported Components**: Exporting components without permission requirements, with weak protection levels, or with misconfigured custom permissions.
- **Caller Not Verified on IPC Interfaces**: Exposing Binder or Messenger interfaces that do not verify the caller's identity or permissions (e.g. not calling `checkCallingPermission()`).
- **Over-Broad Data Grants**: Using sticky broadcasts, over-broad or persistable URI permission grants, or persistent data sharing where one-time, scoped sharing would suffice.
- **Unprotected Local Network Services**: Binding a local web service or open port that accepts connections without authentication.
- **Authentication Material Not Validated**: Accepting authentication tokens without proper validation (e.g. missing signature or claim checks, no PKCE in OAuth flows) or handling authentication inside WebViews instead of secure system flows.
- **Missing Authentication or Authorization on Deep Links**: App-defined URI scheme, Android App Link, or iOS Universal Link triggers a sensitive action (e.g., password reset, fund transfer, account linking) without verifying that the request came from an authenticated or authorized source.

## Impact

- **Compromise of Sensitive Data**: Attackers can query unprotected content providers or receive broadcast data, resulting in unauthorized disclosure of user or app data to other apps on the device.
- **Authentication or Authorization Bypass**: Attackers can invoke privileged functionality, such as internal services or unvalidated token flows, without authenticating, resulting in actions being executed on behalf of the user.
- **Bypass of Protection Mechanisms**: Attackers can launch internal activities directly, resulting in the circumvention of intended flows such as authentication screens or paywalls.

## Mitigations

- **Do Not Export Components Unnecessarily**: Explicitly mark internal components as not exported and keep the exposed surface minimal.
- **Protect Exported Components with Permissions**: Guard intentionally exported components with permissions of an appropriate protection level (e.g. signature-level for same-developer apps) and define custom permissions correctly.
- **Verify Callers on IPC Interfaces**: Check the caller's identity or permissions on Binder and Messenger interfaces before performing sensitive operations or returning data.
- **Grant Minimal, Short-Lived Data Access**: Prefer one-time, narrowly scoped URI grants over persistable ones, avoid sticky broadcasts, and restrict content provider paths to exactly what must be shared.
- **Authenticate Local Services**: Avoid opening local ports where possible; if required, authenticate every connection and bind only to the local interface.
- **Validate Authentication Material**: Validate tokens server-side (signature, issuer, audience, expiry), use PKCE for OAuth flows, and use system-provided authentication sessions instead of handling credentials inside WebViews.
