---
title: Sensitive Data Leaked via Malicious Embedded Libraries
id: MASWE-xxxA
alias: data-leak-malicious-libraries
platform: [android, ios]
profiles: [???]
mappings:
  masvs-v2: [MASVS-PLATFORM-3, MASVS-STORAGE-2]
cwe: [200, 359]
draft:
  description: Any embedded third-party library can act as inadvertently or maliciously leak sensitive data to external services, i.e. after an version update, or an issue in the supply chain. These libraries have access to e.g. ApplicationContext on Android or the full app memory on iOS. This gives them access to read data stored on the disk or in memory and thus could act as an insider threat within the app's process and boundaries. Apply supply chain security best practices to ensure the integrity of embedded libraries. 
status: placeholder

---
