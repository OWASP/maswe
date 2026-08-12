---
title: Usage of Non-Privacy-Preserving Functionality
id: MASWE-0069
alias: non-privacy-preserving-functionality
requirement: "The app uses privacy-preserving functionality."
platform: [android, ios]
profiles: [P]
threat: MAS-THREAT-0069
attacks: [MAS-ATTACK-0076, MAS-ATTACK-0088]
mappings:
  masvs-v2: [MASVS-PRIVACY-2]
  cwe: [359]
  android-core-app-quality: [Minimize_Permissions]
refs:
- https://datatracker.ietf.org/doc/html/rfc8252#appendix-B
- https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession
- https://developer.android.com/training/data-storage/shared/photopicker
- https://developer.apple.com/documentation/photokit/phpickerviewcontroller
---

## Overview

This weakness occurs when an app uses functionality that unnecessarily exposes user data even though the platform provides a privacy-preserving alternative.

Platforms increasingly offer least-exposing APIs for common tasks: system authentication sessions (ASWebAuthenticationSession on iOS and Custom Tabs on Android, as recommended by RFC 8252, Appendix B) keep credentials and browsing state isolated from the app; system pickers (e.g., PHPickerViewController on iOS and the Android Photo Picker) return only the items selected by the user without granting broad permissions; and on-device processing can avoid sending data to remote AI services. Choosing a less privacy-preserving option leads to avoidable data exposure and over-collection. This is the privacy-focused counterpart to @MASWE-0047, which applies the same "prefer platform-provided functionality" principle from a security perspective; some features, such as system authentication sessions, improve both security and privacy.

## Modes of Introduction

- **Embedded Authentication Flows**: Handling third-party authentication in embedded WebViews or deprecated session APIs, exposing credentials and browsing state to the app, instead of isolated system authentication sessions.
- **Broad Permissions Instead of Pickers**: Requesting full photo-library, camera, or file access when a system picker would return only the user-selected items without any permission.
- **Remote Processing Instead of On-Device AI**: Sending user data to remote AI services when on-device processing can support the feature.
- **Over-Exposing API Choices**: Choosing APIs that reveal more user data than the feature requires when a least-exposing platform alternative exists (see also @MASWE-0066).

## Impact

- **Violation of User Privacy**: The app and its embedded components can collect and correlate credentials, browsing state, or whole data collections that a privacy-preserving alternative would never have exposed, resulting in tracking, surveillance, or profiling of the user.
- **Compromise of Sensitive Data**: The app and its embedded components can retain data that a privacy-preserving alternative would not expose, resulting in broader exposure when the app or a third-party service suffers a data breach.
- **Loss of User Trust**: Users can perceive unnecessary permission prompts and embedded login flows as invasive, resulting in refused permissions, abandoned logins, and reduced retention.

## Mitigations

- **Use System Authentication Sessions**: Authenticate against third-party services with `ASWebAuthenticationSession` on iOS or Custom Tabs on Android, following RFC 8252, instead of embedded WebViews or deprecated APIs.
- **Prefer System Pickers**: Use the system photo, file, and contact pickers so the app receives only what the user explicitly selects, without broad permission grants.
- **Prefer On-Device Processing**: Use on-device AI or other local processing when it can support the feature without sending user data to a remote service.
- **Choose Least-Exposing APIs**: When the platform offers a privacy-preserving variant of a capability, prefer it and request broad access only when the feature genuinely requires it (see @MASWE-0066).
