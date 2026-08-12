---
title: Lack of Proper Data Management Controls
id: MASWE-0076
alias: data-management-controls
requirement: "The app provides adequate controls to manage user data."
platform: [android, ios]
profiles: [P]
threat: MAS-THREAT-0076
attacks: [MAS-ATTACK-0083]
mappings:
  masvs-v2: [MASVS-PRIVACY-4]
  cwe: [359]
  maswe-beta: [MASWE-0113]
refs:
- https://developer.apple.com/app-store/app-privacy-details/#privacy-links
---

## Overview

This weakness occurs when an app does not provide users with mechanisms specifically designed to manage their personal data, leaving them without adequate options to exercise their rights over their own information.

These mechanisms typically include the ability for users to delete, export, modify, or opt out of data collection directly within the app interface. For example, some apps provide data management features within the settings menu, while others provide a link to an external website where users can manage their data.

## Modes of Introduction

- **Lack of Proper Data Management Settings**: Failing to provide users with the ability to delete, export, modify, or opt out of data collection.

## Impact

- **Violation of User Privacy**: Users cannot exercise their rights to manage their personal data, such as deleting or exporting their information, resulting in the loss of control over their data and an increased amount of exposed data if a breach occurs.
- **Loss of User Trust**: Users can perceive that they have no control over their personal data, resulting in negative reviews, decreased user engagement, and reduced retention for the app owner.
- **Legal and Regulatory Non-Compliance**: Failing to provide data management capabilities can violate regulations like GDPR and CCPA, resulting in fines, legal action, and other consequences for the app owner.

## Mitigations

- **Implement Data Management Mechanisms**: Ensure that mechanisms are in place for users to delete, export, or modify their data. Provide granular controls for specific aspects of data collection and sharing (e.g., location services, contacts, media access).
- **Regularly Update Data Management Features**: Regularly review and update data management features to ensure compliance with evolving regulations and user expectations. This helps maintain transparency and user trust.
- **Provide a User-Friendly Data Management Interface**: Create a user-friendly interface for data management controls, ensuring that users can easily navigate and exercise their rights over their personal data without friction.
