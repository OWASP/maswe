---
title: Insecure Intents
id: MASWE-0032
alias: insecure-intents
requirement: "The app securely handles intents."
platform: [android]
profiles: [L1, L2]
threat: MAS-THREAT-0032
attacks: [MAS-ATTACK-0047, MAS-ATTACK-0049, MAS-ATTACK-0050]
mappings:
  masvs-v2: [MASVS-PLATFORM-1, MASVS-STORAGE-2]
  cwe: [927, 940]
  android-risks:
  - implicit-intent-hijacking
  - intent-redirection
  - pending-intent
  - sender-of-pending-intents
  - sticky-broadcast
  android-core-app-quality: [Component_Permissions]
  maswe-beta: [MASWE-0066]
refs:
- https://support.google.com/faqs/answer/9267555?hl=en
- https://developer.android.com/privacy-and-security/security-tips#intents
- https://developer.android.com/topic/security/risks/intent-redirection
- https://developer.android.com/topic/security/risks/implicit-intent-hijacking
- https://developer.android.com/topic/security/risks/pending-intent
- https://developer.android.com/topic/security/risks/sticky-broadcast
---

## Overview

This weakness occurs when an app creates or handles Android intents insecurely, allowing other apps to intercept, redirect, or manipulate its communication.

Intents are Android's primary inter- and intra-app messaging mechanism. Insecure handling includes sending sensitive data via implicit intents that any matching app can receive, acting on untrusted intents and their extended data (e.g. calling `startActivity`, `startService`, `sendBroadcast`, or `setResult` on intents received from other apps) without validation, creating PendingIntents that other apps can modify or replay, and using sticky broadcasts, which any app can read and replace.

## Modes of Introduction

- **Implicit Intents for Internal Communication**: Using implicit intents, which any matching app can receive, for internal app communication or for carrying sensitive extras.
- **Intent Redirection**: Extracting a nested intent from untrusted extras and forwarding it (e.g. via `startActivity`) without validating its destination, letting other apps reach the app's non-exported components.
- **Mutable PendingIntents**: Creating PendingIntents without `FLAG_IMMUTABLE`, allowing the receiving app to modify the underlying intent and execute it with the app's identity.
- **Replayable PendingIntents**: Creating one-off PendingIntents without `FLAG_ONE_SHOT`, allowing them to be reused.
- **Sticky Broadcasts**: Using [sticky broadcasts](https://developer.android.com/privacy-and-security/risks/sticky-broadcast), which remain accessible after delivery and can be read or replaced by any app.

## Impact

- **Compromise of Sensitive Data**: Attackers can receive sensitive extras carried in implicit intents or broadcasts, resulting in unauthorized disclosure of user or app data to other apps.
- **Authentication or Authorization Bypass**: Attackers can reach non-exported components through intent redirection or execute actions with the app's identity through manipulated PendingIntents, resulting in privileged operations performed on the attacker's behalf.

## Mitigations

- **Use Explicit Intents Internally**: Address internal communication to explicit component targets so no other app can receive it, and never place sensitive data in implicit intents.
- **Validate Redirected Intents**: Before forwarding a nested intent from untrusted input, validate its destination against an allowlist and strip unexpected flags.
- **Create Immutable, Explicit PendingIntents**: Build PendingIntents with `FLAG_IMMUTABLE` over explicit base intents, and add `FLAG_ONE_SHOT` where a single use is intended.
- **Avoid Sticky Broadcasts**: Use regular broadcasts protected with permissions, or more targeted mechanisms, instead of deprecated sticky broadcasts.
-**Validate Incoming Intent Data**: Treat all extended intent data entering the app through exported components as untrusted. Validate it before further processing (@MASWE-0050).
