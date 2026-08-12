---
title: Debug Mechanisms Not Disabled
id: MASWE-0063
alias: debuggable-flag
requirement: "The app disables debug mechanisms."
platform: [android, ios]
profiles: [R]
threat: MAS-THREAT-0063
attacks: [MAS-ATTACK-0002, MAS-ATTACK-0003, MAS-ATTACK-0004]
mappings:
  masvs-v1: [MSTG-RESILIENCE-2]
  masvs-v2: [MASVS-RESILIENCE-4, MASVS-PLATFORM-2]
  cwe: [489]
  android-risks:
  - android-debuggable
  maswe-beta: [MASWE-0067, MASWE-0074]
refs:
- https://developer.android.com/guide/topics/manifest/application-element
- https://developer.android.com/reference/android/webkit/WebView#setWebContentsDebuggingEnabled(boolean)
- https://developer.apple.com/documentation/webkit/wkwebview/4111163-isinspectable
- https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.cs.debugger
---

## Overview

This weakness occurs when the application has debug mechanisms enabled in production builds, allowing the usage of platform debuggers, or exposes embedded web or JavaScript content to developer inspection tools.

Mobile apps can include configuration flags and mechanisms that enable debugging. While these are essential during development, leaving them enabled in production makes the app inspectable and manipulable.

On Android, application debugging is controlled by the [`android:debuggable`](https://developer.android.com/privacy-and-security/risks/android-debuggable) value in the app's Android Manifest. On iOS, application debuggability is not controlled by an `Info.plist` key. It depends on the [`get-task-allow` entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.cs.debugger) in the signed application, which is normally enabled for development-signed builds and disabled for distribution-signed builds.

Beyond the application-level debuggable flag, this weakness also covers web-content debugging, which lets a remote inspector attach to the app's web content (e.g. Android's [`WebView.setWebContentsDebuggingEnabled(true)`](https://developer.android.com/reference/android/webkit/WebView#setWebContentsDebuggingEnabled(boolean)) or iOS's [`WKWebView.isInspectable`](https://developer.apple.com/documentation/webkit/wkwebview/isinspectable)).

## Modes of Introduction

- **Misconfigured Build Settings**: Accidentally leaving the app in a debuggable state through improper selection of build variants, errors in CI/CD configurations, or mistakenly applying debug settings to production environments.
- **WebView or JavaScript Debugging Enabled**: Leaving WebView content debugging enabled in production (e.g. `setWebContentsDebuggingEnabled(true)` on Android or `isInspectable = true` on iOS).

## Impact

- **Compromise of Sensitive Data**: Attackers can read the app's memory and logs to obtain encryption keys, API keys, user credentials, or tokens that are never written to the app's code or disk, resulting in unauthorized disclosure of secrets and user data.
- **Authentication or Authorization Bypass**: Attackers can manipulate the app's execution flow to skip authentication and authorization checks, resulting in unauthorized access to protected functionality.
- **Facilitated Reverse Engineering and Instrumentation**: Debug access reduces the effort required to observe and manipulate the application's behavior and may facilitate further dynamic analysis or instrumentation.

## Mitigations

- **Disable Application Debugging in Release Builds**: Ensure that the debuggable flag in the app's configuration file is not enabled for production builds. For example, set [`isDebuggable = false` or `debuggable false`](https://developer.android.com/studio/publish/preparing) in Android or ensure that the `get-task-allow` entitlement is absent or set to `false` in iOS applications.
- **Disable WebView and JavaScript Content Debugging in Release Builds**: Ensure that the WebViews and JavaScript contexts in the application are not debuggable. For example, do not call `setWebContentsDebuggingEnabled(true)` on Android and keep `WKWebView.isInspectable` set to `false` on iOS.
