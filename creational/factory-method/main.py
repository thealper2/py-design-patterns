from notification_factory import NotificationFactory


def demonstrate_factory_method() -> None:
    """
    Demonstrate the Factory Method pattern with the NotificationFactory.
    """
    print("=== Factory Method Pattern Demonstration ===")

    # Example recipient information for different notification types
    recipients = [
        {"type": "email", "info": {"email_address": "user@example.com"}},
        {"type": "sms", "info": {"phone_number": "+1234567890"}},
        {"type": "push", "info": {"device_id": "device-12345"}},
    ]

    # Create and send notifications using the factory
    for recipient in recipients:
        try:
            notification = NotificationFactory.create_notification(
                recipient["type"], recipient["info"]
            )

            result = notification.send("Hello! This is a test notification.")
            print(f"Notification sent successfully: {result}")

        except (ValueError, KeyError) as e:
            print(f"Failed to send notification: {str(e)}")


if __name__ == "__main__":
    demonstrate_factory_method()
