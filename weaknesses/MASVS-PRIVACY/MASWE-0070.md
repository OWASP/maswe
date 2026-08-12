---
title: Inadequate Awareness for Privacy Relevant Actions
id: MASWE-0070
alias: inadequate-awareness-privacy-actions
requirement: "The app informs the user about the privacy implications before performing an action."
platform: [android, ios]
profiles: [P]
threat: MAS-THREAT-0070
attacks: [MAS-ATTACK-0084]
mappings:
  masvs-v2: [MASVS-PRIVACY-2]
  cwe: [359]
  maswe-beta: [MASWE-0109]
refs:
- https://cloud.google.com/sensitive-data-protection/docs/classification-redaction
- https://gdpr-info.eu/recitals/no-26/
- https://gdpr-info.eu/recitals/no-28/
- https://gdpr-info.eu/art-4-gdpr/
- https://www.edpb.europa.eu/topics/ai-and-technology/anonymisation-pseudonymisation_en
- https://ec.europa.eu/justice/article-29/documentation/opinion-recommendation/files/2014/wp216_en.pdf
- https://www.statista.com/topics/9460/app-tracking-and-mobile-privacy/
---

## Overview

This weakness occurs when an app performs a privacy relevant action without making its scope or material consequences reasonably apparent to the user.

Privacy relevant actions include sharing, exporting, publishing, synchronizing, backing up, changing visibility, responding to a request from another party, or moving data from private app storage to storage or services accessible by other applications, users, or third parties.

The weakness may cause users to disclose different data, disclose data to a broader audience, or create more persistent copies than they reasonably intended. It includes flows where the app honors another party's request for data without clearly showing the user what will be shared and with whom, or allowing the user to control the disclosure. It does not require the underlying processing to rely on consent. The issue is whether the interface allows the user to understand and control the resulting privacy state.

## Modes of Introduction

- **Unclear Disclosure Context**: The interface or action labels do not clearly identify the affected records, files, accounts, data elements, included metadata, destination, audience, or resulting privacy state, including when responding to another party's request for data.
- **Insufficient Disclosure Review and Feedback**: The app does not allow the user to review, control, or confirm a consequential disclosure, or clearly indicate that a high impact or difficult to reverse disclosure has occurred.

## Impact

- **Violation of User Privacy**: The app can disclose personal or sensitive data to recipients who are not entitled to receive it under the user's sharing choices, resulting in unauthorized exposure of that data.
- **Loss of User Trust**: Users can discover that the app shared data without their awareness or control, resulting in reduced confidence in the app and its owner.
- **Legal and Regulatory Non-Compliance**: The app can share personal data without adequate transparency or user control, resulting in violations of privacy obligations and potential enforcement action.

## Mitigations

- **Provide Clear Disclosure Context and Control**: At the point of action, show the affected data, included metadata, destination, audience, and material privacy consequences; before responding to another party's request for data, identify the requester and recipient and allow the user to approve, limit, or decline the disclosure.
- **Support Review and Reversal of Consequential Disclosures**: Before completion, allow users to review selected items, recipients, audience, included metadata, and visibility; make the resulting privacy state visible and provide proportionate confirmation or undo mechanisms when practical.
