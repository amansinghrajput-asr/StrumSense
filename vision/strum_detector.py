"""
StrumSense - Vision Engine: Strum Detector

Computes frame-to-frame wrist velocity along the Y-axis to classify
strumming motions into UP, DOWN, or IDLE states with zero-crossing debounce.
"""

from typing import Optional, Tuple


class StrumDetector:
    """Classifies strumming direction based on vertical velocity of the wrist."""

    def __init__(self, velocity_threshold: float = 0.02, debounce_frames: int = 3) -> None:
        """Initialize the strum direction detector.

        Args:
            velocity_threshold: Minimum vertical displacement delta to trigger a stroke.
            debounce_frames: Number of stable frames required to register a direction change.
        """
        # TODO: Initialize previous Y-coordinate buffer and debounce counter
        self.velocity_threshold = velocity_threshold
        self.debounce_frames = debounce_frames
        self._prev_y: Optional[float] = None

    def update(self, wrist_coord: Optional[Tuple[float, float]]) -> Optional[str]:
        """Compute vertical velocity and classify strum direction.

        Args:
            wrist_coord: (x, y) normalized coordinate of the wrist in the current frame.

        Returns:
            'DOWN', 'UP', or None if stationary / idle.
        """
        # TODO: Compute dy = current_y - prev_y
        # TODO: Positive dy corresponds to downward movement (image Y increases downwards) -> 'DOWN'
        # TODO: Negative dy corresponds to upward movement -> 'UP'
        # TODO: Apply debounce logic to avoid duplicate triggers for a single stroke
        pass
