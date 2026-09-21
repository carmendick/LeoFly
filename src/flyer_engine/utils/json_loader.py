"""
JSON loader utilities.
"""

import json
from pathlib import Path

from flyer_engine.models.meeting import Meeting


def load_meeting(path: str) -> Meeting:
    """Load meeting data from a JSON file."""
    with open(Path(path), "r", encoding="utf-8") as file:
        data = json.load(file)

    return Meeting(**data)