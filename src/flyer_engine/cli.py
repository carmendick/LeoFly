"""
Command Line Interface for LeoFly.
"""

from flyer_engine.core.engine import FlyerEngine


def main() -> None:
    """Launch LeoFly."""
    engine = FlyerEngine()
    engine.start()


if __name__ == "__main__":
    main()