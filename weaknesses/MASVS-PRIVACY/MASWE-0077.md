---
title: Inadequate Data Visibility Controls
id: MASWE-0077
alias: data-visibility-control
requirement: "The app provides adequate controls over the visibility of user data."
platform: [android, ios]
profiles: [P]
threat: MAS-THREAT-0077
attacks: [MAS-ATTACK-0084, MAS-ATTACK-0087]
mappings:
  masvs-v2: [MASVS-PRIVACY-4]
  cwe: [359]
  maswe-beta: [MASWE-0114]
refs:
- https://firebase.google.com/support/privacy/storing-privacy-settings
- https://www.researchgate.net/publication/335863205_Demystifying_Hidden_Privacy_Settings_in_Mobile_Apps
---

## Overview

This weakness occurs when an app does not give users sufficient control over how their personal information is shared with other users or the broader environment.

Examples of such information include last connection status, read receipts, date of birth, email address, or discoverability settings. Ensuring that users have clear and granular options, typically in the form of app settings, to control data visibility is critical to maintaining their privacy and building trust in the app.

## Modes of Introduction

- **Lack of Granular Privacy Settings**: Failing to provide privacy settings with sufficient granularity to allow users to control specific aspects of data collection and sharing, such as differentiating between location services, contacts, or media access, or to decide which types of information are shared and with whom.
## Impact

- **Violation of User Privacy**: Users can unintentionally expose personal information, such as their email address, birthday, or online status, to others without their consent, resulting in an increased risk of harassment, stalking, or identity theft.
- **Loss of User Trust**: Users can feel they have inadequate control over what information is shared and with whom, resulting in negative reviews and decreased app engagement for the app owner.
- **Legal and Regulatory Non-Compliance**: Failing to offer sufficient privacy controls can violate regulations like GDPR or CCPA, which require user control over data visibility and sharing, resulting in fines or legal action for the app owner.

## Mitigations

- **Offer Granular Privacy Settings**: Provide privacy settings with sufficient granularity, allowing users to control individual data collection categories (e.g., location, contacts) and manage their sharing preferences. Allow users to choose what information is visible to others, such as connection status or discoverability.
- **Educate Users on Privacy Options**: Clearly inform users about available privacy settings and how to use them effectively to manage data visibility. This can be done through tutorials, help sections, or contextual tips within the app.
