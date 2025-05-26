from notification import Notification


class PushNotification(Notification):
    """Concrete implementation of Notification for push notifications."""

    def __init__(self, device_id: str) -> None:
        """
        Initialize the push notification with device ID.

        Args:
            device_id: Unique identifier of the recipient's device.
        """
        self.device_id = device_id

    def send(self, message: str) -> bool:
        """
        Send a push notification.

        Args:
            message: The push notification content.

        Returns:
            bool: True if push notification was "sent" successfully.
        """
        print(
            f"Sending push notification to device {self.device_id} with message: {message}"
        )
        return True
