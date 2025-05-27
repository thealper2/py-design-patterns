from abc import abstractmethod
from typing import Protocol, runtime_checkable


@runtime_checkable
class TextComponent(Protocol):
    """
    Interface for text components in the editor.
    Both simple text and decorated text should implement this.
    """

    @abstractmethod
    def render(self) -> str:
        """Render the text with all applied formatting."""
        pass

    @abstractmethod
    def get_content(self) -> str:
        """Get the raw text content without formatting."""
        pass


class PlainText:
    """Concrete component representing plain unformatted text."""

    def __init__(self, content: str):
        """
        Initialize with text content.

        Args:
            content: The raw text content

        Raises:
            ValueError: If content is not a string
        """
        if not isinstance(content, str):
            raise ValueError("Content must be a string")
        self._content = content

    def render(self) -> str:
        """Return the plain text without formatting."""
        return self._content

    def get_content(self) -> str:
        """Get the raw text content."""
        return self._content
