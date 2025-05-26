from factory import Application, MacOSFactory, WindowsFactory


def demonstrate_abstract_factory() -> None:
    """
    Demonstrate the Abstract Factory pattern by creating applications with different styles.
    """
    print("=== Abstract Factory Pattern Demonstration ===\n")

    try:
        # Create Windows-style application
        print("Creating Windows-style application...")
        windows_app = Application(WindowsFactory())
        windows_app.create_ui()
        windows_app.render_ui()
        windows_app.simulate_user_interaction()

        # Create MacOS-style application
        print("\nCreating MacOS-style application...")
        macos_app = Application(MacOSFactory())
        macos_app.create_ui()
        macos_app.render_ui()
        macos_app.simulate_user_interaction()

    except Exception as e:
        print(f"Application error: {str(e)}")


if __name__ == "__main__":
    demonstrate_abstract_factory()
