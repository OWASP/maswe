---
title: Non-Production Resources Not Removed
id: MASWE-0094
alias: non-production-resources
platform: [android, ios]
profiles: [R]
mappings:
  masvs-v1: [MSTG-CODE-4]
  masvs-v2: [MASVS-RESILIENCE-3]
  cwe: [497, 540, 1295]

draft:
  description: The app contains non-production resources that should not be present in production builds, such as non-production URLs, code flows, or verbose logging. These resources help adversaries understand the app's behavior and potentially exploit it (CWE-497), may include sensitive information (CWE-540) or implementation details (CWE-1295).
  topics:
  - non-production URLs
  - code flows
  - verbose logging (e.g., using logging utilities)
  - enabled testing utilities (e.g., StrictMode)
status: placeholder

---

