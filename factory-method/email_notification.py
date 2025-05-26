from notification import Notification


class EmailNotification(Notification):
    """
    Concrete implementation of Notification for email messages.
    """

    def __init__(self, recipient: str) -> None:
        """
        Initialize the email notification with recipient address.

        Args:
            recipient: Email address of the recipient.
        """
        self.recipient = recipient

    def send(self, message: str) -> bool:
        """
        Send an email notification.

        Args:
            message: The email body content.

        Returns:
            bool: True if email was "sent" successfully
        """
        print(f"Sending email to {self.recipient} with message: {message}")
        return True
