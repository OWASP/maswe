---
title: Sensitive Data Leaked via Screenshots or Screen Recordings
id: MASWE-0055
alias: data-leak-screenshots
platform: [android, ios]
profiles: [L2]
mappings:
  masvs-v1: [MSTG-STORAGE-9]
  masvs-v2: [MASVS-PLATFORM-3, MASVS-STORAGE-2]
  cwe: [200, 359]

refs:
- https://developer.android.com/about/versions/14/features/screenshot-detection
status: new

---

## Overview

Mobile platforms allow users and third-party tools to capture screenshots or record screens. This can expose sensitive data and increase the risk of data leakage.

There are several ways an attacker may obtain this sensitive data:

- **Third-party apps with permission to capture or record the screen**: Third-party apps may record the screen while sensitive content is displayed.
- **Third-party apps with permission to access the screenshot and recording files**: Third-party apps may access screenshots or recordings saved in storage after they are taken by the user or a tool.
- **External tools may record the screen**: Tools such as @MASTG-TOOL-0024 and @MASTG-TOOL-0126 can record the device's screen via a USB connection.
- **Automatic Screenshots when Backgrounding**: When an app enters the background state, the system may capture a screenshot of the app's current view to display in the app switcher. These screenshots are stored on the file system and could potentially be accessed or stolen by malicious actors.

## Impact

- **Loss of Confidentiality**: Under certain conditions, an attacker could access sensitive data previously displayed on the screen, potentially compromising confidentiality and enabling further attacks, such as identity theft or account takeover.

## Modes of Introduction

This can typically occur in two ways:

- **Screenshots and Screen Recordings Not Prevented:** The app does not implement measures (such as setting secure window flags) to prevent the operating system or other apps from capturing screenshots or screen recordings.
- **Unredacted Sensitive On-Screen Content:** The app displays sensitive information directly on the screen without masking or redacting it, allowing confidential data to be visible if a screenshot or screen recording is taken.

## Mitigations

- Prevent screenshots and screen recording.
- Redact sensitive on-screen content so that, if a screenshot is taken, no confidential data is visible.
