---
title: Sensitive Data Hardcoded in the App Package
id: MASWE-0004
alias: data-hardcoded-app-package
requirement: "The app does not hardcode sensitive data in the application package."
platform: [android, ios]
profiles: [L1, L2, EUDIW]
threat: MAS-THREAT-0004
attacks: [MAS-ATTACK-0001]
mappings:
  masvs-v1: [MSTG-STORAGE-1, MSTG-CODE-2]
  masvs-v2: [MASVS-STORAGE-1]
  cwe: [312, 321, 540, 798]
  android-risks:
  - insecure-api-usage
  maswe-beta: [MASWE-0005, MASWE-0013, MASWE-0036]
refs:
- https://cloud.google.com/docs/authentication/api-keys#securing
- https://cloud.google.com/docs/authentication/api-keys#api_key_restrictions
- https://firebase.google.com/docs/projects/api-keys
- https://github.com/OWASP/ASVS/blob/master/5.0/en/0x16-V7-Session-Management.md
- https://github.com/OWASP/ASVS/blob/master/5.0/en/0x17-V8-Authorization.md
- https://github.com/OWASP/ASVS/blob/master/5.0/en/0x19-V10-OAuth-and-OIDC.md
- https://datatracker.ietf.org/doc/html/rfc8252#section-8.5
- https://api-security.owasp.org/editions/2023/en/0x11-t10/
- https://github.com/gitleaks/gitleaks
---

## Overview

This weakness occurs when sensitive data is embedded in the app package (APK/IPA) and shipped with the app, where anyone who downloads the package can recover it.

The hardcoded sensitive data may include API keys and secrets for first- or third-party services, credentials such as passwords or session tokens, and cryptographic material such as symmetric or private keys embedded directly in the package (as opposed to being generated and stored in a platform keystore, see @MASWE-0003). It also includes developer leftover artifacts, such as staging or integration URLs, developer emails and usernames, and source code files left in the package (e.g. `.swift`, `.cpp`, map files, or other build artifacts) that leak internal information.

Not all API keys embedded in an app package are sensitive. Some are public identifiers that a service issues for use in distributed clients. A key that lets anyone holding it reach protected resources or privileged functionality, such as billed APIs or the app owner's data, is sensitive, and embedding it is a weakness. Whether a key is sensitive depends on the permissions and restrictions the remote service associates with it. Authorization weaknesses in the remote service itself should be assessed using the OWASP ASVS and the OWASP API Security Top 10.

Note that developer _debug_ artifacts (verbose logging, backdoors, testing utilities, hidden switches) are covered separately under resilience in @MASWE-0061. The focus here is on hardcoded sensitive data that leaks confidentiality regardless of any anti-tampering considerations.

## Modes of Introduction

- **App Source Code**: Embedding secrets directly in the code that is compiled into the app.
- **App Assets and Resources**: Including secrets in configuration files, manifests, property lists, string resources, and other bundled files.
- **Libraries**: Including secrets in the configuration files or source code of first-party, third-party, or transitive dependencies.
- **Build and Developer Leftovers**: Inadvertently packaging staging/integration endpoints, developer identities, and source files with the app.

## Impact

- **Financial Loss**: Attackers can abuse compromised API keys to make unauthorized billed API calls (e.g., AI/ML services), resulting in unexpected charges to the app owner.
- **Compromise of System Integrity and Business Operations**: Attackers can use extracted credentials to access backend services, resulting in service disruption, policy-violation suspensions, or denial of service.
- **Compromise of Sensitive Data**: Attackers can use extracted cryptographic material to decrypt protected data, resulting in unauthorized disclosure of user or app data.
- **Bypass of Protection Mechanisms**: Attackers can use hardcoded keys to unlock paid features or access restricted content, resulting in circumvention of the protections the app enforces.

## Mitigations

- **Proxy Static Secrets Through a Middleware**: If a stateful API service is not viable, front the stateless API with a middleware solution (API proxy or gateway) that proxies requests between the app and the API endpoint, keeping the static secret server-side rather than in the client. Use JSON Web Tokens (JWT) and JSON Web Signature (JWS) as appropriate.
- **Use Stateful API Services**: Prefer API services that provide secure authentication, client validation, and session controls. Implement dynamic tokens that expire after a reasonably short time (e.g., 1 hour) to reduce the impact of key exposure, and ensure proper error handling and logging to detect unauthorized access attempts. Consider OAuth 2.0 and libraries such as AppAuth to simplify secure OAuth flows.
- **Issue Per-Installation Credentials**: Have the backend issue short-lived credentials per installation, and per user where the app has accounts, instead of one shared secret that can be extracted from any device. Bind them to a key in the platform keystore where possible (see @MASWE-0003), and enforce quotas and revocation at the same scope so abuse can be traced and blocked.
- **Restrict Unavoidable Hardcoded Keys**: Treat any key shipped with the app as public. Limit it to the APIs and operations any anonymous client may use, be prepared to revoke and reissue it, and do not rely on app-declared identifiers such as package name or bundle identifier, which any client can send.
- **Use Platform Keystores**: Store cryptographic keys and authentication material using the platform's hardware-backed keystore (Android Keystore, iOS Keychain) instead of embedding them in the package. See @MASWE-0003.
- **Audit for Leftover Secrets**: Regularly audit the codebase and dependencies for hardcoded sensitive data and developer leftovers (e.g., using tools such as [gitleaks](https://github.com/gitleaks/gitleaks)) and strip build artifacts and source files from release packages.
- **Harden Only as a Last Resort**: When no other secure option is available, use white-box cryptography, code/resource obfuscation, and RASP to raise the effort required to extract secrets, ensuring keys are only assembled in memory when needed. These techniques deter but do not prevent extraction and must not replace the mitigations above.
