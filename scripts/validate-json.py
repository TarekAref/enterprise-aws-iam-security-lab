#!/usr/bin/env python3
"""Validate that all JSON files in the repository are syntactically valid.

This checks JSON syntax only. It does not prove that an IAM policy is secure,
least privilege, or semantically valid for AWS. Use IAM Access Analyzer policy
validation for AWS-aware review.
"""

import json
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
json_files = sorted(root.rglob("*.json"))
failed = False

for path in json_files:
    try:
        with path.open("r", encoding="utf-8") as fh:
            json.load(fh)
        print(f"OK   {path.relative_to(root)}")
    except Exception as exc:
        failed = True
        print(f"FAIL {path.relative_to(root)}: {exc}")

if failed:
    sys.exit(1)

print(f"Validated {len(json_files)} JSON file(s).")
