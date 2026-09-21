"""
Meeting data model.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Meeting:
    title: str
    venue: str
    date: str
    time: str
    president: str
    secretary: str