---
title: Incorrect Use of Identifiers for User Tracking
id: MASWE-0068
alias: unique-identifiers-user-tracking
requirement: "The app does not use persistent or unique identifiers in a way that enables user tracking."
platform: [android, ios]
profiles: [P]
threat: MAS-THREAT-0068
attacks: [MAS-ATTACK-0074, MAS-ATTACK-0077]
mappings:
  masvs-v2: [MASVS-PRIVACY-2]
  cwe: [359]
  android-core-app-quality: [Hardware_IDs]
  maswe-beta: [MASWE-0110]
refs:
- https://developer.android.com/reference/android/provider/Settings.Secure#ANDROID_ID
- https://developer.android.com/privacy-and-security/about#resettable-identifiers
- https://developer.android.com/identity/user-data-ids
- https://developer.android.com/identity/user-data-ids#common-use-cases
- https://developer.android.com/identity/ad-id
- https://developers.google.com/privacy-sandbox/private-advertising/attribution-reporting/android
- https://developer.apple.com/app-store/app-privacy-details/#user-tracking
- https://developer.apple.com/app-store/user-privacy-and-data-use/
- https://developer.apple.com/documentation/apptrackingtransparency/
- https://developer.apple.com/documentation/adsupport/asidentifiermanager/advertisingidentifier
- https://developer.apple.com/documentation/uikit/uidevice/1620059-identifierforvendor/
- https://developer.apple.com/app-store/ad-attribution/
- https://developer.apple.com/documentation/adattributionkit
- https://gdpr-info.eu/recitals/no-30/
---

## Overview

This weakness occurs when an app uses persistent or unique identifiers in a way that enables users to be recognized and followed over time and across different apps, devices, and services, often without their knowledge or consent.

Mobile apps commonly include embedded utilities or third-party SDKs, such as analytics tools, ad networks, and social media integration components, from companies like Google or Meta. These components can collect data not directly related to the app's functionality, potentially accessing sensitive information like contact lists or location history, depending on the permissions granted. Pre-installed apps by device manufacturers can further complicate the issue, as they may engage in invasive data collection without users' knowledge.

Unique identifiers, especially those that cannot be reset, are a key enabler of this tracking. When combined with data from multiple apps, they can be used to create detailed profiles of individuals, estimating interests, health status, sexual orientation, and other personal attributes, which can then be used for targeted advertising, personalized content delivery, or even to influence political opinions.

## Modes of Introduction

- **Use of Non-Resettable Identifiers**: Utilizing identifiers that cannot be reset by the user, such as device IDs, hardware serial numbers, or MAC addresses. For example, the [`ANDROID_ID`](https://developer.android.com/reference/android/provider/Settings.Secure#ANDROID_ID) before Android 8.0 (API level 26) was a non-resettable identifier randomly generated at first boot, while in recent versions it's unique to each combination of app-signing key, user, and device.
- **Misuse of Resettable Identifiers**: Using [resettable identifiers](https://developer.android.com/privacy-and-security/about#resettable-identifiers) like the [Advertising ID](https://developer.android.com/identity/user-data-ids#advertising-ids) on Android or the [Advertising Identifier (aka. Identifier for Advertisers or IDFA)](https://developer.apple.com/documentation/adsupport/asidentifiermanager/advertisingidentifier) on iOS without respecting user preferences or obtaining proper consent.
- **Linking Identifiers Across Services**: Combining identifiers from different sources, such as device IDs, advertising IDs, or other unique identifiers as well as behavioral data, to create a unified profile of a user, even after a reset or reinstall.
- **Tracking Without User Consent**: Tracking users across services or apps without their explicit consent or without providing the ability to opt out or reset identifiers. For instance, on iOS, access to the IDFA requires explicit user consent under the [App Tracking Transparency (ATT) framework](https://developer.apple.com/documentation/AppTrackingTransparency). The IDFV can track users across apps by the same vendor without explicit consent but resets when all of the vendor's apps are removed from the device.

## Impact

- **Violation of User Privacy**: Third parties can build detailed profiles of individuals, estimating interests, health status, sexual orientation, and other personal attributes, resulting in users losing control over their personal information and being subject to unwanted targeting or profiling.
- **Loss of User Trust**: Users can discover undisclosed tracking, resulting in negative reviews, decreased engagement, and reduced retention for the app owner.
- **Legal and Regulatory Non-Compliance**: Tracking users without valid consent can violate data protection laws (like GDPR) and platform guidelines, resulting in fines, legal action, or app store removal for the app owner.

## Mitigations

- **Use Resettable Identifiers**: Prefer [resettable identifiers](https://developer.android.com/privacy-and-security/about#resettable-identifiers) like the [Advertising ID](https://developer.android.com/identity/user-data-ids#advertising-ids) on Android or the [Advertising Identifier (aka. Identifier for Advertisers or IDFA)](https://developer.apple.com/documentation/adsupport/asidentifiermanager/advertisingidentifier) on iOS, for purposes like analytics or personalized advertising. Always respect user preferences and consent regarding tracking and data collection. Avoid using hardware-based identifiers like device IDs or MAC addresses.
- **Use App-Scoped Identifiers**: Use app-scoped identifiers to maintain user privacy and prevent cross-service tracking. Examples include [**ANDROID_ID** (on Android 8.0 (API level 26) and higher)](https://developer.android.com/about/versions/oreo/android-8.0-changes#privacy-all), **Firebase Installation IDs (FIDs)**, or privately stored Globally Unique IDs (GUIDs). On iOS, consider using the **Identifier for Vendors (IDFV)**, which tracks users only across apps by the same vendor and resets when all the vendor's apps are uninstalled.
- **Use Advertising ID Appropriately**: Restrict advertising ID usage to ad-serving and user profiling contexts, respecting user preferences on ad tracking. Avoid linking identifiers after a reset without explicit user consent, ensuring a fresh start. On Android, [use the **Advertising ID** appropriately](https://support.google.com/googleplay/android-developer/answer/9857753#ad-id), and on iOS, comply with **App Tracking Transparency (ATT)** by [requesting user permission](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/requesttrackingauthorization(completionhandler:)) before accessing the **Identifier for Advertisers (IDFA)** and avoid storing it; access [`advertisingIdentifier`](https://developer.apple.com/documentation/adsupport/asidentifiermanager/advertisingidentifier) instead.
- **Use Appropriate APIs**: Use privacy-preserving APIs instead of relying on identifiers. For example, for device verification on Android use **Play Integrity**, and on iOS use **DeviceCheck** (e.g., to identify devices that have taken advantage of a promotional offer or to flag fraudulent devices). For privacy-friendly ad attribution, use the [Attribution Reporting API](https://developers.google.com/privacy-sandbox/private-advertising/attribution-reporting/android) on Android, and consider using **AdAttributionKit** or **SKAdNetwork** on iOS.
- **Treat Third-Party SDKs as Your Own Code**: Be aware of any privacy or security policies associated with third-party SDKs integrated into your app, particularly those related to the use of unique identifiers. Ensure third-party SDKs comply with platform guidelines for data collection and user consent, such as Apple's App Tracking Transparency (ATT) and Google's Play Data Safety policies, to avoid misuse of identifiers and ensure transparency.
- **Provide Clear Privacy Information**: Inform users about the collection and use of unique identifiers in your privacy policy, app store listing, and within the app itself. Clearly explain the purpose of tracking and how it benefits the user experience. Provide users with the ability to opt out of tracking or reset identifiers if possible.
