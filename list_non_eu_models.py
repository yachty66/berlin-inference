#!/usr/bin/env python3
"""
list_non_eu_models.py

Prints all OpenRouter models that are NOT available via EU in-region routing.

Method:
  - Fetch the full global catalog from openrouter.ai/api/v1/models
  - Fetch the EU-filtered catalog from eu.openrouter.ai/api/v1/models/user
  - Print the set difference (everything in global but not in EU)

Note: "not in EU" here means "no provider serving this model has enrolled in
OpenRouter's EU in-region routing program." A provider could still physically
serve from EU hardware — they just haven't formally opted in.

Usage:
  export OPENROUTER_API_KEY=sk-or-v1-...   (or put it in .env)
  python list_non_eu_models.py
"""

import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv()


def main():
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("ERROR: set OPENROUTER_API_KEY environment variable first.")
        sys.exit(1)

    headers = {"Authorization": f"Bearer {api_key}"}

    # Global catalog — every model on OpenRouter
    r_all = requests.get(
        "https://openrouter.ai/api/v1/models", headers=headers
    )
    r_all.raise_for_status()
    all_ids = {m["id"] for m in r_all.json()["data"]}

    # EU in-region catalog — only models where ≥1 provider is enrolled
    # in OpenRouter's enterprise EU routing program.
    r_eu = requests.get(
        "https://eu.openrouter.ai/api/v1/models/user", headers=headers
    )
    r_eu.raise_for_status()
    eu_ids = {m["id"] for m in r_eu.json()["data"]}

    # Diff: models in the global catalog but not in the EU-filtered one.
    non_eu_ids = sorted(all_ids - eu_ids)

    # Write the list to a file next to this script, one model ID per line.
    out_path = os.path.join(os.path.dirname(__file__), "non-eu-models.txt")
    with open(out_path, "w") as f:
        for mid in non_eu_ids:
            f.write(f"{mid}\n")

    print(
        f"Wrote {len(non_eu_ids)} models NOT available via EU in-region "
        f"routing to {out_path}"
    )


if __name__ == "__main__":
    main()
