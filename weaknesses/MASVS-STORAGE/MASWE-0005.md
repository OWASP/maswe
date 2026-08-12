---
title: Insertion of Sensitive Data into Logs
id: MASWE-0005
alias: data-in-logs
requirement: "The app excludes sensitive data from application logs."
platform: [android, ios]
profiles: [L1, L2]
threat: MAS-THREAT-0005
attacks: [MAS-ATTACK-0005, MAS-ATTACK-0006]
mappings:
  masvs-v1: [MSTG-STORAGE-7]
  masvs-v2: [MASVS-STORAGE-2]
  cwe: [209, 359, 497, 532]
  android-risks:
  - log-info-disclosure
  android-core-app-quality: [Sensitive_Data_Logging]
  maswe-beta: [MASWE-0001]
refs:
- https://developer.apple.com/documentation/os/logging/generating_log_messages_from_your_code
---

## Overview

This weakness occurs when an app writes sensitive data to system or application logs. This may include sensitive user data, such as passwords, credit card numbers, or other personally identifiable information (PII), as well as sensitive system data, such as cryptographic keys or session tokens.

Logging all possible information is very useful at development time, especially for debugging the app. However, in production it might not always be necessary and should be prevented whenever possible to avoid any accidental exposure to potential attackers.

## Modes of Introduction

- **Sensitive Data in System Logs**: Writing sensitive data to the system log via platform logging APIs, often as leftover debugging statements.
- **Sensitive Data in App Log Files**: Writing sensitive data to custom log files in the app's data directory, e.g. via third-party logging frameworks.
- **Verbose Logging in Production**: Shipping release builds with debug or verbose log levels still enabled, so diagnostic details containing sensitive data end up in production logs.

## Impact

- **Compromise of Sensitive Data**: Attackers can read passwords, credit card numbers, or PII from log output, resulting in unauthorized disclosure of user data and enabling further attacks such as identity theft.
- **Authentication or Authorization Bypass**: Attackers can reuse leaked credentials or session tokens, resulting in unauthorized access to the user's account and the app's backend services.

## Mitigations

- **Avoid Logging Sensitive Data**: Do not log sensitive data at all; treat any user or system secret as unloggable by default.
- **Redact Sensitive Data**: Where log statements are needed around sensitive values, redact or mask those values before writing them.
- **Use Log Levels Properly**: Assign debug-only details to debug or verbose levels and ensure those levels are disabled in production releases.
- **Disable Logging in Production**: Use build flags or configuration to disable logging in production releases, following the platform guidance for [Android](https://developer.android.com/privacy-and-security/risks/log-info-disclosure#mitigations) and [iOS](https://developer.apple.com/documentation/os/logging/generating_log_messages_from_your_code#3665948).
