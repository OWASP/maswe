---
title: Insecure Identity Pinning
id: MASWE-0028
alias: insecure-pinning
requirement: "The app correctly implements identity pinning."
platform: [android, ios]
profiles: [L2]
threat: MAS-THREAT-0028
attacks: [MAS-ATTACK-0014, MAS-ATTACK-0016, MAS-ATTACK-0017]
mappings:
  masvs-v1: [MSTG-NETWORK-4]
  masvs-v2: [MASVS-NETWORK-2]
  cwe: [295]
  android-core-app-quality: [Network_Security_Configuration]
  maswe-beta: [MASWE-0047]
refs:
- https://developer.android.com/privacy-and-security/security-config#CertificatePinning
- https://developer.apple.com/news/?id=g9ejcf8y
- https://cheatsheetseries.owasp.org/cheatsheets/Pinning_Cheat_Sheet.html
---

## Overview

This weakness occurs when identity pinning (also known as certificate pinning, public key pinning, or TLS pinning) is not implemented, or is implemented incorrectly, so the app cannot guarantee that it only communicates with servers presenting a specific, pre-determined cryptographic identity.

Identity pinning associates a mobile app with a specific certificate or public key, adding a layer of trust verification on top of standard certificate validation. This reduces the risk of unauthorized interception even if a trusted Certificate Authority (CA) is compromised. Compromise of a public CA is rare, but pinning narrows trust to identities the app operator controls, and raises the effort required to intercept, inspect, or replay the app's traffic.

Pinning is not foolproof: attackers who can reverse-engineer the app may remove or modify the pre-defined pins or the pinning logic, and attackers using runtime hooking and dynamic instrumentation may bypass the pinning checks on a device they control. This highlights the importance of implementing pinning **alongside other security measures** to enhance the app's resistance to advanced threats.

## Modes of Introduction

- **Improper Configuration of Pinning Libraries**: Misconfiguring libraries like TrustKit or OkHttp's `CertificatePinner` leading to ineffective pinning.
- **Dynamic Pinning without Security**: Retrieving pins dynamically over insecure channels without proper validation.
- **Improper Validation Logic**: Implementing custom pinning logic that does not correctly validate the certificate chain or public key. For example, accepting any certificate that chains to a trusted root CA instead of a specific certificate or public key.
- **Lack of Backup Pins**: Not including backup pins, so the app cannot establish connections if the primary pin is no longer valid.

## Impact

- **Compromise of Sensitive Data**: Attackers can capture, read, or alter sensitive information transmitted over the network, resulting in unauthorized disclosure or manipulation of user data.
- **Authentication or Authorization Bypass**: Attackers can capture credentials or session tokens in transit, resulting in user impersonation and unauthorized access to accounts or backend systems.
- **Compromise of System Integrity and Business Operations**: Attackers can inspect and reverse engineer the app's API traffic to abuse backend services, resulting in fraud, scraping, or service abuse against the app owner.

## Mitigations

- **Prefer Platform-Provided Solutions**: Use platform-provided mechanisms like Android's Network Security Configuration (NSC) or iOS's App Transport Security (ATS) to enforce pinning.
- **Use Trusted Pinning Libraries**: Refrain from writing custom pinning logic; instead, rely on established and well-maintained libraries and frameworks (e.g., TrustKit, OkHttp's `CertificatePinner`) and ensure they are correctly configured according to best practices.
- **Secure Dynamic Pinning**: If dynamic pinning is necessary, retrieve pins over secure channels and validate them thoroughly before use.
- **Pin to Public Keys Instead of Certificates**: Pin to the certificate's public key rather than the whole certificate to avoid issues regarding expiration and renewals.
- **Enforce Pinning Consistently**: Apply pinning uniformly for all connections to servers that you control.
- **Regularly Update Pins**: Keep the pinned certificates or public keys up to date with the server's current configuration and have a process for updating the app when changes occur.
- **Implement Backup Pins**: Include backup pins (hashes of additional trusted public keys) to prevent connectivity issues if the primary key changes.
