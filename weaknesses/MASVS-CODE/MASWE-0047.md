---
title: Using Non-Standard APIs for Security-Critical Functionality
id: MASWE-0047
alias: non-standard-security-apis
requirement: "The app uses standard APIs for security-critical functionality."
platform: [android, ios]
profiles: [L1, L2]
threat: MAS-THREAT-0047
attacks: [MAS-ATTACK-0001, MAS-ATTACK-0014, MAS-ATTACK-0021]
mappings:
  masvs-v1: [MSTG-CRYPTO-2, MSTG-NETWORK-6]
  masvs-v2: [MASVS-CODE-3, MASVS-AUTH-1, MASVS-CRYPTO-1, MASVS-NETWORK-1]
  cwe: [287, 326, 327, 1240]
  android-risks:
  - bad-dns
  android-core-app-quality: [Cryptographic_Algorithms]
  maswe-beta: [MASWE-0019, MASWE-0032, MASWE-0049]
refs:
- https://developer.android.com/privacy-and-security/security-tips#Credentials
- https://developer.apple.com/documentation/security/password_autofill
- https://developer.android.com/privacy-and-security/cryptography#crypto_provider
- https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-1.pdf?__blob=publicationFile
---

## Overview

This weakness occurs when security-critical functionality, such as cryptography, networking and TLS, DNS resolution, or authentication, is implemented with custom code or unproven components instead of platform-provided APIs or established, peer-reviewed libraries.

Platform APIs and vetted libraries are designed and maintained by experts, incorporate security best practices, and receive timely updates. Custom or non-standard implementations are far more likely to contain subtle, exploitable flaws and to miss security updates. This weakness also covers failing to leverage secure functionality the platform already provides, for example using an insecure custom DNS setup instead of the platform's Private DNS / DNS-over-TLS support. It is the security-focused counterpart to @MASWE-0069, which applies the same principle from a privacy angle.

## Modes of Introduction

- **Roll-Your-Own Cryptography**: Implementing custom or non-compliant cryptography (e.g. not meeting standards such as FIPS 140-2/3), unproven algorithms, or home-grown constructions that have not undergone rigorous peer review and formal validation.
- **Custom Networking or TLS Stacks**: Rolling a custom networking/TLS stack or using outdated third-party networking libraries instead of proven APIs such as `URLSession` on iOS or `HttpsURLConnection`/OkHttp on Android.
- **Custom DNS Resolution**: Bypassing platform-provided name resolution with a custom resolver that lacks equivalent transport security, trust management, and update guarantees.
- **Custom Authentication**: Implementing custom authentication flows instead of platform-provided authentication APIs (e.g. Android Credential Manager/`AccountManager`, iOS Authentication Services / Password AutoFill).
- **Unmaintained Security Libraries**: Depending on unproven or unmaintained third-party components for security-critical functionality.

## Impact

- **Compromise of Sensitive Data**: Attackers can break weak custom cryptography or intercept traffic handled by flawed custom stacks, resulting in unauthorized disclosure or modification of sensitive data.
- **Authentication or Authorization Bypass**: Attackers can exploit logic flaws in custom authentication implementations, resulting in unauthorized access to user accounts and protected functionality.

## Mitigations

- **Use Platform Security APIs**: Prefer platform-provided functionality for cryptography, TLS, DNS, and authentication; it is expert-maintained and updated with the OS.
- **Choose Vetted, Standards-Compliant Libraries**: Where a library is needed, use established, peer-reviewed components that comply with recognized standards (e.g. FIPS 140-2/3, BSI TR-02102) and are actively maintained.
- **Never Roll Your Own Crypto or TLS**: Do not design or implement custom cryptographic algorithms, protocols, or TLS stacks for production use.
- **Leverage Secure Platform Defaults**: Use the platform's secure name resolution (e.g. Private DNS / DNS-over-TLS) and credential-management flows instead of custom substitutes.
