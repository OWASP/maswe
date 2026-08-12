---
title: WebViews Allow Access to Local Resources with Untrusted Content
id: MASWE-0034
alias: webviews-local-resources
requirement: "The app only allows trusted WebView content to access local resources."
platform: [android, ios]
profiles: [L1, L2]
threat: MAS-THREAT-0034
attacks: [MAS-ATTACK-0047, MAS-ATTACK-0051]
mappings:
  masvs-v1: [MSTG-PLATFORM-6]
  masvs-v2: [MASVS-PLATFORM-2, MASVS-STORAGE-2, MASVS-CODE-4]
  cwe: [22, 79, 200, 669]
  android-risks:
  - webview-unsafe-file-inclusion
  android-core-app-quality: [WebView_Asset_Loader]
  maswe-beta: [MASWE-0069, MASWE-0073]
refs:
- https://blog.oversecured.com/Android-Exploring-vulnerabilities-in-WebResourceResponse/
---

## Overview

This weakness occurs when a WebView is configured to access local resources while also rendering untrusted content, allowing that content to reach files and data outside the web sandbox.

Settings that enable file or content access (e.g. `setAllowFileAccess`, `setAllowFileAccessFromFileURLs`, `setAllowUniversalAccessFromFileURLs`, `setAllowContentAccess` on Android, or overly broad file read access grants on iOS) let JavaScript running in the WebView read app-private files, traverse the filesystem, or exfiltrate data. Insecure custom resource loading, such as serving internal files through a hand-rolled `WebResourceResponse` instead of a safe asset loader, can likewise expose protected files to the less-trusted WebView JavaScript context or serve attacker-controllable content from the app's own origin.

## Modes of Introduction

- **File Access Enabled with Untrusted Content**: Enabling file or content access settings on WebViews that also render untrusted or externally influenced content.
- **Universal Access from File URLs**: Allowing universal or file-URL cross-origin access, so a local HTML file can read other local files and send them to remote origins.
- **Insecure Custom Resource Loading**: Serving internal files through custom response handlers without path validation, instead of a dedicated asset-loading mechanism with a restricted scope.
- **Overly Broad File Read Grants**: Granting the WebView read access to broader directories than the specific content it needs to display.

## Impact

- **Compromise of Sensitive Data**: Attackers can read and exfiltrate app-private files, such as databases, preferences, or cached tokens, resulting in unauthorized disclosure of user and app data.
- **Authentication or Authorization Bypass**: Attackers can steal session material stored in reachable files or WebView storage, resulting in account takeover.

## Mitigations

- **Disable File and Content Access**: Keep file, file-URL, and content access settings disabled unless strictly required, and never combine them with untrusted content.
- **Use a Safe Asset Loader**: Serve local app resources through a dedicated asset-loading mechanism with a fixed, validated scope instead of custom response handlers over arbitrary paths.
- **Scope File Read Access Narrowly**: When loading local files, grant read access only to the specific file or directory being displayed.
- **Separate Trusted and Untrusted Content**: Render untrusted content only in WebViews with no local resource access and no privileged configuration.
