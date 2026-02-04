# diagnoVet-Assessment
## Google Cloud Integration

The project uses a pluggable storage interface.
In production, the `GCSStorage` adapter uploads assets to Google Cloud Storage
using workload identity or service account impersonation.

Local development uses `LocalStorage` to avoid IAM and OAuth constraints.
