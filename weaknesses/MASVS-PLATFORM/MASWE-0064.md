---
title: Insecure Content Providers
id: MASWE-0064
alias: MASWE-0064
platform: [android]
profiles: [L1, L2]
mappings:
  masvs-v1: [MSTG-STORAGE-6]
  masvs-v2: [MASVS-PLATFORM-1, MASVS-STORAGE-1]
  cwe: [926]
  android-risks:
    - https://developer.android.com/topic/security/risks/content-resolver
refs:
  - https://developer.android.com/reference/androidx/core/content/FileProvider
  - https://developer.android.com/topic/security/risks/file-providers
  - https://developer.android.com/privacy-and-security/security-tips#content-providers
status: new
---

## Overview

Content Providers are an Android Inter-Process Communication (IPC) mechanism that enables structured data sharing between apps, backed by databases, files, or other storage mechanisms.

The availability of insecure Content Providers occurs when an app exposes a Content Provider without adequate access restrictions, allowing other apps on the device to read, modify, or delete data they shouldn't have access to.


A Content Provider that is exported without proper permission enforcement or that grants overly broad URI permissions can be queried or manipulated by any app on the device. File-based providers, such as `FileProvider`, present additional risk when misconfigured: they can expose files from the app's private directories to arbitrary callers.

The severity depends on the type of data the provider exposes. Providers that serve authentication tokens, personal data, or internal files pose a higher risk than those that share non-sensitive, public content.

## Modes of Introduction

- The app declares a Content Provider with `android:exported="true"` in the `AndroidManifest.xml` without setting a `android:permission`, `android:readPermission`, or `android:writePermission` attribute.
- The app targets an API level below 17, where Content Providers are exported by default unless explicitly set to `android:exported="false"`.
- A `FileProvider` is configured with overly broad path rules (e.g., sharing the root of internal storage via `<root-path>`) that expose files beyond what the app intends.
- The app grants URI permissions with `FLAG_GRANT_READ_URI_PERMISSION` or `FLAG_GRANT_WRITE_URI_PERMISSION` in intents sent to untrusted components, allowing the receiver to access provider data without holding a permanent permission.
- The app defines a custom permission with `android:protectionLevel="normal"` to guard the provider, which any app can request and obtain without user approval.

## Impact

- **Unauthorized Access**: Read access to sensitive data stored in the provider, such as personal information, or application secrets.
- **Data tampering or deletion**: Through unintended access by a malicious app that writes to or deletes records in an unprotected provider, potentially corrupting app state or causing denial of service.
- **Local file disclosure**: Through a misconfigured `FileProvider` that exposes internal files (databases, shared preferences, or configuration files) to other apps.
- **Privilege escalation**: When an attacker chains provider access with other vulnerabilities to gain further control over the app or user data.

## Mitigations

- **Secure Default**: Content providers are non-exported by default since API Level 17. Only set `android:exported="true"` in the Android Manifest, when cross-app sharing of data is explicitly required.
- **Least Privilege**: Protect exported content providers with narrow read and write permissions
- **Runtime Checks**: Enforce additional runtime authorization checks, by using []`checkCallingPermission`](https://developer.android.com/reference/android/content/Context#checkCallingPermission(java.lang.String))
- **Validate Paths**: Restrict file operations to app-controlled directories, canonicalize paths before writing, and reject path traversal or ambiguous path inputs. Additionally, restrict `FileProvider` path configurations to the narrowest directory needed and avoid using `<root-path>`.
- **Protection Level: Signature**: To effectively restrict access, the custom permission should use the [`signature` protection level](https://developer.android.com/guide/topics/manifest/permission-element#plevel), which limits access to apps signed with the same certificate.

!!! `Signature Permission`
    Requiring `signature` for all exported providers might break legitimate cross-app data sharing, therefore it is necessary to understand what the intention of the content provider is.
