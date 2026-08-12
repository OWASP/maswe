---
title: Unnecessary Exposure of Sensitive Data via Notifications
id: MASWE-0037
alias: data-leak-notifications
requirement: "The app does not unnecessarily expose sensitive data through system notifications."
platform: [android, ios]
profiles: [L2]
threat: MAS-THREAT-0037
attacks: [MAS-ATTACK-0044, MAS-ATTACK-0045]
mappings:
  masvs-v2: [MASVS-PLATFORM-3, MASVS-STORAGE-2]
  cwe: [200, 359]
  maswe-beta: [MASWE-0054]
refs:
- https://developer.android.com/develop/ui/views/notifications/build-notification#lockscreenNotification
- https://developer.apple.com/documentation/usernotifications
- https://developer.apple.com/documentation/usernotifications/generating-a-remote-notification
- https://developer.apple.com/documentation/usernotifications/unnotificationcategory/hiddenpreviewsbodyplaceholder
- https://developer.apple.com/documentation/usernotifications/unnotificationcategoryoptions/hiddenpreviewsshowtitle
- https://developer.apple.com/documentation/usernotifications/unnotificationcategoryoptions/hiddenpreviewsshowsubtitle
---

## Overview

This weakness occurs when an app includes more sensitive data (such as one-time codes, message contents, or account details) than necessary in a system notification.

Notifications can be rendered on the lock screen, and therefore, anyone holding the device can read them without unlocking it. They also can be read by other apps that hold notification access, if the platform allows it (e.g. an Android [`NotificationListenerService`](https://developer.android.com/reference/android/service/notification/NotificationListenerService)). Any sensitive value included in a notification therefore leaves the app's control the moment it is posted.

## Modes of Introduction

- **Sensitive Content in Notifications**: Including one-time codes, message contents, financial details, or other sensitive values directly in notification titles or bodies when a generic notification would suffice.
- **No Lock-Screen Redaction**: Not configuring notification visibility so that sensitive content is redacted or hidden on the lock screen.

## Impact

- **Compromise of Sensitive Data**: Unauthorized observers or, where applicable, apps with notification-listener access may obtain personal, financial, authentication, or account information contained in notifications.
- **Authentication or Authorization Bypass**: Attackers may use exposed credentials or still-valid one-time codes to access an account, perform unauthorized transactions, or carry out other sensitive actions.

## Mitigations

- **Minimize Notification Content**: Use notifications only to indicate that an event occurred, and retrieve sensitive details inside the app after appropriate authentication and authorization. For iOS remote notifications, follow Apple's [remote-notification payload guidance](https://developer.apple.com/documentation/usernotifications/generating-a-remote-notification) and keep user-visible alert content non-sensitive by default. Do not place sensitive data in the title because private notifications may still display basic information including the title.
- **Configure Lock-Screen/Preview Redaction**: On Android, use [`NotificationCompat.Builder.setVisibility()` and `setPublicVersion()`](https://developer.android.com/develop/ui/views/notifications/build-notification#lockscreenNotification): `VISIBILITY_PRIVATE` with a generic public version when a redacted notification may be shown, or `VISIBILITY_SECRET` when it should not appear on a secure lock screen at all. On iOS, provide a generic [`hiddenPreviewsBodyPlaceholder`](https://developer.apple.com/documentation/usernotifications/unnotificationcategory/hiddenpreviewsbodyplaceholder) and avoid enabling [`hiddenPreviewsShowTitle`](https://developer.apple.com/documentation/usernotifications/unnotificationcategoryoptions/hiddenpreviewsshowtitle) or [`hiddenPreviewsShowSubtitle`](https://developer.apple.com/documentation/usernotifications/unnotificationcategoryoptions/hiddenpreviewsshowsubtitle) unless those fields are safe to display — these only customize the preview once it is already hidden, they do not force it to be hidden.
