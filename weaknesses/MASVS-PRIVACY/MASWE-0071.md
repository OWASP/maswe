---
title: Inadequate Defaults for Privacy Relevant Actions
id: MASWE-0071
alias: unsafe-defaults-privacy-actions
requirement: "The app uses adequate defaults for privacy relevant actions."
platform: [android, ios]
profiles: [P]
threat: MAS-THREAT-0071
attacks: [MAS-ATTACK-0084, MAS-ATTACK-0087]
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

This weakness occurs when an app uses defaults for a privacy relevant action that expose more data than is necessary for the expected functionality.

Privacy relevant actions include sharing, exporting, publishing, synchronizing, backing up, changing visibility, responding to a request from another party, or moving data from private app storage to storage or services accessible by other applications, users, or third parties.

The weakness may cause users to disclose different data, disclose data to a broader audience, or create more persistent copies than they reasonably intended. The issue is whether the default configuration results in a more exposing privacy state than is necessary for the requested functionality.

## Modes of Introduction

- **Unclear Disclosure Context**: The interface or action labels do not clearly identify the affected records, files, accounts, data elements, included metadata, destination, audience, or resulting privacy state, including when responding to another party's request for data.
- **Overly Exposing Defaults**: The app preselects broader audiences, more data, longer retention, public visibility, or additional recipients when a less exposing default would satisfy the expected functionality.

## Impact

- **Violation of User Privacy**: The app can disclose personal or sensitive data to recipients who are not entitled to receive it under the user's sharing choices, resulting in unauthorized exposure of that data.
- **Loss of User Trust**: Users can discover that the app shared more data, or shared it more broadly, than they reasonably expected, resulting in reduced confidence in the app and its owner.
- **Legal and Regulatory Non-Compliance**: The app can share personal data using unnecessarily exposing defaults, resulting in violations of privacy obligations and potential enforcement action.

## Mitigations

- **Provide Clear Disclosure Context and Control**: At the point of action, show the affected data, included metadata, destination, audience, and material privacy consequences; before responding to another party's request for data, identify the requester and recipient and allow the user to approve, limit, or decline the disclosure.
- **Use Privacy Protective Defaults**: Default to the narrowest audience, smallest data set, shortest appropriate persistence, and least exposing destination that supports the requested functionality.
