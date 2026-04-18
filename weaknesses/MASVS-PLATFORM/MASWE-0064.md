---
title: Insecure Content Providers
id: MASWE-0064
alias: insecure-content-providers
platform: [android]
profiles: [L1, L2]
mappings:
  masvs-v1: [MSTG-STORAGE-6]
  masvs-v2: [MASVS-PLATFORM-1, MASVS-STORAGE-1]
  cwe: [20, 73, 926]
  android-risks:
  - https://developer.android.com/privacy-and-security/risks/content-resolver
  - https://developer.android.com/privacy-and-security/risks/untrustworthy-contentprovider-provided-filename
refs:
- https://developer.android.com/guide/topics/providers/content-provider-basics
- https://developer.android.com/reference/android/content/ContentProvider
- https://developer.android.com/reference/android/content/ContentResolver
status: new
---

## Overview

This weakness occurs when an app exposes or consumes data through `ContentProvider` and `ContentResolver` interfaces without enforcing trust boundaries, access restrictions, and input validation.

Content providers are designed to share structured data between apps through content URIs, including metadata and file-backed resources. This model is powerful for interoperability, but it also creates an inter-process boundary where untrusted callers and untrusted providers can influence data access and file operations.

The weakness can appear in both provider implementations and client code. Providers may overexpose data through incorrect export settings or insufficient permission checks, while clients may treat provider-returned values as trusted even though they originate outside the app's trust domain.

## Modes of Introduction

- Developers configure a provider as exported, or with weak read/write permissions, when the data was intended only for internal app use.
- Developers rely only on manifest declarations and omit runtime validation of caller identity, URI patterns, or requested operations in provider methods.
- Developers consume data from external providers through `ContentResolver` APIs and trust returned columns, MIME types, or filenames without sanitization and canonicalization.
- Developers open file descriptors or create local files based on provider-supplied metadata without constraining paths and destinations to app-controlled locations.
- Third-party SDKs or cross-platform plugins add provider components or provider-consuming flows with permissive defaults that bypass the app's intended sharing model.

## Impact

- Unauthorized apps can read sensitive records or files exposed by a misconfigured provider.
- Unauthorized apps can modify or delete shared data, causing integrity loss and business logic manipulation.
- Malicious providers can supply crafted metadata or filenames that cause insecure file handling in the consuming app.
- Attackers can trigger overwrite or placement of files in unintended app-accessible locations when path handling is not constrained.
- Compromised provider trust boundaries can enable follow-on attacks such as privilege misuse, data exfiltration, or persistence of tampered content.

## Mitigations

- Keep providers non-exported by default, and only export when cross-app sharing is explicitly required.
- Protect exported providers with the narrowest feasible read and write permissions, and enforce additional runtime authorization checks.
- Validate and constrain every incoming URI, selection argument, and operation before processing provider requests.
- Treat all data returned by external providers as untrusted, and sanitize metadata such as display names, MIME types, and paths before use.
- Restrict file operations to app-controlled directories, canonicalize paths before writing, and reject path traversal or ambiguous path inputs.
