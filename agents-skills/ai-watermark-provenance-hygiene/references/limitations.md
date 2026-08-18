# Limitations

- Metadata cleanup does not prove that a file was never AI-generated.
- Detector outcomes are not guarantees of authorship or provenance.
- JPEG APP markers are vendor-extensible; the cleaner removes only the selected classes.
- Removing metadata can invalidate provenance signatures by design.
- The default mode prioritizes fidelity over maximum metadata destruction.
- Always keep an original copy before destructive cleanup.
