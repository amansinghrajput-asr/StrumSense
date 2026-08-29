"""
StrumSense - Configuration Settings

Defines global parameters, audio sampling parameters, vision tracking thresholds,
and supported chord targets.
"""

from typing import Dict, List, Any

# TODO: Configure audio sampling rate and buffer duration
AUDIO_CONFIG: Dict[str, Any] = {
    "sample_rate": 22050,
    "buffer_duration_sec": 1.5,
    "hop_length": 512,
    "target_chords": ["C", "G", "D", "Em"],
    "similarity_threshold": 0.65,
}

# TODO: Configure vision tracking, camera index, and strum velocity thresholds
VISION_CONFIG: Dict[str, Any] = {
    "camera_index": 0,
    "min_detection_confidence": 0.5,
    "min_tracking_confidence": 0.5,
    "velocity_threshold": 0.02,
    "debounce_frames": 3,
}

# TODO: Configure stream fusion sync window
FUSION_CONFIG: Dict[str, Any] = {
    "sync_window_ms": 100,
    "stale_threshold_ms": 500,
}
