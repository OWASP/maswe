---
title: Insecure Content Providers
id: MASWE-0064
alias: insecure-content-providers
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

Content Providers are an Android Inter-Process Communication (IPC) mechanism that enables structured data sharing between apps, and offers access to databases, files, or other storage mechanisms.

A Content Provider that is exported without proper permission enforcement and protection levels or that grants overly broad URI permissions can be queried or manipulated by any app on the device. File-based providers, such as `FileProvider`, present additional risk when misconfigured: they can expose files from the app's private directories to arbitrary callers.

The severity depends on the type of data the provider exposes. Providers that serve authentication tokens, personal data, or internal files pose a higher risk than those that share non-sensitive, public content.

## Modes of Introduction

- **Overly Broad FileProvider Paths**: A `FileProvider` is configured with overly broad `path` attributes (e.g., `path="."`) that share an entire directory rather than a narrow subdirectory, exposing files beyond what the app intends.
- **Exported Content Provider**: The app declares a Content Provider with `android:exported="true"` in the `AndroidManifest.xml` without restricting access through permissions.
- **Missing Authorization**: The `android:permission`, `android:readPermission`, or `android:writePermission` attributes are not set, allowing any app on the device to read and write to the exported Content Provider.
- **Weak Protection Level**: The custom permission guarding the provider is declared with a weak [protection level](https://developer.android.com/guide/topics/manifest/permission-element#plevel) such as `normal`, allowing any app that requests it to gain access.
- **Unscoped URI Permission Grants**: The app grants URI permissions with `FLAG_GRANT_READ_URI_PERMISSION` or `FLAG_GRANT_WRITE_URI_PERMISSION` in intents sent to untrusted components, allowing the receiver to access provider data without holding a permanent permission.

## Impact

- **Unauthorized Access**: Read access to sensitive data stored in the provider, such as personal information or application secrets.
- **Data Tampering or Deletion**: Unauthorized writes or deletions by a malicious app on records in an unprotected provider, potentially corrupting app state or causing denial of service.
- **Local File Disclosure**: Exposure of internal files to other apps through a misconfigured `FileProvider`.
- **Privilege Escalation**: Further control over the app or user data when an attacker chains provider access with other vulnerabilities.

## Mitigations

- **Validate Paths for FileProviders**: Restrict file operations to app-controlled directories, canonicalize paths before writing, and reject path traversal or ambiguous path inputs. Additionally, restrict `FileProvider` path configurations to the narrowest directory needed (e.g., `path="images/"`) rather than sharing an entire directory with `path="."`.
- **Secure Default**: Rely on the platform default (content providers are non-exported by default since API Level 17). Only set `android:exported="true"` in the Android Manifest when cross-app sharing of data is explicitly required.
- **Least Privilege**: Protect exported content providers with narrow read and write permissions to [restrict interactions with it](https://developer.android.com/training/permissions/restrict-interactions#content-providers).
- **Scope URI Permissions**: Grant URI permissions on a [per-URI basis](https://developer.android.com/training/permissions/restrict-interactions#uri) rather than to the entire provider. Use `FLAG_GRANT_READ_URI_PERMISSION` or `FLAG_GRANT_WRITE_URI_PERMISSION` for temporary, scoped access and revoke them with `revokeUriPermission()` as soon as they are no longer needed.
- **Use a Strong Protection Level**: Declare the custom permission with the [`signature` protection level](https://developer.android.com/guide/topics/manifest/permission-element#plevel) to limit access to apps signed with the same certificate, or with `dangerous` to require explicit user consent.

!!! Warning "Signature Permission"
    Requiring `signature` for all exported providers might break legitimate cross-app data sharing; understand the intended purpose of the content provider before choosing a protection level.
