---
title: Inadequate or Ambiguous User Consent Mechanisms
id: MASWE-0078
alias: ambiguous-consent-mechanisms
requirement: "The app requests user consent prior to any data processing."
platform: [android, ios]
profiles: [P]
threat: MAS-THREAT-0078
attacks: [MAS-ATTACK-0085, MAS-ATTACK-0086]
mappings:
  masvs-v2: [MASVS-PRIVACY-4]
  cwe: [200, 285, 358, 359]
  maswe-beta: [MASWE-0115, MASWE-0060]
refs:
- https://developer.apple.com/design/human-interface-guidelines/privacy#Requesting-permission
- https://developer.apple.com/documentation/uikit/protecting_the_user_s_privacy/requesting_access_to_protected_resources
- https://developer.android.com/training/permissions/requesting#explain
---

## Overview

This weakness occurs when an app processes personal data without obtaining consent that is explicit, informed, and given prior to the processing, or when the consent request is vague, bundled, or coercive.

According to various international privacy regulations, such as the [EU's GDPR](https://gdpr-info.eu/art-7-gdpr/), [California's CCPA](https://cppa.ca.gov/regulations/pdf/cppa_act.pdf), [Brazil's LGPD](https://lgpd-brazil.info/chapter_02/article_08), and [Canada's PIPEDA](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/p_principle/principles/p_consent/), users must be made fully aware of the purposes of the data collection, as well as the potential consequences of providing consent. Consent should be an active choice, specific to the data being processed, and not bundled with other service agreements or presented in a vague or coercive manner.

In addition, users must be able to easily withdraw their consent at any time and should be clearly informed of how to do so, including the potential impact on the functionality of the app. Developers must maintain a record of user consent and ensure that consent requests are clear, separate from other terms, and legally valid, and avoid practices that obscure the full scope of data processing.

## Modes of Introduction

- **Failure to Prompt for Consent Changes**: Failing to prompt the user for consent when data collection practices change or when additional data is collected beyond what was originally specified.
- **Ambiguous Consent Mechanisms**: Bundling consent with terms of service, often covering future use cases without notifying the user again, or implying consent when the user doesn't explicitly deny access.

## Impact

- **Violation of User Privacy**: Users can unknowingly give up control over their data, resulting in its use for purposes they may find objectionable or harmful, such as targeted advertising, profiling, discrimination, or even identity theft.
- **Loss of User Trust**: Users can lose trust in the app and abandon it, share negative reviews, or discourage others from using it, resulting in reputational damage and potential loss of business for the app owner.
- **Legal and Regulatory Non-Compliance**: Processing data without valid consent can violate laws and platform requirements, resulting in legal consequences, fines, or removal from app stores for the app owner.

## Mitigations

- **Prompt for Consent on Changes**: Establish mechanisms for prompting users for consent if data collection practices change or if additional data is being collected, ensuring transparency when app functionality evolves.
- **Obtain Clear and Explicit User Consent for Immediate Actions**: Before accessing sensitive resources like sensors or local data (e.g., camera, location), always request explicit permission from the user. Clearly explain why the permission is needed, using mechanisms like [purpose strings](https://developer.apple.com/documentation/uikit/protecting_the_user_s_privacy/requesting_access_to_protected_resources) on iOS or [similar prompts](https://developer.android.com/training/permissions/requesting#explain) on Android, to ensure users understand the immediate use of their data.
- **Ensure Informed and Transparent Consent**: Provide users with clear, specific information about what data will be collected, how it will be used, and the potential impact. Consent should not be hidden in terms of service or bundled for future uses. Users must confirm consent separately for each purpose, especially when permissions extend beyond the initial request.
