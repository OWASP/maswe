---
title: Step-Up Authentication Not Implemented for Sensitive Actions
id: MASWE-0023
alias: step-up-auth
requirement: "The app enforces step-up authentication before granting access to sensitive functionality."
platform: [android, ios]
profiles: [L2]
threat: MAS-THREAT-0023
attacks: [MAS-ATTACK-0032, MAS-ATTACK-0033]
mappings:
  masvs-v1: [MSTG-AUTH-10]
  masvs-v2: [MASVS-AUTH-3, MASVS-PLATFORM-3]
  cwe: [306]
  android-core-app-quality: [Biometric_Authentication]
  maswe-beta: [MASWE-0029]
refs:
- https://developer.apple.com/documentation/localauthentication
- https://auth0.com/blog/what-is-step-up-authentication-when-to-use-it/
- https://pages.nist.gov/800-63-4/sp800-63b.html
---

## Overview

This weakness occurs when an app allows sensitive actions to be performed within an already authenticated session without requiring the user to re-confirm their identity.

Step-up authentication requires the user to re-authenticate or provide an additional authentication factor before performing a sensitive action, even within an active session.

For example, a user logged into their bank account who requests a large transfer to an unknown payee should be required to re-confirm their identity (e.g. via biometrics or a second factor) so that only the legitimate user can complete the action. Without it, whoever holds the active session, not necessarily the legitimate user, can perform every operation the account allows.

Depending on the context, other sensitive actions may include:

- Changing account data such as password, email address or phone number
- Elevating a user role
- Disabling security features such as multifactor authentication (MFA)
- Displaying sensitive data such as credit card number / PAN

## Modes of Introduction

- **No Re-Authentication for Sensitive Actions**: Allowing high-risk operations, such as payments, credential or profile changes, or the display of sensitive personal data, with only the assurance of the initial login.
- **Step-Up Not Bound to the Action**: Implementing a re-authentication challenge that is not tied to the specific transaction being approved, so a single approval can be reused for a different or modified action.
- **Step-Up Not Enforced Server-Side**: Step-up authentication is only performed by app and not by the server.
- **Uniform Assurance Level**: Designing all functionality behind a single login assurance level without classifying operations by risk.

## Impact

- **Financial Loss**: Attackers can initiate transfers or purchases in the victim's session, resulting in direct financial harm to the user.
- **Compromise of Sensitive Data**: Attackers can view or export sensitive personal data available in the session, resulting in unauthorized disclosure of user information.
- **Authentication or Authorization Bypass**: Attackers can change the account's credentials or security settings without any additional challenge, resulting in persistent account takeover.

## Mitigations

- **Classify Actions by Risk**: Define which operations require step-up authentication and match the required assurance level to the sensitivity of each action.
- **Require Step-Up for Sensitive Actions**: Re-authenticate the user, e.g. with biometrics bound to a keystore-protected key or an additional factor, before executing high-risk operations or displaying highly sensitive data.
- **Bind the Challenge to the Action**: Tie the step-up challenge cryptographically to the specific transaction (e.g. transaction signing), so an approval cannot be replayed or applied to a different action.
- **Enforce Step-Up Server-Side**: Have the server require and verify step-up evidence before executing the action, rather than trusting a client-side check.
