from abc import ABC, abstractmethod

from buttons import (
    Button,
    Checkbox,
    MacOSButton,
    MacOSCheckbox,
    MacOSTextField,
    TextField,
    WindowsButton,
    WindowsCheckbox,
    WindowsTextField,
)


class GUIFactory(ABC):
    """Abstract factory interface for creating UI components."""

    @abstractmethod
    def create_button(self) -> Button:
        """Create a button UI component."""
        pass

    @abstractmethod
    def create_text_field(self) -> TextField:
        """Create a text input UI component."""
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        """Create a checkbox UI component."""
        pass


# --- Concrete Factories ---
class WindowsFactory(GUIFactory):
    """Concrete factory for Windows-style UI components."""

    def create_button(self) -> Button:
        return WindowsButton()

    def create_text_field(self) -> TextField:
        return WindowsTextField()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacOSFactory(GUIFactory):
    """Concrete factory for MacOS-style UI components."""

    def create_button(self) -> Button:
        return MacOSButton()

    def create_text_field(self) -> TextField:
        return MacOSTextField()

    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()


class Application:
    """
    Client class that uses the abstract factory to create UI components.

    The client code works with factories and products through abstract interfaces.
    This allows you to pass any factory subclass to create different UI styles.
    """

    def __init__(self, factory: GUIFactory) -> None:
        """
        Initialize the application with a concrete factory.

        Args:
            factory: The factory implementation to use for creating UI components.
        """
        self._factory = factory
        self._button = None
        self._text_field = None
        self._checkbox = None

    def create_ui(self) -> None:
        """Create the UI components using the factory."""
        try:
            self._button = self._factory.create_button()
            self._text_field = self._factory.create_text_field()
            self._checkbox = self._factory.create_checkbox()
        except Exception as e:
            print(f"Error creating UI components: {str(e)}")
            raise

    def render_ui(self) -> None:
        """Render all UI components."""
        if not all([self._button, self._text_field, self._checkbox]):
            raise RuntimeError("UI components not created. Call create_ui() first.")

        print("\n--- Rendering UI ---")
        self._button.render()
        self._text_field.render()
        self._checkbox.render()

    def simulate_user_interaction(self) -> None:
        """Simulate user interaction with the UI components."""
        if not all([self._button, self._text_field, self._checkbox]):
            raise RuntimeError("UI components not created. Call create_ui() first.")

        print("\n--- Simulating User Interaction ---")
        self._text_field.set_text("Hello, Abstract Factory!")
        self._checkbox.toggle()
        self._button.on_click(lambda: print("Button clicked!"))
