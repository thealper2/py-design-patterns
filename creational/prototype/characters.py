import copy
import json
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class CharacterPrototype(ABC):
    """
    Abstract base class for character prototypes that defines the cloning interface.
    """

    @abstractmethod
    def clone(self) -> "CharacterPrototype":
        """Create a deep copy of the character instance."""
        pass

    @abstractmethod
    def customize(self, **kwargs: Any) -> None:
        """
        Customize the character's attributes.

        Args:
            **kwargs: Key-value pairs of attributes to modify.
        """
        pass

    @abstractmethod
    def display(self) -> None:
        """Display the character's attributes."""
        pass


class GameCharacter(CharacterPrototype):
    """
    Concrete implementation of a game character that supports cloning.
    """

    def __init__(
        self,
        character_type: str,
        health: int,
        mana: int,
        abilities: Dict[str, int],
        appearance: Dict[str, str],
        inventory: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a game character with basic attributes.

        Args:
            character_type: The class/type of the character (e.g., 'Warrior', 'Mage')
            health: Initial health points
            mana: Initial mana points
            abilities: Dictionary of abilities and their levels
            appearance: Dictionary describing visual attributes
            inventory: Optional list of starting items
        """
        self.character_type = character_type
        self.health = health
        self.mana = mana
        self.abilities = abilities.copy()
        self.appearance = appearance.copy()
        self.inventory = inventory.copy() if inventory else []

        # Internal state not meant to be cloned
        self._unique_id = id(self)

    def clone(self) -> "GameCharacter":
        """
        Create a deep copy of the character instance.

        Returns:
            A new GameCharacter instance with identical attributes.
        """
        try:
            new_character = copy.deepcopy(self)
            new_character._unique_id = id(new_character)  # Assign new unique ID
            return new_character
        except Exception as e:
            print(f"Error cloning character: {str(e)}")
            raise

    def customize(self, **kwargs: Any) -> None:
        """
        Modify the character's attributes.

        Args:
            **kwargs: Attributes to modify with their new values.

        Raises:
            ValueError: If trying to modify non-existent attributes.
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                if isinstance(getattr(self, key), dict):
                    # For dictionary attributes, update rather than replace
                    getattr(self, key).update(value)
                else:
                    setattr(self, key, value)
            else:
                raise ValueError(f"Invalid character attribute: {key}")

    def add_ability(self, name: str, level: int) -> None:
        """
        Add or update an ability.

        Args:
            name: Name of the ability
            level: Level of proficiency
        """
        self.abilities[name] = level

    def add_item(self, item: str) -> None:
        """Add an item to the character's inventory."""
        self.inventory.append(item)

    def display(self) -> None:
        """Display the character's full specification."""
        print("\nCharacter Details:")
        print(f"Type: {self.character_type}")
        print(f"Health: {self.health}")
        print(f"Mana: {self.mana}")
        print("Abilities:")
        for ability, level in self.abilities.items():
            print(f"  - {ability}: {level}")
        print("Appearance:")
        for attr, value in self.appearance.items():
            print(f"  - {attr}: {value}")
        print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")
        print(f"Unique ID: {self._unique_id}")
        print("-----------------------\n")

    def to_json(self) -> str:
        """Serialize the character to JSON (excluding the unique ID)."""
        data = {
            "character_type": self.character_type,
            "health": self.health,
            "mana": self.mana,
            "abilities": self.abilities,
            "appearance": self.appearance,
            "inventory": self.inventory,
        }
        return json.dumps(data)

    @classmethod
    def from_json(cls, json_str: str) -> "GameCharacter":
        """Create a character from JSON data."""
        data = json.loads(json_str)
        return cls(**data)


class CharacterRegistry:
    """
    Prototype manager that stores pre-defined character templates.
    """

    def __init__(self) -> None:
        self._prototypes: Dict[str, GameCharacter] = {}

    def register_prototype(self, name: str, prototype: GameCharacter) -> None:
        """
        Register a character prototype in the registry.

        Args:
            name: Key to identify the prototype
            prototype: Character instance to store as prototype

        Raises:
            ValueError: If prototype is not a GameCharacter instance
        """
        if not isinstance(prototype, GameCharacter):
            raise ValueError(
                "Only GameCharacter instances can be registered as prototypes"
            )
        self._prototypes[name] = prototype

    def unregister_prototype(self, name: str) -> None:
        """Remove a prototype from the registry."""
        self._prototypes.pop(name, None)

    def clone_prototype(self, name: str, **kwargs: Any) -> GameCharacter:
        """
        Clone a registered prototype and optionally customize it.

        Args:
            name: Key of the prototype to clone
            **kwargs: Attributes to customize in the cloned instance

        Returns:
            A new customized GameCharacter instance

        Raises:
            KeyError: If prototype name is not found
        """
        try:
            prototype = self._prototypes[name]
            clone = prototype.clone()
            if kwargs:
                clone.customize(**kwargs)
            return clone
        except KeyError:
            raise KeyError(f"No prototype registered with name: {name}")
