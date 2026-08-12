---
title: Insecure Certificate Validation
id: MASWE-0027
alias: insecure-cert-validation
requirement: "The app validates certificates for all network traffic."
platform: [android, ios]
profiles: [L1, L2]
threat: MAS-THREAT-0027
attacks: [MAS-ATTACK-0014, MAS-ATTACK-0015]
mappings:
  masvs-v1: [MSTG-NETWORK-3]
  masvs-v2: [MASVS-NETWORK-1]
  cwe: [295, 297]
  android-risks:
  - unsafe-trustmanager
  - unsafe-hostname
  android-core-app-quality: [Network_Security_Configuration, Security_Provider_Initialization]
  maswe-beta: [MASWE-0052]
refs:
- https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-52r2.pdf#page=17
- https://developer.android.com/privacy-and-security/security-ssl#tls-1.3-enabled-by-default
- https://support.google.com/faqs/answer/7071387?hl=en
- https://developer.android.com/reference/android/webkit/WebViewClient.html?sjid=15211564825735678155-EU#onReceivedSslError(android.webkit.WebView,%20android.webkit.SslErrorHandler,%20android.net.http.SslError)
- https://developer.android.com/privacy-and-security/security-ssl#WarningsSslSocket
- https://developer.apple.com/forums/thread/67493
- https://developer.apple.com/forums/thread/707320
- https://support.apple.com/en-us/102390
- https://developer.apple.com/documentation/foundation/performing-manual-server-trust-authentication
---

## Overview

This weakness occurs when an app does not properly validate TLS certificates during secure communication, accepting invalid, expired, self-signed, or untrusted certificates without appropriate verification.

Certificate validation is the mechanism through which a TLS client establishes that it is talking to the intended server and not to an intermediary. When it is disabled, weakened, or implemented incorrectly, the confidentiality and integrity guarantees of TLS no longer hold, even though the connection itself is encrypted.

## Modes of Introduction

- **Disabling Certificate Validation**: Disabling or bypassing certificate validation checks to simplify development or troubleshoot connectivity issues, and shipping that configuration to production.
- **Accepting Self-Signed Certificates**: Accepting self-signed or untrusted certificates without proper validation against trusted Certificate Authorities (CAs).
- **Ignoring Hostname Verification**: Failing to verify that the certificate's hostname matches the server's hostname.
- **Using Insecure Custom Trust Managers**: Implementing custom certificate validation logic that is incomplete, incorrect, or insecure.
- **Incorrect Error Handling**: Proceeding with connections even when certificate validation errors occur, without alerting the user or terminating the connection.
- **Third-Party Libraries**: Using third-party libraries or SDKs that disable or weaken certificate validation internally, or that default to permissive trust settings.

## Impact

- **Compromise of Sensitive Data**: Attackers can capture, read, or alter sensitive information transmitted over the network, resulting in unauthorized disclosure or manipulation of user data.
- **Authentication or Authorization Bypass**: Attackers can capture credentials or session tokens in transit, resulting in user impersonation and unauthorized access to accounts or backend systems.
- **Compromise of System Integrity and Business Operations**: Attackers can impersonate legitimate servers and feed altered or malicious data to the app, resulting in unreliable or malicious app behavior and reputational damage for the app owner.
- **Legal and Regulatory Non-Compliance**: Attackers can capture personal data in transit, resulting in reportable breaches and regulatory penalties for the app owner under laws such as GDPR or HIPAA.

## Mitigations

- **Enforce Strict Certificate Validation**: Always validate TLS certificates against a trusted set of Certificate Authorities (CAs) provided by the operating system or a trusted third party.
- **Avoid Accepting Self-Signed Certificates**: Do not accept self-signed or untrusted certificates in production environments unless there is a secure mechanism to trust them explicitly.
- **Enable Hostname Verification**: Ensure that the application's network layer verifies the server's hostname against the certificate's Subject Alternative Name (SAN) or Common Name (CN).
- **Use Standard Trust Managers**: Utilize well-established libraries and platform-provided APIs for certificate validation instead of custom implementations.
- **Handle Validation Errors Properly**: Terminate the connection and alert the user whenever certificate validation fails due to issues like expiration, revocation, or mismatch.
