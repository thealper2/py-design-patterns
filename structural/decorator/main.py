from text_editor import TextEditor


def demonstrate_decorator():
    """Demonstrate the Decorator pattern with text formatting."""
    try:
        editor = TextEditor()

        print("=== Basic Text ===")
        editor.set_text("Hello, Design Patterns!")
        print(editor.get_formatted_text())

        print("\n=== Adding Bold ===")
        editor.apply_format("bold")
        print(editor.get_formatted_text())

        print("\n=== Adding Italic ===")
        editor.apply_format("italic")
        print(editor.get_formatted_text())

        print("\n=== Adding Color ===")
        editor.apply_format("color", "blue")
        print(editor.get_formatted_text())

        print("\n=== Adding Underline ===")
        editor.apply_format("underline")
        print(editor.get_formatted_text())

        print("\n=== Adding Font Size ===")
        editor.apply_format("size", 24)
        print(editor.get_formatted_text())

        print("\n=== Plain Text ===")
        print(editor.get_plain_text())

        print("\n=== Clearing Formats ===")
        editor.clear_formats()
        print(editor.get_formatted_text())

        print("\n=== Testing Error Cases ===")
        try:
            editor.apply_format("shadow")  # Unknown format
        except ValueError as e:
            print(f"Expected error: {e}")

        try:
            editor.apply_format("color")  # Missing color value
        except ValueError as e:
            print(f"Expected error: {e}")

        try:
            editor.apply_format("size", -12)  # Invalid size
        except ValueError as e:
            print(f"Expected error: {e}")

        try:
            editor.set_text(123)  # type: ignore # Invalid content type
        except ValueError as e:
            print(f"Expected error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    demonstrate_decorator()
