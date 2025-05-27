import time


class AudioDecoder:
    """Subsystem class for audio decoding operations."""

    def __init__(self):
        self._initialized = False

    def initialize(self) -> None:
        """Initialize the audio decoder."""
        print("Initializing audio decoder...")
        time.sleep(0.5)
        self._initialized = True

    def decode_audio(self, audio_stream: str) -> None:
        """
        Decode the audio stream.

        Args:
            audio_stream: The audio stream to decode

        Raises:
            RuntimeError: If decoder not initialized
        """
        if not self._initialized:
            raise RuntimeError("Audio decoder not initialized")
        print(f"Decoding audio stream: {audio_stream}")
        time.sleep(1)


class VideoDecoder:
    """Subsystem class for video decoding operations."""

    def __init__(self):
        self._initialized = False

    def initialize(self) -> None:
        """Initialize the video decoder."""
        print("Initializing video decoder...")
        time.sleep(0.5)
        self._initialized = True

    def decode_video(self, video_stream: str) -> None:
        """
        Decode the video stream.

        Args:
            video_stream: The video stream to decode

        Raises:
            RuntimeError: If decoder not initialized
        """
        if not self._initialized:
            raise RuntimeError("Video decoder not initialized")
        print(f"Decoding video stream: {video_stream}")
        time.sleep(1.5)
