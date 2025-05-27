from devices import TV, Radio
from remote_control import AdvancedRemoteControl, RemoteControl


def demonstrate_bridge():
    """Demonstrate the Bridge pattern with TV and Radio devices."""
    try:
        print("=== Testing TV with Basic Remote ===")
        tv = TV()
        remote = RemoteControl(tv)

        remote.toggle_power()
        remote.volume_up()
        remote.channel_up()
        remote.channel_down()
        remote.volume_down()
        remote.toggle_power()

        print("\n=== Testing Radio with Advanced Remote ===")
        radio = Radio()
        advanced_remote = AdvancedRemoteControl(radio)

        advanced_remote.toggle_power()
        advanced_remote.volume_up()
        advanced_remote.go_to_channel(95)
        advanced_remote.mute()
        advanced_remote.toggle_power()

        print("\n=== Testing Error Cases ===")
        try:
            bad_remote = RemoteControl("not a device")  # type: ignore
        except TypeError as e:
            print(f"Expected type error: {e}")

        try:
            advanced_remote.go_to_channel(50)  # Radio doesn't support this channel
        except ValueError as e:
            print(f"Expected value error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    demonstrate_bridge()
