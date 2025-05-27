import time
from abc import abstractmethod
from typing import Protocol, runtime_checkable


@runtime_checkable
class VideoFile(Protocol):
    """Interface for video file objects."""

    @property
    @abstractmethod
    def filename(self) -> str:
        """Get the video filename."""
        ...

    @abstractmethod
    def load(self) -> None:
        """Load the video file into memory."""
        ...

    @abstractmethod
    def unload(self) -> None:
        """Unload the video file from memory."""
        ...


class MP4File:
    """Concrete implementation for MP4 video files."""

    def __init__(self, filename: str):
        """
        Initialize MP4 file handler.

        Args:
            filename: Path to the MP4 file

        Raises:
            ValueError: If filename is empty
        """
        if not filename.strip():
            raise ValueError("Filename cannot be empty")
        self._filename = filename
        self._loaded = False

    @property
    def filename(self) -> str:
        return self._filename

    def load(self) -> None:
        """Simulate loading an MP4 file."""
        print(f"Loading MP4 file: {self._filename}")
        time.sleep(1)  # Simulate loading time
        self._loaded = True

    def unload(self) -> None:
        """Simulate unloading an MP4 file."""
        if self._loaded:
            print(f"Unloading MP4 file: {self._filename}")
            self._loaded = False


class AVIFile:
    """Concrete implementation for AVI video files."""

    def __init__(self, filename: str):
        """
        Initialize AVI file handler.

        Args:
            filename: Path to the AVI file

        Raises:
            ValueError: If filename is empty
        """
        if not filename.strip():
            raise ValueError("Filename cannot be empty")
        self._filename = filename
        self._loaded = False

    @property
    def filename(self) -> str:
        return self._filename

    def load(self) -> None:
        """Simulate loading an AVI file."""
        print(f"Loading AVI file: {self._filename}")
        time.sleep(2)  # AVI files take longer to load
        self._loaded = True

    def unload(self) -> None:
        """Simulate unloading an AVI file."""
        if self._loaded:
            print(f"Unloading AVI file: {self._filename}")
            self._loaded = False
