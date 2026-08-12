---
title: WebViews Loading Untrusted Content
id: MASWE-0035
alias: webviews-untrusted-content
requirement: "The app only allows trusted content in WebViews."
platform: [android, ios]
profiles: [L1, L2]
threat: MAS-THREAT-0035
attacks: [MAS-ATTACK-0047, MAS-ATTACK-0051]
mappings:
  masvs-v2: [MASVS-PLATFORM-2, MASVS-CODE-4]
  cwe: [79, 601, 829]
  android-risks:
  - cross-app-scripting
  - unsafe-uri-loading
  maswe-beta: [MASWE-0071, MASWE-0070, MASWE-0072]
refs:
- https://blog.oversecured.com/Evernote-Universal-XSS-theft-of-all-cookies-from-all-sites-and-more/
---

## Overview

This weakness occurs when a WebView loads URLs, HTML, or JavaScript from untrusted sources, or lets users navigate to arbitrary sites outside the developer's control.

WebViews run with app-specific privileges and often use JavaScript bridges (see @MASWE-0033) to communicate between the web sandbox and the app to access contacts, local files, the device location, or its camera. Loading untrusted content into WebViews is therefore more dangerous than opening it in an external browser.

A URL received via an intent or deep link, or JavaScript fetched from an unverified source, can lead to cross-site scripting, including Universal XSS, allowing an attacker to steal cookies and tokens from any site, perform phishing attacks, or trigger drive-by downloads. Actors can also access functionality outside the web sandbox using JavaScript bridges declared by the developers.

## Modes of Introduction

- **Unrestricted Navigation**: Not restricting which origins the WebView may load (e.g. via `WebViewClient.shouldOverrideUrlLoading` or navigation delegates), letting users or content navigate anywhere directly, or loading domains that can be used to navigate to attacker-controlled domains.
- **Untrusted URLs from External Input**: Loading URLs received through intents, deep links, or other external input without validating them against an allowlist.
- **Untrusted Script Inclusion**: Loading JavaScript from unverified sources into pages rendered by the WebView.
- **Safe Browsing Disabled**: Disabling platform protections such as Safe Browsing that warn about known-malicious sites.
- **Deprecated WebView Components**: Using deprecated WebView implementations that lack modern process isolation and security protections.

## Impact

- **Compromise of Sensitive Data**: Attackers can steal cookies, tokens, or displayed data from any origin via cross-site scripting in the privileged WebView, resulting in unauthorized disclosure of session material and user data.
- **Authentication or Authorization Bypass**: Attackers can reuse stolen session cookies or tokens, resulting in account takeover across the sites the WebView had sessions with.
- **Loss of User Trust**: Attackers can render phishing pages or trigger unwanted downloads inside the app's own UI, resulting in users being deceived under the app's identity and reputational damage for the app owner.

## Mitigations

- **Allowlist Navigation**: Restrict the WebView to an allowlist of trusted origins and open everything else in the system browser.
- **Validate Externally Supplied URLs**: Treat URLs arriving via intents or deep links as untrusted input and validate them before loading (see @MASWE-0029 and @MASWE-0032).
- **Load Scripts Only from Trusted Sources**: Never inject or include JavaScript fetched from unverified sources.
- **Keep Platform Protections Enabled**: Leave Safe Browsing and equivalent protections enabled and use current, supported WebView components.
