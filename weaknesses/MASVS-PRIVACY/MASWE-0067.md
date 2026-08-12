---
title: Lack of Anonymization or Pseudonymisation Measures
id: MASWE-0067
alias: anonymization-pseudonymization-measures
requirement: "The app uses anonymization or pseudonymisation measures."
platform: [android, ios]
profiles: [P]
threat: MAS-THREAT-0067
attacks: [MAS-ATTACK-0074, MAS-ATTACK-0078]
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

This weakness occurs when an app processes or shares user data without applying anonymization, or pseudonymization measures allowing individuals to be identified and potentially tracked across different services and over time.

Anonymization uses techniques such as randomization or generalization to irreversibly prevent identification. Pseudonymization replaces identifiable data with tokens or hashed values, but may remain reversible when additional information is available.

## Modes of Introduction

- **Identifiers Not Removed**: Failing to remove or transform identifiers, such as user ID or name, before server-side collection.
- **Pseudonymization Implemented Insecurely**: Using predictable or stable hashes, reusing pseudonyms across unrelated contexts, or storing keys or mapping data together with the pseudonymized data.
- **Sensitive Metadata Not Removed**: Failing to remove private or sensitive metadata, such as geolocation from Exif data, before server-side collection.
- **Sensitive Data Not Redacted Before Sending to AI Services**: Sending unredacted sensitive or personal data to AI services.

## Impact

- **Violation of User Privacy**: Third parties can profile users and target them with advertising without consent, resulting in the loss of users' control over their personal information, retention and its unforeseen use, e.g. to train AI models.
- **Legal and Regulatory Non-Compliance**: Processing personal data without de-identification safeguards can violate data protection laws and regulations (like GDPR), resulting in legal consequences and fines for the app owner.
- **Loss of User Trust**: Unexpected identification, tracking, or secondary use of personal data can reduce user confidence in the app.

## Mitigations

- **Use Anonymisation and Pseudonymisation**: Ensure techniques like anonymisation and pseudonymisation are implemented to prevent user identification.
- **Redact Sensitive Data Before Sending to AI Services**: Before sending data to AI services, redact or mask sensitive fields and identifiers so that personal data is not exposed to (or used to train) third-party models.
