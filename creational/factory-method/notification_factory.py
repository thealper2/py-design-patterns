from typing import Any, Dict

from email_notification import EmailNotification
from notification import Notification
from push_notification import PushNotification
from sms_notification import SMSNotification


class NotificationFactory:
    """
    Factory class for creating different types of notifications.
    """

    @staticmethod
    def create_notification(
        notification_type: str, recipient_info: Dict[str, Any]
    ) -> Notification:
        """
        Createa a notification instance based on the specified type.

        Args:
            notification_type: Type of notication to create ('email', 'sms' or 'push').
            recipient_info: Dictionary containing recipient information needed for the notification.

        Returns:
            An instance of the appropriate Notification subclass.

        Raises:
            ValueError: If an invalid notification type is provided.
            KeyError: If required recipient information is missing.
        """
        try:
            if notification_type == "email":
                if "email_address" not in recipient_info:
                    raise KeyError("email_address is required for email notifications")
                return EmailNotification(recipient_info["email_address"])

            elif notification_type == "sms":
                if "phone_number" not in recipient_info:
                    raise KeyError("phone_number is required for SMS notifications")
                return SMSNotification(recipient_info["phone_number"])

            elif notification_type == "push":
                if "device_id" not in recipient_info:
                    raise KeyError("device_id is required for push notifications")
                return PushNotification(recipient_info["device_id"])

            else:
                raise ValueError(f"Invalid notification type: {notification_type}")

        except Exception as e:
            print(f"Error creating notification: {str(e)}")
            raise
