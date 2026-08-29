"""
StrumSense - General Utilities & Helpers

Provides shared helper routines for timestamp handling, metrics calculations,
and chord visualization mappings.
"""

from typing import Dict, Any


def format_duration(seconds: float) -> str:
    """Format duration in seconds into a human-readable mm:ss string.

    Args:
        seconds: Elapsed time in seconds.

    Returns:
        Formatted string (e.g. '02:45').
    """
    # TODO: Implement duration string formatting
    pass


def get_chord_color(chord: str) -> str:
    """Return hex color code associated with each standard chord for UI overlays.

    Args:
        chord: Chord name.

    Returns:
        Hex color string.
    """
    # TODO: Map chord names to distinct color palette
    pass
