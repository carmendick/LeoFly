"""
Core FlyerEngine.
"""

from flyer_engine.utils.json_loader import load_meeting


class FlyerEngine:

    def start(self):

        meeting = load_meeting("examples/json/meeting.json")

        print("=" * 50)
        print("🦁 LeoFly")
        print("=" * 50)

        print(f"Title      : {meeting.title}")
        print(f"Venue      : {meeting.venue}")
        print(f"Date       : {meeting.date}")
        print(f"Time       : {meeting.time}")
        print(f"President  : {meeting.president}")
        print(f"Secretary  : {meeting.secretary}")

        print("=" * 50)