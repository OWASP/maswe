---
title: Insufficient Protection of Sensitive Data from Screenshots or Screen Recordings
id: MASWE-0038
alias: data-leak-screenshots
requirement: "The app removes or masks sensitive data from its views when moved to the background, when being recorded or when a screenshot is taken."
platform: [android, ios]
profiles: [L2]
threat: MAS-THREAT-0038
attacks: [MAS-ATTACK-0010, MAS-ATTACK-0071, MAS-ATTACK-0072]
mappings:
  masvs-v1: [MSTG-STORAGE-9]
  masvs-v2: [MASVS-PLATFORM-3, MASVS-STORAGE-2]
  cwe: [200, 359]
  maswe-beta: [MASWE-0055]
refs:
- https://developer.android.com/about/versions/14/features/screenshot-detection
---

## Overview

This weakness occurs when sensitive data displayed by an app can be captured in screenshots or screen recordings, and the app does not prevent the capture or conceal or redact the data when such protection is warranted.

Mobile platforms allow users, privileged apps, and external tools to capture screenshots or record the screen. In addition, when an app enters the background, the system may capture a snapshot of the app's current view for display in the app switcher. Sensitive content that remains visible without appropriate protection can be retained in these images or recordings.

## Modes of Introduction

- **Missing Platform Screenshot Protection**: Displaying sensitive fields without applying the related platform protections that can avoid the field information from appearing in screenshots or screen recordings (e.g., in Android, applying the [`FLAG_SECURE`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_SECURE) flag).
- **Missing Capture-State Redaction**: Continuing to display sensitive information while the app or scene is being recorded, mirrored, or shared, despite the platform providing an API to detect the active capture state.
- **Excessive On-Screen Disclosure**: Displaying complete sensitive values when a masked, partial, temporary, or user-initiated representation would be sufficient for the current task.

## Impact

- **Compromise of Sensitive Data**: Sensitive information may be retained in an image or video after the app session ends and may later be viewed, shared, synchronized, backed up, or accessed by another person or service.

## Mitigations

- **Redact Sensitive On-Screen Content**: Display only the portion of a sensitive value required for the current task. Mask values by default and unmask the values only for the needed actions, masking them again once they have been used for the task.
- **Anti-Screenshot Platform Protections**: Apply platform protections that prevent elements containing sensitive content from appearing in screenshots or on non-secure displays (for example, in Android, applying the [`FLAG_SECURE`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_SECURE) flag).
