---
title: Authenticators Hardcoded in the App Package
id: MASWE-0005
alias: authenticators-hardcoded-app-package
platform: [android, ios]
profiles: [L1, L2]
mappings:
  masvs-v2: [MASVS-AUTH-1]
  mastg-v1: []
  cwe: [798]
  android-risks:
  - https://developer.android.com/privacy-and-security/risks/insecure-api-usage
status: new
refs:
- https://cloud.google.com/docs/authentication/api-keys#securing
- https://cloud.google.com/docs/authentication/api-keys#api_key_restrictions
- https://www.youtube.com/watch?v=4enjKo2hQMY
- https://bughunters.google.com/learn/invalid-reports/google-products/5222475159961600/understanding-api-key-leaks
- https://firebase.google.com/support/guides/security-checklist#api-keys-not-secret
---

## Overview

Hardcoding authenticators—such as API keys, tokens, passwords, or private keys—into a mobile app package makes them trivially retrievable through static or dynamic analysis. When these authenticators provide access to protected resources, backend services, or user data, their exposure contradicts [NIST SP 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html) guidance, which requires authenticator secrets to be safeguarded against disclosure.

However, not all keys found in an app are inherently sensitive. Many third-party services (e.g., Google Maps, Firebase, analytics providers) intentionally rely on **public client-side API keys** that act only as identifiers. These keys are expected to appear in mobile applications and are **not considered secrets**, provided they do not grant access to user data and are properly usage-restricted. For example, Firebase explicitly states that its client API keys "are not secret" and "are not used for authorization", and Google VRP does not accept reports of leaked `AIza` public API keys unless exploitability is demonstrated.

This weakness therefore focuses on cases where the embedded authenticator **should have been kept secret**, or where a supposedly public key is **missing required usage restrictions** that prevent abuse.

## Impact

Hardcoding sensitive or misconfigured authenticators can result in:

- **Financial Loss**: Keys tied to billable services (e.g., AI/ML APIs, cloud compute, SMS/email gateways) can be abused for unauthorized API consumption, leading to unexpected operational costs.
- **Unauthorized Access to Data or Services**: Exposure of secret authenticators (e.g., Firebase FCM **server keys**, service account **private keys**, backend **API keys with write privileges**, OAuth **client secrets**, payment processor **secret keys**) may allow attackers to impersonate the app, access protected user data, or perform privileged operations.
- **App Integrity and Business Operations Risks**: Attackers may leverage hardcoded secrets to perform actions that disrupt services (e.g., DoS through quota exhaustion or policy violations), manipulate backend content, or circumvent feature-gating, harming user trust and business reputation.
- **Bypassing Protection Mechanisms**: Weakly protected or unprotected client-side keys may enable attackers to bypass feature restrictions, unlock premium features, or tamper with application logic.

## Modes of Introduction

Hardcoded authenticators may appear in:

- **App Source Code**: directly embedded in code or configuration files.
- **App Assets**: included in manifests, resource files, `google-services.json`, plist files, or other bundled assets.
- **Libraries**: present in third-party SDKs, first-party modules, or included build-time dependencies.

## Mitigations

- Use a **stateful authentication model** (e.g., OAuth 2.0, short-lived tokens) so sensitive operations require server-issued, time-bound credentials rather than static client-side keys.
- If a stateful model is not possible, use an **API gateway or proxy**. Keep sensitive keys server-side and expose only scoped, temporary tokens (e.g., JWTs or signed requests) to the client.
- If an API key must reside in the client, ensure:
    - It has **minimal permissions**.
    - It is **restricted** by package name, SHA-1 signature, domain, IP, or allowed API list.
    - It **cannot** grant access to user data.
- Consider using a **Key Management Service (KMS)** to retrieve sensitive credentials at runtime only after verifying app integrity (e.g., device attestation or RASP signals).
- Audit source code and dependencies for hardcoded secrets (e.g., with tools like `gitleaks` or CI secret scanners).
- Apply **white-box cryptography** or **RASP** solutions when no stronger architectural alternative is possible, ensuring secrets are split, obfuscated, or constructed only in memory at runtime.
- Use **code and resource obfuscation** as a last resort to increase the difficulty of reverse engineering, but never as a primary protection mechanism.
