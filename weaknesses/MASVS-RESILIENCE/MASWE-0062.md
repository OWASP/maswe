---
title: No Application-Level Payload Encryption
id: MASWE-0062
alias: data-unencrypted
requirement: "The app applies application-level payload encryption in addition to transport-layer encryption."
platform: [android, ios]
profiles: [R]
threat: MAS-THREAT-0062
attacks: [MAS-ATTACK-0064]
mappings:
  masvs-v1: [MSTG-RESILIENCE-13]
  masvs-v2: [MASVS-RESILIENCE-3, MASVS-NETWORK-1]
  cwe: [319]
  maswe-beta: [MASWE-0096]
---

## Overview

This weakness occurs when an app relies solely on transport-layer encryption for its network traffic, without an additional layer of application-level payload encryption.

Even when the connection uses HTTPS, an attacker who controls the device can bypass transport protections (for example by defeating certificate pinning with instrumentation) and observe or tamper with the plaintext payloads, revealing the inner workings of the app and its API. Application-level payload encryption raises the effort required to analyze and manipulate the app's traffic. This is a resilience measure aimed at hindering analysis and abuse; it complements rather than replaces transport security (see @MASWE-0026, @MASWE-0028).

## Modes of Introduction

- **TLS-Only Protection**: Sending security-relevant API payloads with no protection beyond the transport channel, so they appear in plaintext as soon as TLS is intercepted on a controlled device.
- **No Integrity Binding on Requests**: Not signing or otherwise binding sensitive requests, so intercepted payloads can be modified and replayed once the transport layer is bypassed.

## Impact

- **Compromise of System Integrity and Business Operations**: Attackers can map the app's API and craft or tamper with requests, resulting in fraud, scraping, and abuse of backend services at the app owner's expense.
- **Bypass of Protection Mechanisms**: Attackers can easily modify payloads that carry security-relevant state, without having to reverse-engineer the application to first circumvent the additional encryption.

## Mitigations

- **Encrypt Sensitive Payloads at the Application Layer**: Apply an additional layer of encryption to security-relevant payloads before they enter the transport channel, using keys managed via the platform keystore.
- **Sign Security-Relevant Requests**: Authenticate and integrity-protect sensitive requests (e.g. with signatures bound to attested, hardware-backed keys) so tampered payloads are rejected server-side.
- **Treat It as Defense in Depth**: Keep full transport security (TLS and pinning) in place; application-level encryption raises analysis effort but is still client-side and ultimately bypassable.
