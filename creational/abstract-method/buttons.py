from abc import ABC, abstractmethod


class Button(ABC):
    """Abstract base class for button UI elements."""

    @abstractmethod
    def render(self) -> None:
        """Render the button on screen."""
        pass

    @abstractmethod
    def on_click(self, callback: callable) -> None:
        """
        Set the click event handler.

        Args:
            callback: Function to be called when button is clicked.
        """
        pass


class TextField(ABC):
    """Abstract base class for text input UI elements."""

    @abstractmethod
    def render(self) -> None:
        """Render the text field on screen."""
        pass

    @abstractmethod
    def get_text(self) -> str:
        """Get the current text content."""
        pass

    @abstractmethod
    def set_text(self, text: str) -> None:
        """
        Set the text content.

        Args:
            text: The text to display in the field.
        """
        pass


class Checkbox(ABC):
    """Abstract base class for checkbox UI elements."""

    @abstractmethod
    def render(self) -> None:
        """Render the checkbox on screen."""
        pass

    @abstractmethod
    def toggle(self) -> None:
        """Toggle the checkbox state."""
        pass

    @abstractmethod
    def is_checked(self) -> bool:
        """Get the current checked state."""
        pass


# --- Concrete Products: Windows Style ---
class WindowsButton(Button):
    """Concrete Windows-style button implementation."""

    def __init__(self) -> None:
        self._callback = None

    def render(self) -> None:
        print("Rendering a Windows-style button")

    def on_click(self, callback: callable) -> None:
        print("Setting Windows button click handler")
        self._callback = callback


class WindowsTextField(TextField):
    """Concrete Windows-style text field implementation."""

    def __init__(self) -> None:
        self._text = ""

    def render(self) -> None:
        print(f"Rendering Windows text field with content: '{self._text}'")

    def get_text(self) -> str:
        return self._text

    def set_text(self, text: str) -> None:
        self._text = text
        print(f"Windows text field content updated to: '{text}'")


class WindowsCheckbox(Checkbox):
    """Concrete Windows-style checkbox implementation."""

    def __init__(self) -> None:
        self._checked = False

    def render(self) -> None:
        state = "checked" if self._checked else "unchecked"
        print(f"Rendering Windows checkbox ({state})")

    def toggle(self) -> None:
        self._checked = not self._checked
        print(
            f"Windows checkbox toggled to {'checked' if self._checked else 'unchecked'}"
        )

    def is_checked(self) -> bool:
        return self._checked


# --- Concrete Products: MacOS Style ---
class MacOSButton(Button):
    """Concrete MacOS-style button implementation."""

    def __init__(self) -> None:
        self._callback = None

    def render(self) -> None:
        print("Rendering a MacOS-style button")

    def on_click(self, callback: callable) -> None:
        print("Setting MacOS button click handler")
        self._callback = callback


class MacOSTextField(TextField):
    """Concrete MacOS-style text field implementation."""

    def __init__(self) -> None:
        self._text = ""

    def render(self) -> None:
        print(f"Rendering MacOS text field with content: '{self._text}'")

    def get_text(self) -> str:
        return self._text

    def set_text(self, text: str) -> None:
        self._text = text
        print(f"MacOS text field content updated to: '{text}'")


class MacOSCheckbox(Checkbox):
    """Concrete MacOS-style checkbox implementation."""

    def __init__(self) -> None:
        self._checked = False

    def render(self) -> None:
        state = "checked" if self._checked else "unchecked"
        print(f"Rendering MacOS checkbox ({state})")

    def toggle(self) -> None:
        self._checked = not self._checked
        print(
            f"MacOS checkbox toggled to {'checked' if self._checked else 'unchecked'}"
        )

    def is_checked(self) -> bool:
        return self._checked
