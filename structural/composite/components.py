from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional


class FileSystemComponent(ABC):
    """
    Abstract base class representing a component in the file system.
    This is the common interface for both individual files and directories.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Get the name of the component."""
        pass

    @abstractmethod
    def size(self) -> int:
        """Calculate the total size of the component in bytes."""
        pass

    @abstractmethod
    def display(self, indent: int = 0) -> None:
        """
        Display the component structure with proper indentation.

        Args:
            indent: Number of spaces to indent (for hierarchical display)
        """
        pass

    def add(self, component: "FileSystemComponent") -> None:
        """
        Add a child component (only applicable to directories).

        Args:
            component: The component to add

        Raises:
            NotImplementedError: If called on a leaf component (file)
        """
        raise NotImplementedError("Cannot add to a leaf component")

    def remove(self, component: "FileSystemComponent") -> None:
        """
        Remove a child component (only applicable to directories).

        Args:
            component: The component to remove

        Raises:
            NotImplementedError: If called on a leaf component (file)
        """
        raise NotImplementedError("Cannot remove from a leaf component")

    def get_child(self, name: str) -> Optional["FileSystemComponent"]:
        """
        Get a child component by name (only applicable to directories).

        Args:
            name: Name of the child component to find

        Returns:
            The child component if found, None otherwise

        Raises:
            NotImplementedError: If called on a leaf component (file)
        """
        raise NotImplementedError("Leaf components have no children")


@dataclass
class File(FileSystemComponent):
    """
    Leaf component representing a file in the file system.
    """

    _name: str
    _size: int

    @property
    def name(self) -> str:
        return self._name

    def size(self) -> int:
        return self._size

    def display(self, indent: int = 0) -> None:
        print(" " * indent + f"📄 {self._name} ({self._size} bytes)")


class Directory(FileSystemComponent):
    """
    Composite component representing a directory in the file system.
    Can contain other directories or files.
    """

    def __init__(self, name: str):
        self._name = name
        self._children: List[FileSystemComponent] = []

    @property
    def name(self) -> str:
        return self._name

    def size(self) -> int:
        """Calculate total size by summing all children's sizes."""
        return sum(child.size() for child in self._children)

    def display(self, indent: int = 0) -> None:
        """Display directory and all its contents recursively."""
        print(" " * indent + f"📁 {self._name}/ (total: {self.size()} bytes)")
        for child in self._children:
            child.display(indent + 4)

    def add(self, component: FileSystemComponent) -> None:
        """
        Add a child component to this directory.

        Args:
            component: The component to add (file or directory)

        Raises:
            ValueError: If a component with the same name already exists
        """
        if any(child.name == component.name for child in self._children):
            raise ValueError(f"A component named '{component.name}' already exists")
        self._children.append(component)

    def remove(self, component: FileSystemComponent) -> None:
        """
        Remove a child component from this directory.

        Args:
            component: The component to remove

        Raises:
            ValueError: If the component is not found
        """
        try:
            self._children.remove(component)
        except ValueError:
            raise ValueError(
                f"Component '{component.name}' not found in directory '{self._name}'"
            )

    def get_child(self, name: str) -> Optional[FileSystemComponent]:
        """
        Find a child component by name.

        Args:
            name: Name of the child to find

        Returns:
            The child component if found, None otherwise
        """
        return next((child for child in self._children if child.name == name), None)
