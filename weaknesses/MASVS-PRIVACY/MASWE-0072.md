---
title: Inadequate Privacy Policy
id: MASWE-0072
alias: privacy-policy
requirement: "The app provides an adequate privacy policy."
platform: [android, ios]
profiles: [P]
threat: MAS-THREAT-0072
attacks: [MAS-ATTACK-0079, MAS-ATTACK-0080]
mappings:
  masvs-v1: [MSTG-STORAGE-12]
  masvs-v2: [MASVS-PRIVACY-3]
  cwe: [359]
  maswe-beta: [MASWE-0111]
refs:
- https://support.google.com/googleplay/android-developer/answer/9859455#privacy_policy
- https://developer.apple.com/app-store/app-privacy-details/#privacy-links
- https://developer.apple.com/app-store/review/guidelines/#5.1.1
---

## Overview

This weakness occurs when an app does not provide users with a clear, accessible, and accurate statement of how their data is collected, processed, shared, and protected.

Privacy policies should be easily accessible, tailored specifically to the app in question, and written in a way that users can easily understand. Without a robust privacy policy, users are unable to make informed decisions about their data, and may be unaware of how their information is being used or shared. A privacy policy that is incomplete, vague, or does not match the app's behavior can mislead users and undermine transparency.

## Modes of Introduction

- **Unclear or Absent Privacy Policy**: Not providing a privacy policy, or having one that is not easily accessible or clear to the user, or that doesn't specifically address the data practices of that particular app, instead being a generic document that covers multiple services.
- **Discrepancies in Policy vs Behavior**: Collecting, processing, or sharing data in ways that differ from what the privacy policy states.

## Impact

- **Violation of User Privacy**: Users can unknowingly provide data that is shared with third parties, used for profiling, or used for targeted advertising without explicit consent, resulting in the loss of control over their personal information.
- **Loss of User Trust**: Users can perceive the app as non-transparent, resulting in negative reviews, decreased user engagement, and reduced retention for the app owner.
- **Legal and Regulatory Non-Compliance**: Failing to provide an adequate privacy policy can violate privacy laws and regulations, such as GDPR or CCPA, resulting in fines, legal action, or removal from app stores for the app owner.

## Mitigations

- **Provide a Clear Privacy Policy**: Make sure a comprehensive and understandable privacy policy is readily accessible to users. Tailor it to the specific data practices of your app and write it in clear, understandable language as stated in Article 12 of the GDPR.
- **Ensure Consistency in Policy vs Behavior**: Keep your data collection practices documented and up to date in privacy policies, privacy labels, and app store listings. Ensure that these documents match the app's actual behavior to avoid discrepancies that could mislead users or violate platform policies.
