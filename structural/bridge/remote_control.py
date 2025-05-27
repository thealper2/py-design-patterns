from devices import DeviceImplementation


class RemoteControl:
    """
    Abstraction in Bridge pattern.
    Defines the high-level interface that clients will use.
    """

    def __init__(self, device: DeviceImplementation) -> None:
        """
        Initialize remote control with a specific device implementation.

        Args:
            device: Concrete device implementation

        Raises:
            TypeError: If device doesn't implement DeviceImplementation protocol
        """
        if not isinstance(device, DeviceImplementation):
            raise TypeError("Device must implement DeviceImplementation protocol")
        self._device = device

    def toggle_power(self) -> None:
        """Toggle device power on/off."""
        if self._device.is_enabled():
            self._device.disable()
            print("Device turned off")
        else:
            self._device.enable()
            print("Device turned on")

    def volume_up(self) -> None:
        """Increase volume by 10%."""
        current = self._device.get_volume()
        try:
            self._device.set_volume(min(100, current + 10))
            print(f"Volume increased to {self._device.get_volume()}%")
        except Exception as e:
            print(f"Failed to increase volume: {e}")

    def volume_down(self) -> None:
        """Decrease volume by 10%."""
        current = self._device.get_volume()
        try:
            self._device.set_volume(max(0, current - 10))
            print(f"Volume decreased to {self._device.get_volume()}%")
        except Exception as e:
            print(f"Failed to decrease volume: {e}")

    def channel_up(self) -> None:
        """Go to next channel."""
        current = self._device.get_channel()
        try:
            self._device.set_channel(current + 1)
            print(f"Changed to channel {self._device.get_channel()}")
        except Exception as e:
            print(f"Failed to change channel: {e}")

    def channel_down(self) -> None:
        """Go to previous channel."""
        current = self._device.get_channel()
        try:
            self._device.set_channel(max(1, current - 1))
            print(f"Changed to channel {self._device.get_channel()}")
        except Exception as e:
            print(f"Failed to change channel: {e}")


class AdvancedRemoteControl(RemoteControl):
    """
    Extended abstraction with additional features.
    Demonstrates how the Bridge pattern allows extending the abstraction
    without changing the implementation hierarchy.
    """

    def mute(self) -> None:
        """Mute the device (set volume to 0)."""
        try:
            self._device.set_volume(0)
            print("Device muted")
        except Exception as e:
            print(f"Failed to mute device: {e}")

    def go_to_channel(self, channel: int) -> None:
        """Go directly to specific channel number."""
        if channel < 1:
            raise ValueError("Channel number must be positive")
        try:
            self._device.set_channel(channel)
            print(f"Jumped to channel {channel}")
        except Exception as e:
            print(f"Failed to change channel: {e}")
