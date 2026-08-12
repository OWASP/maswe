---
title: Insecure Deep Links
id: MASWE-0029
alias: insecure-deep-links
requirement: "The app securely handles deep links."
platform: [android, ios]
profiles: [L1, L2]
threat: MAS-THREAT-0029
attacks: [MAS-ATTACK-0046, MAS-ATTACK-0047]
mappings:
  masvs-v1: [MSTG-PLATFORM-3]
  masvs-v2: [MASVS-PLATFORM-1, MASVS-STORAGE-2, MASVS-CODE-4]
  cwe: [939, 917]
  android-risks:
  - unsafe-use-of-deeplinks
  maswe-beta: [MASWE-0058]
refs:
- https://developer.apple.com/documentation/technotes/tn3155-debugging-universal-links
- https://developer.android.com/training/app-links/verify-android-applinks
---

## Overview

This weakness occurs when an app handles deep links insecurely, relying on unverified schemes or trusting the attacker-controllable data they carry.

Deep links (Android App Links, iOS Universal Links and custom URL schemes) let other apps and websites launch the app, trigger an in-app action and pass parameters. They become insecure when the app relies on custom URL schemes that any app can claim, does not verify App Links or Universal Links through domain association, or fails to validate and sanitize the incoming URL and its parameters. Because deep link input is attacker-controllable, a malformed URI or parameter can trigger injection or logic abuse at various points in the app.

## Modes of Introduction

- **Unverified Custom URL Schemes**: Relying on custom URL schemes for sensitive flows even though any installed app can claim the same scheme.
- **Missing Domain Association**: Declaring App Links without `autoVerify` and Digital Asset Links, or Universal Links without a valid apple-app-site-association file, so links are not cryptographically tied to the app's domain.
- **Unvalidated Deep Link Input**: Passing the deep link URL and its parameters into navigation decisions, WebViews, or queries without validation and sanitization.

## Impact

- **Compromise of Sensitive Data**: Attackers can intercept tokens or personal data carried in deep links, or exfiltrate data through injected parameters, resulting in unauthorized disclosure of user data.
- **Authentication or Authorization Bypass**: Attackers can capture authentication material delivered via hijacked links (e.g. login or password-reset links), resulting in account takeover.
- **Execution of Unauthorized Code**: Attackers can inject expressions or script through unsanitized deep link parameters that reach interpreters or WebViews, resulting in attacker-controlled behavior inside the app.

## Mitigations

- **Use Verified Link Mechanisms**: Handle sensitive flows only through verified Android App Links (with `autoVerify` and Digital Asset Links) and iOS Universal Links, not through claimable custom schemes.
- **Validate and Sanitize Deep Link Input**: Treat every deep link URL and parameter as untrusted input; validate against an allowlist of expected destinations and value formats before use.
- **Validate the Source Where Possible**: Verify the calling application or referrer for custom scheme invocations when the platform allows it.
- **Keep Secrets Out of Deep Links**: Avoid transporting session tokens or other secrets in links; where unavoidable, make them single-use and short-lived.
