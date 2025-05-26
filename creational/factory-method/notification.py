from abc import ABC, abstractmethod


class Notification(ABC):
    """
    Abstract base class representing a notification.
    All concrete notification types must implement the send method.
    """

    @abstractmethod
    def send(self, message: str) -> bool:
        """
        Send the notification with the given message.

        Args:
            message: The content to be sent in the notification.

        Returns:
            bool: True if the notification was sent successfully, False otherwise.
        """
        pass
