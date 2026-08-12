---
title: Dependencies with Known Vulnerabilities
id: MASWE-0044
alias: dependencies-with-known-vulnerabilities
requirement: "The app's third-party components are regularly checked for known vulnerabilities."
platform: [android, ios]
profiles: [L1, L2]
threat: MAS-THREAT-0044
attacks: [MAS-ATTACK-0073]
mappings:
  masvs-v1: [MSTG-CODE-5]
  masvs-v2: [MASVS-CODE-3]
  cwe: [1395, 1357]
  android-risks:
  - insecure-library
  - unsafe-download-manager
  android-core-app-quality: [SDK_Maintenance, Security_Provider_Initialization]
  maswe-beta: [MASWE-0076]
refs:
- https://www.cisa.gov/sites/default/files/2023-04/sbom-types-document-508c.pdf
- https://www.ntia.doc.gov/files/ntia/publications/sbom_minimum_elements_report.pdf
- https://developer.android.com/guide/practices/sdk-best-practices
- https://developer.android.com/privacy-and-security/security-best-practices#services-dependencies-updated
- https://developer.android.com/privacy-and-security/security-best-practices#update-dependencies
- https://support.google.com/googleplay/android-developer/answer/14514531
- https://support.google.com/googleplay/android-developer/answer/13326895
- https://developer.apple.com/support/third-party-SDK-requirements/
- https://www.youtube.com/watch?v=3klmiHX0uVQ
- https://developer.apple.com/videos/play/wwdc2023/10060/
---

## Overview

This weakness occurs when an app includes third-party libraries, software development kits (SDKs), or frameworks that contain publicly known vulnerabilities.

Mobile apps often depend on such components, either open-source components maintained by the community or closed-source products provided by commercial vendors, to implement functionality, streamline development, or integrate platform services. Vulnerabilities in dependencies can be more easily exploited than vulnerabilities in first-party code because they (and some exploits) are often documented in public databases, such as the CVE list, or accessible through security advisories.

**The developer is responsible** for ensuring all dependencies are secure and up to date because they are part of the app's codebase and therefore extend the app's attack surface. Google and Apple emphasize this in their security best practices:

!!! quote "Google's [Using SDKs safely and securely](https://support.google.com/googleplay/android-developer/answer/13326895)"

    "If you include an SDK in your app, you are responsible for ensuring that their third-party code and practices are compliant with Google Play Developer Program Policies and do not cause your app to violate policies."

!!! quote "Apple's [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)"

    "You are responsible for making sure everything in your app complies with these guidelines, including ad networks, analytics services, and third-party SDKs, so review and choose them carefully."

In terms of privacy, dependencies can introduce risks if they collect or transmit user data without proper consent or transparency. Both Google and Apple require third-party SDKs used in apps to comply with their privacy policies and guidelines to ensure user data is handled securely and transparently. It is the developer's responsibility to ensure that any third-party libraries or SDKs used in the app adhere to these requirements, even if the libraries themselves are not under their direct control and even if they don't use the specific code that could violate the platform's policies.

!!! quote "Google's [Using SDKs safely and securely](https://support.google.com/googleplay/android-developer/answer/13326895)"

    "App developers are required to treat any data collection from within their app by an SDK as if they collected it directly."

!!! quote "Apple's [Third-party SDK requirements](https://developer.apple.com/support/third-party-SDK-requirements/)"

    "When you use a third-party SDK with your app, you are responsible for all the code the SDK includes in your app, and need to be aware of its data collection and use practices.

For more information on privacy and data collection declarations, see @MASWE-0073.

## Modes of Introduction

- **Direct Dependencies**: Including vulnerable dependencies either manually (by copying and linking source or binary files) or, more commonly, via package managers and build tools (e.g., Gradle, CocoaPods, Swift Package Manager). This includes both first- and third-party SDKs, and may involve both statically and dynamically linked libraries.
- **Transitive Dependencies**: Pulling in vulnerable dependencies indirectly through other libraries or SDKs that the app uses, even if the app does not directly include the vulnerable library itself.
- **Dynamically Loaded Dependencies**: Loading libraries dynamically at runtime, which can make it difficult to track and manage dependencies and can lead to a vulnerable version being used without the developer's knowledge.
- **Outdated Platform Security Components**: Relying on platform-provided security components, such as cryptographic libraries or SSL/TLS implementations, that are outdated or lack timely updates. For instance, on Android, the system's security provider responsible for secure network communications must be explicitly updated by the developer at app startup.
- **Usage of Third-Party Frameworks**: Building the app on a third-party application framework such as Flutter or React Native, where the framework itself, as well as any platform-specific bindings, may contain vulnerabilities.

## Impact

- **Compromise of Sensitive Data**: Attackers can exploit vulnerable components to bypass access controls or cryptographic protections and expose credentials, session tokens, or personally identifiable information (PII), resulting in data breaches with legal, financial, and reputational consequences for the app owner.
- **Execution of Unauthorized Code**: Attackers can exploit vulnerabilities in embedded dependencies to execute arbitrary code within the app's context (e.g., through code injection), escalate privileges, or manipulate app behavior, resulting in compromised user accounts, abuse of backend services, or persistent access to protected resources.
- **Legal and Regulatory Non-Compliance**: Shipping dependencies with publicly known CVEs can violate regulatory requirements (e.g., GDPR, HIPAA, PCI-DSS) or platform security policies (e.g., Google Play or App Store guidelines), resulting in app rejection, fines, or mandatory disclosures for the app owner.

## Mitigations

- **Use a Software Bill of Materials (SBOM)**: Produce and maintain an SBOM to track all components and transitive dependencies, ensuring visibility and accountability for third-party code. See [NIST SSDF (NIST SP 800-218) PS.3.2](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf), [NTIA The Minimum Elements For a Software Bill of Materials (SBOM)](https://www.ntia.doc.gov/files/ntia/publications/sbom_minimum_elements_report.pdf), [CISA SBOM Types document](https://www.cisa.gov/sites/default/files/2023-04/sbom-types-document-508c.pdf) for more information on SBOMs and their importance in managing software dependencies.
- **Update Dependencies Responsibly**: As part of secure [dependency management](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.html), regularly monitor all used third-party dependencies for security-related updates (for example, by using Software Composition Analysis (SCA) tools and SBOMs in your CI/CD pipelines). Apply updates when they fix known vulnerabilities, and pin versions explicitly to prevent unexpected changes and reduce the risk of supply-chain attacks.
- **Remove Unused or Obsolete Dependencies**: Periodically review and eliminate unused, legacy, or unnecessary libraries to reduce the app's attack surface and dependency footprint.
- **Use Trusted Sources**: Only include libraries and SDKs from reputable sources, such as official repositories or well-maintained open-source projects, to minimize the risk of introducing malicious or vulnerable code.
