---
title: Sensitive Data Not Excluded From Backup
id: MASWE-0006
alias: data-not-excluded-backup
requirement: "The app excludes sensitive data from backups."
platform: [android, ios]
profiles: [L1, L2]
threat: MAS-THREAT-0006
attacks: [MAS-ATTACK-0008, MAS-ATTACK-0009]
mappings:
  masvs-v1: [MSTG-STORAGE-8]
  masvs-v2: [MASVS-STORAGE-2]
  cwe: [212, 313]
  android-risks:
  - backup-best-practices
  maswe-beta: [MASWE-0004, MASWE-0003]
refs:
- https://developer.android.com/guide/topics/data/autobackup#include-exclude-android-11
- https://developer.android.com/guide/topics/data/autobackup#include-exclude-android-12
- https://developer.android.com/guide/topics/data/autobackup#define-device-conditions
---

## Overview

This weakness occurs when an app fails to exclude sensitive data from device backups, so that user and app secrets end up in cloud or local backup archives.

iOS and Android automatically back up app data to cloud services, users can create local backups on physical machines, and backups are also created during data transfers when switching between phones. When developers do not properly configure how their app handles backups and neglect to exclude sensitive files, the backups may contain sensitive user and app data. Under certain conditions, the backups may not be adequately secured by the cloud provider, or a malicious actor could tamper with the backed-up files.

## Modes of Introduction

- **Automatic System Backups**: Relying on the platform's default cloud backup behavior, which includes app data once the user consents during the initial device setup, without defining backup exclusion rules for sensitive files.
- **Local Backups**: Allowing sensitive data to be included in backups that users create on local systems (e.g., laptops), where it may be stored unencrypted.
- **Device-To-Device Transfer**: Allowing sensitive data to be included in device-to-device migrations (e.g., via iCloud or Google's migration tools) without restricting transfer conditions.
- **Sensitive Data Unencrypted in Backups**: Storing sensitive data in backed-up locations without additional encryption, so it is readable by anyone who obtains the backup.

## Impact

- **Compromise of Sensitive Data**: Attackers can extract personal information, photos, documents, or audio files from backups, resulting in unauthorized disclosure of user data.
- **Authentication or Authorization Bypass**: Attackers can extract passwords, cryptographic keys, and session tokens from backups, resulting in identity theft, account takeover, or unauthorized access to backend services.
- **Bypass of Protection Mechanisms**: Attackers can modify backed-up app state, e.g. a database tracking premium features, or restore a pre-redemption backup to reuse one-time coupons, resulting in circumvention of business logic and revenue loss for the app owner.

## Mitigations

- **Exclude Sensitive Data from Backups**: Declare backup rules that exclude sensitive information, files, and key material from all backup mechanisms.
- **Encrypt Data That Must Be Backed Up**: If sensitive data has to be included in backups, encrypt it with an algorithm strong enough to protect the data for its entire required lifetime, even if the backup is later compromised.
- **Constrain Backup Conditions**: On Android, declare the appropriate [device conditions](https://developer.android.com/guide/topics/data/autobackup#define-device-conditions), such as requiring client-side encryption (`requireFlags="clientSideEncryption"`) and disabling device-to-device transfer (`deviceToDeviceTransfer`) for sensitive datasets, so that unencrypted copies are never produced.
