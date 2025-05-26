from notification import Notification


class SMSNotification(Notification):
    """Concrete implementation of Notification for SMS messages."""

    def __init__(self, phone_number: str) -> None:
        """
        Initialize the SMS notification with phone number.

        Args:
            phone_number: Phone number of the recipient.
        """
        self.phone_number = phone_number

    def send(self, message: str) -> bool:
        """
        Send an SMS notification.

        Args:
            message: The SMS text content.

        Returns:
            bool: True if SMS was "sent" successfully.
        """
        print(f"Sending SMS to {self.phone_number} with message: {message}")
        return True
