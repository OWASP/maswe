---
title: Dependencies Know to be Malicious
id: MASWE-xxxB
alias: data-leak-malicious-libraries
platform: [android, ios]
profiles: [L1,L2]
mappings:
  masvs-v2: [MASVS-PLATFORM-3, MASVS-STORAGE-2]
cwe: [200, 359]
draft:
  description: Embedded third-party libraries known to be malicious can leak sensitive data to external services. These libraries have access to e.g. ApplicationContext on Android or the full app memory on iOS. This gives them access to read data stored on the disk or in memory and thus could act as an insider threat within the app's process and boundaries. Apply supply chain security best practices to ensure the integrity of embedded libraries such as SBOM checks.
status: placeholder

---
