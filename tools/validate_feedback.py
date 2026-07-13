#!/usr/bin/env python3
"""Validate a SIMS_FEEDBACK_V1 v1.1 JSON file."""
from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("jsonschema is required: pip install jsonschema", file=sys.stderr)
    raise SystemExit(2)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python tools/validate_feedback.py feedback.json", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parents[1]
    schema_path = root / "product" / "contracts" / "SIMS_FEEDBACK_V1_1.schema.json"
    data_path = Path(sys.argv[1])

    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        data = json.loads(data_path.read_text(encoding="utf-8"))
        jsonschema.validate(data, schema)
    except FileNotFoundError as exc:
        print(f"File not found: {exc.filename}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f"Invalid JSON: {exc}", file=sys.stderr)
        return 1
    except jsonschema.ValidationError as exc:
        print(f"Schema validation failed: {exc.message}", file=sys.stderr)
        return 1

    print("PASS: valid SIMS_FEEDBACK_V1 version 1.1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
