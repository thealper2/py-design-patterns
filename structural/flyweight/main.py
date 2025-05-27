import random
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Tuple


class CharacterProperties(ABC):
    """Flyweight interface that declares properties of characters."""

    @abstractmethod
    def render(self, position: Tuple[int, int]) -> str:
        """
        Render the character at a specific position.

        Args:
            position: (x, y) coordinates where to render

        Returns:
            String representation of the rendered character
        """
        pass


class ConcreteCharacter(CharacterProperties):
    """Concrete Flyweight that stores intrinsic state (shared properties)."""

    def __init__(self, char: str, font: str, size: int, color: str):
        """
        Initialize character properties.

        Args:
            char: The actual character (A-Z, a-z, 0-9, etc.)
            font: Font family name
            size: Font size in points
            color: Font color name or hex code

        Raises:
            ValueError: For invalid character or size
        """
        if len(char) != 1:
            raise ValueError("Character must be a single character")
        if size <= 0:
            raise ValueError("Font size must be positive")

        self._char = char
        self._font = font
        self._size = size
        self._color = color

    def render(self, position: Tuple[int, int]) -> str:
        """Render the character with its shared properties at given position."""
        x, y = position
        return (
            f"Character '{self._char}' rendered at ({x}, {y}) "
            f"with font '{self._font}', size {self._size}, color {self._color}"
        )


class CharacterFactory:
    """
    Flyweight factory that manages and reuses existing flyweights.
    Ensures that characters are shared properly.
    """

    _characters: Dict[str, CharacterProperties] = {}

    @classmethod
    def get_character(
        cls, char: str, font: str, size: int, color: str
    ) -> CharacterProperties:
        """
        Get or create a character flyweight.

        Args:
            char: The character to get/create
            font: Font family name
            size: Font size in points
            color: Font color name or hex code

        Returns:
            A character flyweight instance

        Raises:
            ValueError: For invalid character properties
        """
        key = f"{char}_{font}_{size}_{color}"

        if key not in cls._characters:
            cls._characters[key] = ConcreteCharacter(char, font, size, color)
            print(f"Created new character flyweight for '{key}'")
        else:
            print(f"Reusing existing character flyweight for '{key}'")

        return cls._characters[key]

    @classmethod
    def total_flyweights(cls) -> int:
        """Get the total number of flyweights created."""
        return len(cls._characters)


class Character:
    """
    Context class that contains extrinsic state (position) and reference to flyweight.
    Represents a character in the document with its position.
    """

    def __init__(
        self,
        char: str,
        position: Tuple[int, int],
        font: str = "Arial",
        size: int = 12,
        color: str = "black",
    ):
        """
        Initialize a character with its properties and position.

        Args:
            char: The character to render
            position: (x, y) coordinates where to render
            font: Font family name (default: Arial)
            size: Font size in points (default: 12)
            color: Font color (default: black)
        """
        self._position = position
        self._properties = CharacterFactory.get_character(char, font, size, color)

    def render(self) -> str:
        """Render the character by delegating to the flyweight."""
        return self._properties.render(self._position)


class Document:
    """
    Client class that uses flyweights through Character objects.
    Represents a document containing many characters.
    """

    def __init__(self):
        self._characters: List[Character] = []

    def add_character(
        self,
        char: str,
        position: Tuple[int, int],
        font: Optional[str] = None,
        size: Optional[int] = None,
        color: Optional[str] = None,
    ) -> None:
        """
        Add a character to the document with random properties if not specified.

        Args:
            char: The character to add
            position: (x, y) coordinates
            font: Optional font family (random if None)
            size: Optional font size (random if None)
            color: Optional color (random if None)

        Raises:
            ValueError: For invalid character
        """
        if len(char) != 1:
            raise ValueError("Can only add single characters")

        fonts = ["Arial", "Times New Roman", "Courier New", "Verdana"]
        colors = ["black", "red", "blue", "green", "purple"]

        font = font or random.choice(fonts)
        size = size or random.randint(10, 24)
        color = color or random.choice(colors)

        self._characters.append(Character(char, position, font, size, color))

    def render(self) -> None:
        """Render all characters in the document."""
        print("\n=== Document Rendering ===")
        for char in self._characters:
            print(char.render())

        print(f"\nTotal characters in document: {len(self._characters)}")
        print(f"Total flyweights created: {CharacterFactory.total_flyweights()}")
        print(
            f"Memory savings: {len(self._characters) - CharacterFactory.total_flyweights()} flyweights saved"
        )


def demonstrate_flyweight():
    """Demonstrate the Flyweight pattern with character rendering."""
    try:
        doc = Document()

        # Add some characters with random properties
        for i in range(100):
            char = random.choice(
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            )
            position = (random.randint(0, 100), (random.randint(0, 100)))
            doc.add_character(char, position)

        # Add some repeated characters (should reuse flyweights)
        for _ in range(10):
            doc.add_character("A", (0, 0), "Times New Roman", 12, "black")
            doc.add_character("B", (10, 10), "Arial", 14, "red")

        # Render the document
        doc.render()

        print("\n=== Testing Error Cases ===")
        try:
            doc.add_character("", (0, 0))  # Empty character
        except ValueError as e:
            print(f"Expected error: {e}")

        try:
            doc.add_character("AB", (0, 0))  # Multiple characters
        except ValueError as e:
            print(f"Expected error: {e}")

        try:
            CharacterFactory.get_character("A", "Invalid", -12, "black")  # Invalid size
        except ValueError as e:
            print(f"Expected error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    demonstrate_flyweight()
