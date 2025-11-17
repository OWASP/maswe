---
title: Dependencies Known to be Malicious
id: MASWE-xxxB
alias: data-leak-malicious-libraries
platform: [android, ios]
profiles: [L1,L2]
mappings:
  masvs-v2: [MASVS-CODE-3]
cwe: [829]
draft:
  description: |
    Embedding third-party libraries known to be malicious may be risky. Such libraries act as an insider threat from within the app's process and boundaries. To mitigate apply chain security best practices, such as Software composition analysis (SCA) (generate a Bill of Materials (BOM), which is then compared against a variety of databases) to ensure the integrity of embedded libraries.
status: placeholder

---
