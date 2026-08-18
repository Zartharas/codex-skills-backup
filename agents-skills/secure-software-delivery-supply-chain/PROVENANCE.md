# Upgrade provenance

Version 2.0.0 upgrades the user's prior instruction-only `secure-software-delivery-supply-chain` package while preserving its domain boundary and source-map record.

The v2 wording was rewritten to remove transient incident statistics, avoid hard-coded "safe" version floors, prevent automatic tool installation, enforce secret redaction, and treat scanner results as candidates requiring triage. The original `source-map.json` and retained Apache-2.0 notice remain included for upstream workflows identified by the prior package.
