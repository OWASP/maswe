---
title: Non-Reproducible Builds
id: MASWE-0075
alias: non-reproducible-builds
requirement: "The app offers reproducible builds."
platform: [android, ios]
profiles: [P]
threat: MAS-THREAT-0075
attacks: [MAS-ATTACK-0060, MAS-ATTACK-0062]
mappings:
  masvs-v2: [MASVS-PRIVACY-3]
  cwe: [1357, 494]
refs:
- https://reproducible-builds.org/
- https://slsa.dev/
- https://github.com/signalapp/Signal-Android/blob/main/reproducible-builds/README.md
---

## Overview

This weakness occurs when compiling the app's source with the same build environment does not yield a bit-for-bit identical binary, making it impossible to independently verify that a distributed binary was built from the claimed, unmodified source.

Reproducible builds allow third parties, and the developers themselves, to detect tampering or injected malicious code by rebuilding from source and comparing the result with the released artifact. Without reproducibility, this verification is impossible, weakening supply-chain integrity. Together with build provenance and attestation frameworks (e.g. SLSA), reproducible builds let stakeholders verify the integrity of released artifacts.

## Modes of Introduction

- **Source Code Not Available**: Not making the source code used to build the app available.
- **Non-Deterministic Build Outputs**: Embedding timestamps, absolute paths, environment data, or unstable orderings in build artifacts, so identical inputs produce differing outputs.
- **Unpinned Build Environments**: Building with undocumented or unpinned toolchains and dependencies, so it's impossible to recreate the environment that produced a release.
- **No Provenance or Attestation**: Publishing releases without provenance describing what was built, from which source, and by which pipeline.
- **Applying Non-Deterministic Obfuscation Controls**: By applying non-deterministic obfuscation controls, each build will generate a new random binary which cannot directly be compared with previous builds from the same code.

## Impact

- **Execution of Unauthorized Code**: Attackers can inject code during the build or distribution process without straightforward detection, since no independent party can verify the binary against the source, resulting in malicious code shipping to the entire user base.
- **Loss of User Trust**: Users and auditors cannot verify that the shipped app matches the published source, resulting in weakened trust in the app, particularly for security- and privacy-sensitive apps.

## Mitigations

- **Make Source Code Available**: Make the source code used to build the app available, including any build scripts, so third parties can attempt to reproduce the build.
- **Make Builds Deterministic**: Eliminate timestamps, absolute paths, environment-dependent data, and unstable orderings from build outputs, following [reproducible-builds.org](https://reproducible-builds.org/) guidance.
- **Pin and Document the Build Environment**: Define the exact toolchain and dependency versions in version control so any party can recreate the build environment.
- **Publish Provenance and Attestations**: Generate build provenance (e.g. per [SLSA](https://slsa.dev/)) and, where feasible, publish verification instructions so third parties can reproduce and compare releases.
- **Use Deterministic Obfuscation Techniques**: Use obfuscation techniques which will always generate the same deterministic result.
