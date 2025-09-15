---
title: Insecure Deep Links
id: MASWE-0058
alias: insecure-deep-links
platform: [android, ios]
profiles: [L1, L2]
mappings:
  masvs-v1: [MSTG-PLATFORM-3]
  masvs-v2: [MASVS-PLATFORM-1, MASVS-STORAGE-2, MASVS-CODE-4]
  cwe: [939, 917]
refs:
- https://developer.apple.com/documentation/technotes/tn3155-debugging-universal-links
- https://developer.android.com/training/app-links/verify-android-applinks
status: new
---

## Overview

Mobile apps often accept deep links to navigate to particular sections within the app or perform specific functionality. However, if not implemented securely, they can introduce vulnerabilities. Insecure deep links can lead to unauthorized access, data leakage, fault injection, command injection, phishing attempts or other security issues if they are not properly validated and sanitized.

## Impact

- **Unauthorized Access**: Attackers can exploit insecure deep links to access restricted areas of the app or perform actions without proper authentication or authorization.
- **Phishing Attacks**: In combination with webviews, attackers can craft deep links that lead users to malicious (brand-alike) websites, potentially stealing sensitive information.
- **Injection Attacks**: Malformed deep link parameters can be exploited to perform injection attacks such as command injection, or fault injection.
- **Reputation Damage**: Exploitation of insecure deep links can lead to negative publicity and loss of user trust.
- **App Crashes**: Improper handling of deep link parameters can lead to application crashes or unexpected behavior, affecting the user experience.

## Mode of Introduction

- **Too Wide URL parameter Acceptance**: Accepting deep links from untrusted domains or allowing overly broad URL patterns such as wildcard schemes.
- **Improper Configuration**: Misconfiguring deep link handling, such as not restricting which domains can open the app, can lead to unauthorized access.
- **Lack of Input Validation**: Failing to validate and sanitize deep link parameters can allow attackers to inject malicious input.
- **Excessive Permissions**: Granting deep links access to sensitive app functionality or data without proper checks.
- **Insecure WebView Integration**: If deep links open content in a WebView without proper security measures, it can lead to vulnerabilities like cross-site scripting.
- **Inadequate Logging and Monitoring**: Failing to log deep link usage and monitor for suspicious activity can delay the detection of exploitation attempts.

## Mitigations

- Restrict Accepted Domains and parameters: Limit deep link handling to trusted domains and specific URL patterns. Avoid using wildcards in schemes or hostnames.
- Validate and Sanitize Input: Always validate and sanitize deep link parameters to ensure they conform to expected formats and values.
- Implement Proper Authorization Checks: Ensure that deep links do not bypass authentication or authorization mechanisms.
- Secure WebView Usage: If using WebViews, ensure they are configured securely to prevent vulnerabilities like cross-site scripting, clickjacking or redirecting to malicious sites.
- Fuzz Testing: Use fuzz testing to identify potential vulnerabilities in deep link handling.
- Log and Monitor: Implement logging for deep link usage and monitor for unusual patterns that may indicate exploitation attempts.
