from components import PlainText, TextComponent
from decorators import (
    BoldDecorator,
    ColorDecorator,
    FontSizeDecorator,
    ItalicDecorator,
    UnderlineDecorator,
)


class TextEditor:
    """
    Client class that uses the decorators to format text.
    Provides a simple interface for applying multiple formats.
    """

    def __init__(self):
        self._text: TextComponent = PlainText("")

    def set_text(self, content: str) -> None:
        """
        Set the base text content.

        Args:
            content: The plain text content

        Raises:
            ValueError: If content is not a string
        """
        self._text = PlainText(content)

    def apply_format(self, format_type: str, *args) -> None:
        """
        Apply a formatting decorator to the text.

        Args:
            format_type: The format to apply (bold, italic, etc.)
            *args: Additional arguments needed by the decorator

        Raises:
            ValueError: For unknown format types or invalid arguments
        """
        try:
            if format_type == "bold":
                self._text = BoldDecorator(self._text)
            elif format_type == "italic":
                self._text = ItalicDecorator(self._text)
            elif format_type == "underline":
                self._text = UnderlineDecorator(self._text)
            elif format_type == "color":
                if not args:
                    raise ValueError("Color value required")
                self._text = ColorDecorator(self._text, args[0])
            elif format_type == "size":
                if not args:
                    raise ValueError("Size value required")
                self._text = FontSizeDecorator(self._text, args[0])
            else:
                raise ValueError(f"Unknown format type: {format_type}")
        except Exception as e:
            print(f"Error applying format: {e}")

    def get_formatted_text(self) -> str:
        """Get the text with all applied formatting."""
        return self._text.render()

    def get_plain_text(self) -> str:
        """Get the raw text without formatting."""
        return self._text.get_content()

    def clear_formats(self) -> None:
        """Remove all formatting, keeping only the plain text."""
        content = self.get_plain_text()
        self._text = PlainText(content)
