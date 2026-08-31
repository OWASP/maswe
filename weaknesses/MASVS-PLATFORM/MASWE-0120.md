---
title: Sensitive Data Leaked via Outgoing Inter-App Communication
id: MASWE-0120
alias: data-leak-outgoing-ipc
platform: [android, ios]
profiles: [L1, L2]
mappings:
  masvs-v2: [MASVS-PLATFORM-1, MASVS-STORAGE-2]
  cwe: [200, 668, 927]
refs:
- https://developer.android.com/privacy-and-security/security-tips#intents
- https://developer.android.com/topic/security/risks/implicit-intent-hijacking
- https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app
- https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app
status: new

---

## Overview

Mobile apps frequently launch other apps and pass them data through an inter-app communication channel. On Android this is commonly an [implicit `Intent`](https://developer.android.com/privacy-and-security/security-tips#intents) (with data in its extras, action, or data URI) sent through `startActivity`, `startActivityForResult`, `sendBroadcast`, or `setResult`. On iOS this is commonly a custom URL scheme or universal link opened with [`open(_:options:completionHandler:)`](https://developer.apple.com/documentation/uikit/uiapplication/1648685-open) (with data carried in the URL's host, path, or query).

The defining property of these channels is that the **sending app does not control which app ultimately receives the data**. The system resolves the recipient: an implicit Intent can be delivered to any app declaring a matching intent filter, and a custom URL scheme can be claimed by any installed app. Even universal links, which are bound to a verified domain, give the sender no guarantee about the web or app context that ultimately handles the request.

This weakness occurs when an app places sensitive data, such as authentication tokens, session identifiers, passwords, or personally identifiable information, into one of these outgoing messages. A malicious or merely unexpected app that receives the message gains access to that data.

This weakness concerns the **sending** side of inter-app communication. The receiving side, where an app fails to validate or restrict incoming deep links, is covered by MASWE-0058. Persistent file or content sharing through content providers and shared storage is covered by MASWE-0065, and unauthenticated IPC channels such as the clipboard or localhost sockets are covered by MASWE-0059. On Android, the broader misuse of the Intent system (implicit Intent hijacking, Intent redirection, and insecure `PendingIntent`s) is covered by MASWE-0066.

## Impact

- **Disclosure of sensitive data to unauthorized apps**: any app able to receive the outgoing message can read the transmitted data, leading to account takeover, session hijacking, or privacy violations.
- **Interception and tampering**: an attacker-controlled app that registers for the same scheme, action, or intent filter can silently collect the data, and may relay a modified request onward.

## Modes of Introduction

- **Android**: populating an implicit `Intent` with sensitive extras or a sensitive data URI and dispatching it via `startActivity`, `startActivityForResult`, `sendBroadcast`, or returning it via `setResult`, instead of using an explicit `Intent` targeted at a specific component or another secure IPC mechanism.
- **iOS**: building a custom URL scheme or universal link URL that embeds sensitive data and opening it in another app with `open(_:options:completionHandler:)` (or the deprecated `openURL:options:completionHandler:`).
- Logging or analytics flows that mirror an outgoing inter-app URL or Intent, re-exposing the same sensitive data.

## Mitigations

- Do not place sensitive data in outgoing inter-app messages whose recipient is system-resolved. Transmit sensitive data only over channels with an authenticated, explicitly identified recipient (for example, an Android explicit `Intent` targeting a known component, or a backend connection with proper transport security).
- When data must be handed to another app, pass a short-lived, single-use reference (such as an opaque handle redeemable over an authenticated channel) rather than the sensitive value itself.
- Minimize the data included in any outgoing URL or Intent to what is strictly required for routing.

For platform-specific guidance, see the MASTG best practices linked from the corresponding tests.
