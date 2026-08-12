---
title: Sensitive Data Leaked via Accessibility Services
id: MASWE-0040
alias: data-leak-accessibility
requirement: "The app prevents sensitive data from being exposed to, or captured by, accessibility services."
platform: [android, ios]
profiles: [L2]
threat: MAS-THREAT-0040
attacks: [MAS-ATTACK-0052]
mappings:
  masvs-v2: [MASVS-PLATFORM-3, MASVS-STORAGE-2]
  cwe: [200, 359]
refs:
- https://developer.android.com/guide/topics/ui/accessibility/service
- https://support.google.com/googleplay/android-developer/answer/10964491
- https://developer.apple.com/documentation/uikit/uiaccessibility
---

## Overview

This weakness occurs when an app exposes sensitive data to accessibility APIs beyond what is necessary, making it harvestable by malicious or overly privileged accessibility services.

Accessibility services (e.g. Android's `AccessibilityService`) can observe screen content, read the text of on-screen nodes, and receive UI events across apps. This power is essential for assistive technology, but it also makes accessibility a common exfiltration and automation vector for malware: a malicious service that the user was tricked into enabling can harvest passwords, one-time codes, messages, and other personal data, and even drive the UI. Apps handling sensitive data should minimize what is exposed through accessibility metadata without degrading accessibility for legitimate users.

## Modes of Introduction

- **Secrets in Accessibility Metadata**: Exposing sensitive values through accessibility node text, labels, or hints beyond what assistive technology needs.
- **Sensitive Fields Not Using Secure Input**: Presenting secret input in fields that are not marked as password/secure entry, so their content is readable through accessibility APIs.
- **High-Risk Flows Fully Automatable**: Designing sensitive flows (e.g. payments) so that they can be completed entirely through programmatic UI interaction without any additional verification.
- **System Keyboards Exposing Sensitive Input**: Relying on standard system keyboards for passcode or PIN entry, which allows keyboard events and typed credentials to be captured by accessibility services.

## Impact

- **Compromise of Sensitive Data**: Attackers can read messages, personal data, and financial details from on-screen content, resulting in unauthorized disclosure of user data.
- **Authentication or Authorization Bypass**: Attackers can harvest credentials and one-time codes as they are displayed or entered, resulting in account takeover.
- **Financial Loss**: Attackers can combine harvested data with accessibility-driven UI automation to initiate fraudulent transactions, resulting in direct financial harm to the user.

## Mitigations

- **Keep Secrets Out of Accessibility Metadata**: Do not place sensitive values in accessibility labels, hints, or node text beyond what assistive technology requires.
- **Use Secure Input Fields**: Mark secret fields as password/secure entry so platforms mask their content from accessibility reading.
- **Add Friction to High-Risk Flows**: Require verification that UI automation cannot satisfy (e.g. biometric-bound confirmation, see @MASWE-0020) for the most sensitive actions.
- **Preserve Legitimate Accessibility**: Minimize only the sensitive values exposed; never degrade the app's overall accessibility for assistive-technology users.
- **Use Custom Passcode Inputs**: Replace standard system keyboards with an in-app custom keypad for sensitive entry fields, preventing accessibility services from capturing or announcing typed credentials.
- **Use Custom Passcode Inputs**: Replace standard system keyboards with an in-app custom keypad for sensitive entry fields, preventing accessibility services from capturing or announcing typed credentials.
