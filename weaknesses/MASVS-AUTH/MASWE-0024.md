---
title: Sensitive Data Accessible After Session Termination
id: MASWE-0024
alias: session-termination
requirement: "The app makes sensitive data inaccessible after session termination."
platform: [android, ios]
profiles: [L2]
threat: MAS-THREAT-0024
attacks: [MAS-ATTACK-0005, MAS-ATTACK-0032, MAS-ATTACK-0033]
mappings:
  masvs-v2: [MASVS-AUTH-3]
  cwe: [285, 287, 613]
  maswe-beta: [MASWE-0030]
refs:
- https://developer.android.com/identity/sign-in/credential-manager-siwg-implementation#handle-sign-out
- https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
---

## Overview

This weakness occurs when sensitive data or an authenticated session remains accessible after the session should have ended, whether through explicit logout, a timeout, or a contextual state change.

Session termination is not limited to the user tapping "log out": inactivity timeouts, the app moving to the background, or remarkable changes in the user's context (such as location or profile changes) can all require the session to end or the user to re-authenticate. When the app fails to invalidate the session and clear the associated sensitive data (session tokens, cached personal data, in-memory state, on-screen content), anyone who gains access to the device or the leftover tokens can resume access without authenticating.

## Modes of Introduction

- **Sessions Not Invalidated Server-Side**: Terminating sessions only client-side, leaving session tokens valid on the server after logout or timeout.
- **Missing Client-Side Session Termination**: The app provides no way to terminate user sessions (e.g. no logout button or timeout).
- **No Re-Authentication on State Changes**: Resuming the app from the background or continuing after remarkable context changes (e.g. a significant change in the user's location or profile) without invalidating the current session and requiring re-authentication.
- **Cached Data Not Cleared**: Retaining session tokens, cached personal data, in-memory state, or on-screen content after the session ends.
- **Missing Inactivity Timeout**: Allowing sessions to remain valid indefinitely without inactivity or absolute expiration limits.

## Impact

- **Authentication or Authorization Bypass**: Attackers can resume the victim's session and act as the user without authenticating, resulting in unauthorized access to the account and its functionality.
- **Compromise of Sensitive Data**: Attackers can read cached or leftover personal data from a terminated session, resulting in unauthorized disclosure of user information.

## Mitigations

- **Invalidate Sessions Fully**: Invalidate the session server-side on logout, timeout, and account state changes, following the [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html).
- **Re-Authenticate on Context Changes**: Require re-authentication when the app returns to the foreground after a sensitive flow or when remarkable changes in the user's context (e.g. location or profile) are detected.
- **Clear Sensitive Data on Termination**: Remove session tokens, cached personal data, and in-memory or on-screen sensitive content when the session ends, including disconnecting linked accounts where applicable.
- **Enforce Timeouts**: Apply both inactivity and absolute session timeouts appropriate to the app's risk profile.
