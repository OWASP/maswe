---
title: Fallback to Non-biometric Credentials Allowed for Sensitive Transactions
id: MASWE-0021
alias: no-biometric-fallback
requirement: "The app does not allow fallback to non-biometric credentials for sensitive transactions."
platform: [android, ios]
profiles: [L2]
threat: MAS-THREAT-0021
attacks: [MAS-ATTACK-0034]
mappings:
  masvs-v2: [MASVS-AUTH-2]
  cwe: [288, 287]
  android-core-app-quality: [Biometric_Authentication]
  maswe-beta: [MASWE-0045]
refs:
- https://developer.android.com/training/sign-in/biometric-auth#allow-fallback
- https://developer.apple.com/documentation/localauthentication/logging_a_user_into_your_app_with_face_id_or_touch_id#3148834
- https://developer.apple.com/documentation/localauthentication/lapolicy/deviceownerauthenticationwithbiometrics/
---

## Overview

This weakness occurs when authentication for a sensitive transaction can silently fall back from biometrics to a weaker device credential such as a PIN, pattern, or password.

Device credentials are typically short, reusable, and observable, so allowing them as a fallback drops the assurance level below what a high-value operation requires. On Android, this happens when `DEVICE_CREDENTIAL` is permitted as an authenticator (e.g. via `BiometricPrompt.setAllowedAuthenticators`) for a sensitive action; on iOS, when `LAPolicy.deviceOwnerAuthentication` is used instead of `LAPolicy.deviceOwnerAuthenticationWithBiometrics`. Sensitive transactions should require biometrics and be bound to a biometric-protected key rather than permitting a non-biometric fallback.

## Modes of Introduction

- **Device Credential Allowed for Sensitive Actions**: Permitting `DEVICE_CREDENTIAL` as an accepted authenticator for high-value operations on Android.
- **Generic Authentication Policy on iOS**: Using `LAPolicy.deviceOwnerAuthentication`, which allows passcode fallback, instead of `LAPolicy.deviceOwnerAuthenticationWithBiometrics` for sensitive operations.
- **Operation Not Bound to a Biometric-Only Key**: Protecting the sensitive operation with a UI-level prompt rather than a keystore key that only unlocks with strong biometric authentication.

## Impact

- **Authentication or Authorization Bypass**: Attackers can complete authentication challenges intended to require the user's biometrics, resulting in unauthorized approval of sensitive operations.
- **Financial Loss**: Attackers can authorize payments or transfers with a stolen device and its credential, resulting in direct financial harm to the user.

## Mitigations

- **Require Biometrics for Sensitive Transactions**: Configure the authentication prompt to accept only strong biometrics (e.g. `BIOMETRIC_STRONG` on Android, `LAPolicy.deviceOwnerAuthenticationWithBiometrics` on iOS) for high-value operations.
- **Bind Operations to Biometric-Only Keys**: Protect the operation with a keystore key that requires strong biometric authentication for use and is invalidated on new biometric enrollments (see @MASWE-0022).
- **Match Assurance to Sensitivity**: Allow device-credential fallback only for low-risk convenience features, never for the transactions that motivated biometric protection in the first place.
