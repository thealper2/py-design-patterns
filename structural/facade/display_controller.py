import time
from typing import Optional

from decoders import AudioDecoder, VideoDecoder
from files import AVIFile, MP4File, VideoFile


class DisplayController:
    """Subsystem class for display operations."""

    def __init__(self):
        self._active = False

    def activate_display(self) -> None:
        """Activate the video display."""
        print("Activating display...")
        time.sleep(0.3)
        self._active = True

    def deactivate_display(self) -> None:
        """Deactivate the video display."""
        if self._active:
            print("Deactivating display...")
            self._active = False

    def render_frame(self, frame_data: str) -> None:
        """
        Render a video frame.

        Args:
            frame_data: The frame data to render

        Raises:
            RuntimeError: If display not active
        """
        if not self._active:
            raise RuntimeError("Display not active")
        print(f"Rendering frame: {frame_data}")


class VideoPlayerFacade:
    """
    Facade class that provides a simple interface to the complex video playback system.
    """

    def __init__(self):
        self._audio_decoder = AudioDecoder()
        self._video_decoder = VideoDecoder()
        self._display = DisplayController()
        self._current_file: Optional[VideoFile] = None

    def play(self, filename: str) -> None:
        """
        Play a video file.

        Args:
            filename: Path to the video file to play

        Raises:
            ValueError: For unsupported file formats
            RuntimeError: For playback errors
        """
        try:
            # Determine file type and load appropriate handler
            if filename.lower().endswith(".mp4"):
                self._current_file = MP4File(filename)
            elif filename.lower().endswith(".avi"):
                self._current_file = AVIFile(filename)
            else:
                raise ValueError(f"Unsupported file format: {filename}")

            # Initialize subsystems
            self._audio_decoder.initialize()
            self._video_decoder.initialize()
            self._display.activate_display()

            # Load and play the file
            self._current_file.load()

            print(f"\nPlaying {filename}...")
            self._video_decoder.decode_video("main_video_stream")
            self._audio_decoder.decode_audio("main_audio_stream")

            # Simulate frame rendering
            for i in range(1, 4):
                self._display.render_frame(f"frame_{i}")
                time.sleep(0.7)

            print("\nPlayback completed successfully!")

        except Exception as e:
            print(f"\nPlayback failed: {e}")
            self.stop()
            raise RuntimeError("Playback aborted due to errors") from e

    def stop(self) -> None:
        """Stop playback and clean up resources."""
        print("\nStopping playback...")
        if self._current_file:
            self._current_file.unload()
        self._display.deactivate_display()
        print("All resources released")
