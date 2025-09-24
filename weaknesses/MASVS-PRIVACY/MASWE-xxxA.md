---
title: Sensitive Data Leaked via Embedded Libraries
id: MASWE-xxxA
alias: data-leak-libraries
platform: [android, ios]
profiles: [L1, L2]
mappings:
  masvs-v2: [MASVS-PLATFORM-3, MASVS-STORAGE-2]
cwe: [200, 359]
draft:
  description: Embedded third-party libraries (e.g. analytics, advertising, or crash reporting) can leak sensitive data to external services. Review the usage of embedded libraries to ensure they do not leak sensitive data outside of the expected SLA.
status: placeholder

---
