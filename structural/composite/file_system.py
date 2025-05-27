from components import Directory, File


class FileSystem:
    """
    High-level interface for the file system using the Composite pattern.
    """

    def __init__(self):
        self._root = Directory("root")
        self._current_directory = self._root

    def create_file(self, name: str, size: int) -> None:
        """
        Create a new file in the current directory.

        Args:
            name: Name of the new file
            size: Size of the file in bytes

        Raises:
            ValueError: If file name is invalid or size is negative
        """
        if not name or "/" in name:
            raise ValueError("Invalid file name")
        if size < 0:
            raise ValueError("File size cannot be negative")

        try:
            self._current_directory.add(File(name, size))
            print(f"Created file '{name}' ({size} bytes)")
        except ValueError as e:
            print(f"Error creating file: {e}")

    def create_directory(self, name: str) -> None:
        """
        Create a new subdirectory in the current directory.

        Args:
            name: Name of the new directory

        Raises:
            ValueError: If directory name is invalid
        """
        if not name or "/" in name:
            raise ValueError("Invalid directory name")

        try:
            new_dir = Directory(name)
            self._current_directory.add(new_dir)
            print(f"Created directory '{name}/'")
        except ValueError as e:
            print(f"Error creating directory: {e}")

    def change_directory(self, name: str) -> None:
        """
        Change the current working directory.

        Args:
            name: Name of the directory to navigate to ('..' for parent)

        Raises:
            ValueError: If directory doesn't exist or is a file
        """
        if name == "..":
            self._current_directory = self._root
            print("Changed to root directory")
            return

        component = self._current_directory.get_child(name)
        if component is None:
            raise ValueError(f"Directory '{name}' not found")

        if not isinstance(component, Directory):
            raise ValueError(f"'{name}' is not a directory")

        self._current_directory = component
        print(f"Changed to directory '{name}/'")

    def list_contents(self) -> None:
        """Display all contents of the current directory."""
        print(f"Contents of '{self._current_directory.name}/':")
        self._current_directory.display(4)

    def get_current_path(self) -> str:
        """Get the current directory path (simplified for this example)."""
        return f"/{self._current_directory.name}"
