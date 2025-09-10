---
title: Device Attestation Not Implemented
id: MASWE-0100
alias: device-attestation
platform: [android, ios]
profiles: [R]
mappings:
  masvs-v1: [MSTG-RESILIENCE-10]
  masvs-v2: [MASVS-RESILIENCE-1]
  cwe: [693]

refs:
- https://developer.android.com/google/play/integrity
- https://support.google.com/googleplay/android-developer/answer/11395166?hl=en
- https://www.youtube.com/watch?v=TyxL78e5Bag
- https://github.com/1nikolas/play-integrity-checker-app
- https://developer.apple.com/videos/play/wwdc2021/10244/ 
- https://developer.apple.com/documentation/devicecheck/preparing-to-use-the-app-attest-service 
- https://github.com/iansampson/AppAttest 
- https://github.com/firebase/firebase-ios-sdk/blob/v8.15.0/FirebaseAppCheck/Sources/AppAttestProvider/DCAppAttestService%2BFIRAppAttestService.h 
- https://blog.restlesslabs.com/john/ios-app-attest
status: new

---

## Overview

Device attestation is a security mechanism that allows a mobile application or backend service to verify the integrity and trustworthiness of the environment in which the application is running. It provides cryptographic proof that the device has not been tampered with.

In this context it need to be differentiated between attestation and assertion:

- **Attestation** - Occurs during the registration phase, when your app initially connects to your server.
- **Assertion** - Is used during subsequent interactions, whenever the app needs to authenticate again or make further requests.

If device attestation is used also app attestation should be considered to confirm that the application instance is genuine. App attestation provides cryptographic proof that the app instance is trustworthy and genuine.

Attestation can be performed locally on the device or remotely through a backend service. Local checks rely on the application itself to verify system integrity, but these can be bypassed by attackers with sufficient control over the environment (e.g., through hooking and modifying the app during runtime). Server-side attestation shifts the verification to a backend service, which can make it harder for attackers to tamper with the verification logic.

To summarize:

- **Device attestation** confirms the environment is trustworthy.
- **App attestation** confirms the app instance is trustworthy.

If the app doesn't use attestation APIs or services the backend cannot ensure requests originate from a genuine app binary and from a trusted platform.

## Impact

- **Abuse of Functionality**: Backend systems cannot distinguish between legitimate and tampered apps, enabling abuse such as fake account creation, fraud or unauthorized use of premium features.
- **App Executed in outdated Environment**: Users may run the application on outdated platforms that have no security patches installed.
- **App Executed in untrusted Environment**: Attackers may run the application on rooted or jailbroken devices without detection.

## Mode of Introduction

- **Weak Architecture**: The application does not include device attestation in its security model, assuming the device environment can be trusted.
- **Reliance on Weak Checks**: Instead of proper attestation, the app only performs basic root/jailbreak detection, which is easily bypassed.  
