from components import TextComponent


class TextDecorator(TextComponent):
    """
    Base decorator class that follows the TextComponent interface.
    All concrete decorators will inherit from this class.
    """

    def __init__(self, component: TextComponent):
        """
        Initialize with a TextComponent to decorate.

        Args:
            component: The text component to wrap

        Raises:
            TypeError: If component doesn't implement TextComponent
        """
        if not isinstance(component, TextComponent):
            raise TypeError("Component must implement TextComponent")
        self._component = component

    def render(self) -> str:
        """Delegate rendering to the wrapped component."""
        return self._component.render()

    def get_content(self) -> str:
        """Delegate content retrieval to the wrapped component."""
        return self._component.get_content()


class BoldDecorator(TextDecorator):
    """Decorator that adds bold formatting to text."""

    def render(self) -> str:
        """Render text wrapped in bold tags."""
        return f"<b>{self._component.render()}</b>"


class ItalicDecorator(TextDecorator):
    """Decorator that adds italic formatting to text."""

    def render(self) -> str:
        """Render text wrapped in italic tags."""
        return f"<i>{self._component.render()}</i>"


class UnderlineDecorator(TextDecorator):
    """Decorator that adds underline formatting to text."""

    def render(self) -> str:
        """Render text wrapped in underline tags."""
        return f"<u>{self._component.render()}</u>"


class ColorDecorator(TextDecorator):
    """Decorator that adds color formatting to text."""

    def __init__(self, component: TextComponent, color: str):
        """
        Initialize with text component and color.

        Args:
            component: The text component to decorate
            color: The color to apply (hex or name)

        Raises:
            ValueError: If color is empty
        """
        super().__init__(component)
        if not color.strip():
            raise ValueError("Color cannot be empty")
        self._color = color

    def render(self) -> str:
        """Render text wrapped in color span."""
        return f'<span style="color:{self._color}">{self._component.render()}</span>'


class FontSizeDecorator(TextDecorator):
    """Decorator that changes font size."""

    def __init__(self, component: TextComponent, size: int):
        """
        Initialize with text component and font size.

        Args:
            component: The text component to decorate
            size: The font size in pixels

        Raises:
            ValueError: If size is not positive
        """
        super().__init__(component)
        if size <= 0:
            raise ValueError("Font size must be positive")
        self._size = size

    def render(self) -> str:
        """Render text with font size style."""
        return (
            f'<span style="font-size:{self._size}px">{self._component.render()}</span>'
        )
