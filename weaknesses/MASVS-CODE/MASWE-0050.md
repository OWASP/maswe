---
title: Unsafe Handling of Untrusted Data
id: MASWE-0050
alias: unsafe-untrusted-data
requirement: "The app securely handles untrusted data."
platform: [android, ios]
profiles: [L1, L2]
threat: MAS-THREAT-0050
attacks: [MAS-ATTACK-0047, MAS-ATTACK-0059]
mappings:
  masvs-v1: [MSTG-PLATFORM-2]
  masvs-v2: [MASVS-CODE-4]
  cwe: [20, 22, 73, 89, 116, 345, 348, 349, 502, 611, 924]
  android-risks:
  - path-traversal
  - zip-path-traversal
  - sql-injection
  - unsafe-deserialization
  - xml-external-entities-injection
  - untrustworthy-contentprovider-provided-filename
  - use-of-native-code
  maswe-beta: [MASWE-0079, MASWE-0080, MASWE-0081, MASWE-0082, MASWE-0083, MASWE-0084, MASWE-0086, MASWE-0087, MASWE-0088]
refs:
- https://developer.android.com/topic/security/risks/path-traversal
- https://developer.android.com/topic/security/risks/sql-injection
- https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html
---

## Overview

This weakness occurs when data originating outside the app's trust boundary reaches a sensitive sink without being validated, sanitized, or safely parsed.

Untrusted data is any data the app did not create itself, regardless of how it arrives: network responses (even over TLS), data restored from backups, external interfaces such as Bluetooth, NFC, and USB, local files (including document pickers and archives), user interface input (text fields, QR codes, URLs, the clipboard), and the platform's IPC (e.g., for Android, received intents, broadcasts, content URIs, or deep links).

When the untrusted data reaches a dangerous sink that has not been validated or sanitized, it cause unintended behavior of the application by exploiting vulnerabilities like SQL injection, path traversal (including variants like ZIP path traversal), XML external entity (XXE) injection, insecure object deserialization, output-encoding flaws, or memory corruption in native parsers, or misleading presentation of security-relevant information.

## Modes of Introduction

- **Missing Validation at Trust Boundaries**: Consuming untrusted data from the network, backups, external interfaces, files, UI, or platform IPC without validating type, length, format, and range before use.
- **Untrusted Data in Queries**: Concatenating untrusted input into queries like SQL queries instead of using parameterized APIs.
- **Untrusted Paths and Archives**: Using externally supplied file names or paths (e.g. from ZIP entries) without canonicalization and containment checks.
- **Insecure Parsing**: Parsing untrusted XML with external entities enabled, or emitting untrusted data without proper output encoding.
- **Insecure Deserialization**: Deserializing untrusted data into rich object types (e.g. `Serializable`, `Parcelable`, `NSCoding`, XML/JSON object mappers) without restricting the allowed types.
- **Weakly Validated URI Handling**: Relying on URI parsing classes that apply little to no validation of untrusted input when making security decisions.
- **Unsafe Presentation of Untrusted Data**: Displaying untrusted data in notifications, warnings, confirmation dialogs, or other security-sensitive interfaces without constraining its length or formatting.

## Impact

- **Compromise of Sensitive Data**: Attackers can extract or overwrite private files and database contents through path traversal, SQL injection, or XXE, resulting in unauthorized disclosure or modification of user and app data.
- **Execution of Unauthorized Code**: Attackers can exploit insecure deserialization or memory corruption in parsers, resulting in attacker-controlled code running in the app's context.
- **Authentication or Authorization Bypass**: Attackers can manipulate queries or logic through injected input, resulting in access to data or functionality beyond what the caller is authorized for.
- **Compromise of Content or UI Integrity**: Attackers can obscure, alter, or impersonate trusted application content in interfaces or notifications, resulting in users approving unintended actions or ignoring legitimate security alerts.
- **Application Content Spoofing**: Attackers can obscure, alter, or impersonate trusted application content in interfaces or notifications, resulting in users approving unintended actions or ignoring legitimate security alerts.

## Mitigations

- **Validate at Every Trust Boundary**: Treat all externally originated data as untrusted and validate it against strict expectations before use.
- **Use Parameterized Queries**: Access databases exclusively through parameterized or prepared statements. Do not build queries by concatenating untrusted input.
- **Canonicalize and Contain Paths**: Canonicalize externally supplied file names and paths and verify they resolve inside the intended directory before any file operation.
- **Harden Parsers**: Disable external entity resolution for XML, apply correct output encoding for the destination context, and prefer hardened platform parsers.
- **Deserialize Safely**: Avoid deserializing untrusted data into rich object graphs; prefer simple data formats and safe APIs with explicit type allow-lists.
- **Distinguish Untrusted Data From Application-Generated Content**: Distinguish externally-provided values from trusted application content, especially in notifications and security-sensitive interfaces. Apply context-appropriate length, line, and formatting restrictions so untrusted data cannot obscure or alter the apparent meaning of the information presented.
