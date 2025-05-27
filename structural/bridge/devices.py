from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable


@runtime_checkable
class DeviceImplementation(Protocol):
    """Interface for all device implementations in the Bridge pattern."""

    @abstractmethod
    def is_enabled(self) -> bool:
        """Check if the device is powered on."""
        pass

    @abstractmethod
    def enable(self) -> None:
        """Power on the device."""
        pass

    @abstractmethod
    def disable(self) -> None:
        """Power off the device."""
        pass

    @abstractmethod
    def get_volume(self) -> int:
        """Get current volume level."""
        pass

    @abstractmethod
    def set_volume(self, percent: int) -> None:
        """Set volume level (0-100)."""
        pass

    @abstractmethod
    def get_channel(self) -> int:
        """Get current channel number."""
        pass

    @abstractmethod
    def set_channel(self, channel: int) -> None:
        """Set channel number."""
        pass


class TV(DeviceImplementation):
    """Concrete implementation of a TV device."""

    def __init__(self) -> None:
        self._enabled = False
        self._volume = 30
        self._channel = 1
        self._max_channel = 100

    def is_enabled(self) -> bool:
        return self._enabled

    def enable(self) -> None:
        self._enabled = True

    def disable(self) -> None:
        self._enabled = False

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, percent: int) -> None:
        if not 0 <= percent <= 100:
            raise ValueError("Volume must be between 0 and 100")
        self._volume = percent

    def get_channel(self) -> int:
        return self._channel

    def set_channel(self, channel: int) -> None:
        if not 1 <= channel <= self._max_channel:
            raise ValueError(f"Channel must be between 1 and {self._max_channel}")
        self._channel = channel


class Radio(DeviceImplementation):
    """Concrete implementation of a radio device."""

    def __init__(self) -> None:
        self._on = False
        self._volume = 20
        self._channel = 88  # FM frequency

    def is_enabled(self) -> bool:
        return self._on

    def enable(self) -> None:
        self._on = True

    def disable(self) -> None:
        self._on = False

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, percent: int) -> None:
        if not 0 <= percent <= 100:
            raise ValueError("Volume must be between 0 and 100")
        self._volume = percent

    def get_channel(self) -> int:
        return self._channel

    def set_channel(self, channel: int) -> None:
        if not 88 <= channel <= 108:  # Typical FM range
            raise ValueError("FM frequency must be between 88 and 108 MHz")
        self._channel = channel
