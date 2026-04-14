#!/usr/bin/env python3
"""
list_eu_models.py

Prints all OpenRouter models that satisfy EU in-region routing.

The EU filter is triggered by the combination of:
  - the eu.openrouter.ai subdomain, AND
  - the /models/user path

Usage:
  export OPENROUTER_API_KEY=sk-or-v1-...
  python list_eu_models.py
"""

import os
import sys
import requests
from dotenv import load_dotenv

# Loads OPENROUTER_API_KEY from a .env file sitting next to this script.
load_dotenv()


def main():
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("ERROR: set OPENROUTER_API_KEY environment variable first.")
        sys.exit(1)

    headers = {"Authorization": f"Bearer {api_key}"}

    r = requests.get(
        "https://eu.openrouter.ai/api/v1/models/user", headers=headers
    )
    r.raise_for_status()
    eu_models = r.json()["data"]

    print(f"{len(eu_models)} models available via EU in-region routing:\n")
    for m in sorted(eu_models, key=lambda x: x["id"]):
        print(f"  {m['id']}")


if __name__ == "__main__":
    main()
