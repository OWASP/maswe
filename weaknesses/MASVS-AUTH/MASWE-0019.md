---
title: Lack of Auto-fill Support for Credential Providers
id: MASWE-0019
alias: autofill-authenticators
requirement: "The app enables auto-fill support for credential providers."
platform: [android, ios]
profiles: [L1, L2]
threat: MAS-THREAT-0019
attacks: [MAS-ATTACK-0041, MAS-ATTACK-0042]
mappings:
  masvs-v1: [MSTG-AUTH-9]
  masvs-v2: [MASVS-AUTH-1, MASVS-AUTH-3]
  cwe: [287, 522]
  android-core-app-quality: [Autofill_Hints, Credential_Manager]
  maswe-beta: [MASWE-0028, MASWE-0032, MASWE-0035, MASWE-0039]
refs:
- https://developer.apple.com/documentation/security/password_autofill
- https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession
- https://developer.android.com/guide/topics/text/autofill
- https://developer.apple.com/documentation/authenticationservices/public-private_key_authentication/supporting_passkeys
---

## Overview

This weakness occurs when an app does not support the platform's auto-fill and credential-management mechanisms, pushing users toward insecure workarounds such as copying and pasting credentials between apps.

Platforms provide secure flows for supplying credentials, one-time codes, and passkeys: credential and one-time-code auto-fill, Password AutoFill tied to the app's associated domain, system authentication sessions for third-party services, passwordless authentication with passkeys and WebAuthn, and shared web credentials between an app and its website counterpart. When an app ignores these mechanisms, users end up typing or copying secrets manually, weakening both their credentials and the trust boundary they cross.

## Modes of Introduction

- **No Auto-Fill Support in Credential Fields**: Building login fields that are not recognized by or are incompatible with the platform's auto-fill framework and password managers.
- **No One-Time-Code Auto-Fill**: Requiring users to manually read and copy one-time codes (e.g. from SMS) instead of supporting the platform's code auto-fill.
- **Missing Website Association**: Not associating the app with its domain, preventing frictionless secure credential sharing between the app and its website counterpart.
- **Embedded Custom Login Instead of System Flows**: Handling custom authentication, such as using third-party logins in embedded views, instead of system-provided authentication sessions (e.g. `ASWebAuthenticationSession`).
- **No Support for Passwordless Authentication**: Not offering passkeys or other multi-device FIDO/WebAuthn credentials where they could replace passwords.

## Impact

- **Authentication or Authorization Bypass**: Attackers can reuse captured credentials or one-time codes, resulting in account takeover and unauthorized access to the user's data and functionality.
- **Compromise of Sensitive Data**: Attackers can read credentials exposed through clipboard-based workarounds, resulting in disclosure of authentication material that protects sensitive information.

## Mitigations

- **Support Platform Auto-Fill**: Annotate credential fields so the platform's auto-fill framework and password managers can fill them securely (e.g. autofill hints on Android, `textContentType` on iOS).
- **Support One-Time-Code Auto-Fill**: Use the platform mechanisms that deliver one-time codes directly into the app, removing the need for manual copying.
- **Associate the App with Its Domain**: Configure website association (e.g. iOS Password AutoFill with associated domains, shared web credentials) so credentials flow securely between the app and its website.
- **Use System Authentication Sessions for Third-Party Logins**: Authenticate against third-party services with system flows such as `ASWebAuthenticationSession` instead of embedded views.
- **Support Passkeys**: Offer passkeys or other WebAuthn-based passwordless authentication to remove shared secrets from the login flow entirely.
