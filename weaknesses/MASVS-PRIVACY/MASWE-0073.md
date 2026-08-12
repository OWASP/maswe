---
title: Inadequate Data Collection Declarations
id: MASWE-0073
alias: data-collection-declarations
requirement: "The app adequately declares all user collected data."
platform: [android, ios]
profiles: [P]
threat: MAS-THREAT-0073
attacks: [MAS-ATTACK-0081, MAS-ATTACK-0082]
mappings:
  masvs-v1: [MSTG-STORAGE-12, MSTG-NETWORK-1]
  masvs-v2: [MASVS-PRIVACY-3, MASVS-PRIVACY-1]
  cwe: [359]
  maswe-beta: [MASWE-0112, MASWE-0108]
refs:
- https://support.apple.com/en-us/102188
- https://support.apple.com/kb/HT211970
- https://developer.apple.com/app-store/review/guidelines/#5.1.2
- https://developer.apple.com/app-store/app-privacy-details/#data-collection
- https://support.google.com/googleplay/android-developer/answer/10787469
- https://developer.apple.com/videos/play/wwdc2023/10060
- https://support.google.com/googleplay/answer/11416267
- https://www.youtube.com/watch?v=J7TM0Yy0aTQ
- https://www.youtube.com/watch?v=4rfF3y4xchU
---

## Overview

This weakness occurs when an app's stated data collection practices, such as those documented in Apple's [App Privacy Report](https://support.apple.com/en-us/102188) and [Privacy Nutrition Labels](https://support.apple.com/kb/HT211970), or Google's [Data Safety section](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en), are incomplete or inconsistent with the app's actual behavior.

These declarations must clearly outline what data is collected, how it is used, whether it is linked to the user's identity, and whether it is shared with third parties in accordance with the platform's policies. When they are inaccurate, users are prevented from making informed decisions about their privacy, including understanding whether data will be linked to their identity, used for tracking, or shared with third parties.

**Note about third-party libraries (SDKs)**: Developers, as data controllers, are legally responsible for ensuring that third-party components process sensitive data lawfully, fairly, and transparently, as highlighted in the [ENISA study on GDPR compliance](https://www.enisa.europa.eu/sites/default/files/publications/WP2017%20O-2-2-4%20GDPR%20Mobile.pdf) (Section 2.2.7, _"Data transfers and processing by third parties"_). However, in some cases, it may be challenging for mobile app developers to be fully aware of what data these third-party SDKs actually collect.

## Modes of Introduction

- **Undeclared Data Collection and Purpose**: Failing to declare what data is being collected (e.g., location, contacts, identifiers) and for what purposes (e.g., analytics, personalization).
- **Discrepancies in Declarations vs Behavior**: Publishing declarations that differ from the app's actual behavior by using data for purposes other than those disclosed.

## Impact

- **Violation of User Privacy**: Users can unknowingly share data whose purpose they do not understand, resulting in unauthorized sharing, profiling, or targeted advertising.
- **Loss of User Trust**: Users can discover the inconsistent declarations, resulting in negative reviews, lower user engagement, and reduced retention for the app owner.
- **Legal and Regulatory Non-Compliance**: Inaccurate or inconsistent data declarations can violate regulations like GDPR or CCPA and platform policies, resulting in fines, legal action, or removal from app stores for the app owner.

## Mitigations

- **Maintain Accurate Privacy Labels**: Comply with Apple's Privacy Nutrition Labels and Google's Data Safety Section requirements by providing accurate, up to date and transparent information about your data practices, including data collection and sharing with third parties.
