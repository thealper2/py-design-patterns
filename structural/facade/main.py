from display_controller import VideoPlayerFacade


def demonstrate_facade():
    """Demonstrate the Facade pattern with video playback."""
    try:
        player = VideoPlayerFacade()

        print("=== Playing MP4 File ===")
        player.play("sample_video.mp4")
        player.stop()

        print("\n=== Playing AVI File ===")
        player.play("another_video.avi")
        player.stop()

        print("\n=== Testing Error Cases ===")
        try:
            player.play("unsupported_format.mkv")  # Unsupported format
        except ValueError as e:
            print(f"Expected error: {e}")

        try:
            # This would fail in the subsystems if we didn't have proper error handling
            player.play("corrupted_file.avi")
            player.stop()
        except RuntimeError as e:
            print(f"Expected error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    demonstrate_facade()
