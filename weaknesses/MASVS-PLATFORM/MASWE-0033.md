---
title: Sensitive Native Functionality Exposed in WebViews
id: MASWE-0033
alias: js-bridges-webviews
requirement: "The app does not expose sensitive native functionality to WebView content."
platform: [android, ios]
profiles: [L1, L2]
threat: MAS-THREAT-0033
attacks: [MAS-ATTACK-0047, MAS-ATTACK-0051]
mappings:
  masvs-v1: [MSTG-PLATFORM-7]
  masvs-v2: [MASVS-PLATFORM-2, MASVS-STORAGE-2]
  cwe: [749, 94]
  android-risks:
  - insecure-webview-native-bridges
  android-core-app-quality: [WebView_JavaScript]
  maswe-beta: [MASWE-0068]
refs:
- https://support.google.com/faqs/answer/9095419
- https://developer.android.com/develop/ui/views/layout/webapps/native-api-access-jsbridge
- https://developer.android.com/reference/androidx/webkit/WebViewCompat#addWebMessageListener(android.webkit.WebView,java.lang.String,java.util.Set%3Cjava.lang.String%3E,androidx.webkit.WebViewCompat.WebMessageListener)
- https://developer.apple.com/documentation/webkit/wkscriptmessagehandler
---

## Overview

This weakness occurs when an app exposes sensitive native functionality to content loaded in its WebViews, most commonly through JavaScript bridges.

Bridges such as [`addWebMessageListener`](https://developer.android.com/reference/androidx/webkit/WebViewCompat#addWebMessageListener%28android.webkit.WebView,java.lang.String,java.util.Set%3Cjava.lang.String%3E,androidx.webkit.WebViewCompat.WebMessageListener%29) on Android and [`WKScriptMessageHandler`](https://developer.apple.com/documentation/webkit/wkscriptmessagehandler) on iOS allow web content to send messages to native code. When these bridges expose more capability than necessary, or are reachable by untrusted content, malicious JavaScript can invoke native functionality, access sensitive data, or perform privileged actions using the app's permissions and privileges.

## Modes of Introduction

- **Bridges Reachable by Untrusted Content**: Making bridge interfaces available to any page, origin, or frame the WebView loads instead of restricting them to trusted origins.
- **Unvalidated Bridge Messages**: Accepting message names, arguments, or payloads without validating their structure, types, values, authorization, and expected application state.
- **Globally Exposed Bridge Mechanisms**: Using bridge mechanisms that expose native interfaces broadly across the WebView, such as Android `addJavascriptInterface`, when origin-scoped messaging APIs are available.
- **App-Owned Bridge Scripts in the Page World**: Running injected bridge scripts in the same JavaScript execution world as page content, allowing page scripts, including third-party scripts, to access or interfere with the bridge.
- **Sensitive Data in Bridge Replies**: Returning sensitive data into the WebView JavaScript context in a way that any untrusted scripts can read, regardless of user authentication state.
- **Over-Exposed Bridges**: Exposing more native functionality through the bridge than the web content actually needs.

## Impact

- **Compromise of Sensitive Data**: Attackers can call bridge methods that return user or app data, resulting in exfiltration of sensitive information to attacker-controlled servers.
- **Execution of Unauthorized Code**: Attackers can drive native functionality exposed through the bridge, resulting in privileged actions performed within the app's context.

## Mitigations

- **Minimize the Bridge Surface**: Expose only the specific methods the web content needs, and strip bridges entirely from WebViews that do not need them.
- **Restrict Bridges to Trusted Origins**: Attach bridges only when loading trusted content and prefer origin-scoped messaging mechanisms over global bridges.
- **Validate Bridge Messages**: Treat every message arriving over the bridge as untrusted input and validate it before acting on it.
- **Prefer Modern Messaging APIs**: On Android, prefer [`WebViewCompat.addWebMessageListener`](https://developer.android.com/reference/androidx/webkit/WebViewCompat#addWebMessageListener%28android.webkit.WebView,java.lang.String,java.util.Set,androidx.webkit.JavaScriptExecutionWorld,androidx.webkit.WebViewCompat.WebMessageListener%29) over the legacy [`WebView.addJavascriptInterface`](https://developer.android.com/reference/android/webkit/WebView#addJavascriptInterface%28java.lang.Object,java.lang.String%29). On iOS, use [`WKScriptMessageHandlerWithReply`](https://developer.apple.com/documentation/webkit/wkscriptmessagehandlerwithreply) when JavaScript requires a native response, and use [`WKScriptMessageHandler`](https://developer.apple.com/documentation/webkit/wkscriptmessagehandler) for one way messages.
- **Isolate App-Owned Bridge Scripts**: When the bridge is intended only for app-injected JavaScript, register the handler and injected script in a named execution world. Use [`JavaScriptExecutionWorld`](https://developer.android.com/reference/androidx/webkit/JavaScriptExecutionWorld) on Android and [`WKContentWorld`](https://developer.apple.com/documentation/webkit/wkcontentworld) on iOS, where supported. Keep origin restrictions, frame checks, and message validation in place, because execution world isolation is not origin authorization.
