---
title: Inadequate Permission Management
id: MASWE-0066
alias: inadequate-permission-management
requirement: "The app adequately manages permissions."
platform: [android, ios]
profiles: [P]
threat: MAS-THREAT-0066
attacks: [MAS-ATTACK-0088, MAS-ATTACK-0089]
mappings:
  masvs-v2: [MASVS-PRIVACY-1]
  cwe: [250]
  android-core-app-quality: [Minimize_Permissions, Sensitive_Permissions, Runtime_Permissions, Permission_Rationale, Graceful_Degradation]
  maswe-beta: [MASWE-0117]
refs:
- https://developer.apple.com/design/human-interface-guidelines/privacy#Requesting-permission
- https://developer.apple.com/documentation/uikit/protecting_the_user_s_privacy/requesting_access_to_protected_resources
- https://developer.android.com/training/permissions/requesting
- https://support.google.com/googleplay/android-developer/answer/9888170?hl=en
- https://developer.android.com/privacy-and-security/minimize-permission-requests
- https://developer.android.com/training/permissions/usage-notes
- https://arxiv.org/pdf/1905.02713
- https://arxiv.org/pdf/2203.10583
- https://ieeexplore.ieee.org/document/9001128
- https://www.enisa.europa.eu/sites/default/files/publications/WP2017%20O-2-2-4%20GDPR%20Mobile.pdf
- https://developer.android.com/privacy-and-security/risks/ai-risks/excessive-agency
- https://developer.android.com/privacy-and-security/risks/ai-risks/sensitive-information-disclosure
- https://developer.apple.com/documentation/bundleresources/information_property_list/nsextension/nsextensionattributes/requestsopenaccess
---

## Overview

This weakness occurs when an app requests more permissions than it needs, keeps permissions it no longer needs, or fails to explain why permissions are required.

Permissions control access to sensitive device features such as the camera, microphone, location, and storage, making them a crucial aspect of mobile app privacy. They serve as the gateway for data collection and processing, so proper permission management is essential to protect user privacy and comply with regulations.

Developers face the challenge of balancing functionality with privacy: while some permissions are essential for core features (e.g., a camera app requiring camera access), excessive permissions enable unnecessary data collection. From the user's perspective, privacy concerns may lead to reluctance in granting permissions, forcing them to choose between privacy and app functionality, while other users may grant permissions without fully understanding the implications. Pre-installed apps aggravate the problem, as they frequently come with excessive permissions that are granted by default and that users cannot control or revoke.

Third-party libraries (SDKs) further complicate permission management by requiring permissions that the app itself does not need and by using the app's granted permissions to collect data. Similarly, AI-enabled features can be given permission-backed tools that allow them to access sensitive data or act on the user's behalf beyond what the feature requires. Mobile permission models often fail to distinguish between permissions granted to an app and those assigned to third-party components, a challenge highlighted in the [IEEE research paper "Engineering Privacy in Smartphone Apps"](https://ieeexplore.ieee.org/document/9001128) (Section IV, _"Third-party content"_). Furthermore, third-party services behind these SDKs may continue accessing data collected over the network even after permissions are revoked or the app is deleted.

## Modes of Introduction

- **Requesting Excessive Permissions**: Requesting more permissions than necessary for the app's core functionality.
- **Lack of Use of Privacy-Friendly Alternatives**: Failing to use less intrusive alternatives, such as requesting fine location when coarse location would suffice or requesting camera and photo-library access instead of using an image picker.
- **Retaining Unneeded Permissions**: Not revoking permissions that are no longer necessary.
- **Inadequate Permission Explanations**: Failing to provide clear explanations for why each permission is required.
- **Third-Party Permission Requirements**: Including SDKs that require permissions beyond the app's functional needs or use granted permissions to collect and analyze data.
- **Excessive AI Agent Permissions**: Giving an AI-enabled feature permission-backed tools or data access beyond what it requires for its intended task.
- **Unjustified Full Access in a Bundled Keyboard**: Shipping a custom keyboard extension that sets `RequestsOpenAccess` to `true` without a feature that requires it, allowing the keyboard to transmit typed input or write it to a shared container.

## Impact

- **Violation of User Privacy**: Apps and embedded components can use unnecessarily granted access to collect location, contacts, or media, resulting in tracking, surveillance, or profiling of the user.
- **Compromise of Sensitive Data**: Apps and embedded components can retain sensitive data collected through unnecessary permissions, resulting in broader exposure of that data when the app or a third-party service suffers a data breach.
- **Loss of User Trust**: Users can perceive permission requests as unjustified, resulting in refused permissions, negative reviews, lower user engagement, and reduced retention for the app owner.
- **Legal and Regulatory Non-Compliance**: Requesting or retaining unnecessary permissions can violate data minimization requirements in regulations like GDPR or CCPA, resulting in fines, legal action, or removal from app stores for the app owner.

## Mitigations

- **Limit Permissions to Essential Needs**: Ensure the app and any AI-enabled features only request permissions necessary for core functionality, avoiding the collection of unnecessary data and adhering to the principle of data minimization.
- **Prefer Privacy-Friendly Alternatives**: Use privacy-friendly alternatives to permissions that are less intrusive and provide users with more control over their data. For example, use coarse location instead of fine location, or use an image picker instead of requesting access to the camera and photo gallery.
- **Enable Proactive Permission Revocation**: Automatically relinquish permissions that are no longer necessary to minimize unnecessary data access over time, and ensure that users can manually revoke permissions at any time through a clear and accessible interface.
- **Implement Just-in-Time Permission Requests**: Request permissions only when they are needed, providing clear explanations for why each permission is required. This approach helps build user trust and ensures users understand the implications of granting access to their data.
- **Add Proper Permission Explanations**: Provide clear explanations for why each permission is required, helping users understand the necessity and scope of the requested access.
- **Avoid Full Access in Bundled Keyboards**: Do not set `RequestsOpenAccess` in a custom keyboard extension unless a user-facing feature requires it, and never use it to transmit or store the characters the keyboard receives.
