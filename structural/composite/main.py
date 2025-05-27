from file_system import FileSystem


def demonstrate_composite():
    """Demonstrate the Composite pattern with a file system simulation."""
    try:
        fs = FileSystem()

        print("\n=== Creating initial file structure ===")
        fs.create_directory("documents")
        fs.create_directory("pictures")

        fs.change_directory("documents")
        fs.create_file("report.txt", 1500)
        fs.create_file("notes.md", 800)

        fs.create_directory("work")
        fs.change_directory("work")
        fs.create_file("project.docx", 2500)

        fs.change_directory("..")  # Go back to documents
        fs.change_directory("..")  # Go back to root

        fs.change_directory("pictures")
        fs.create_file("vacation.jpg", 3500)
        fs.create_file("profile.png", 1200)

        fs.change_directory("..")

        print("\n=== Current file system structure ===")
        fs.list_contents()

        print("\n=== Calculating total sizes ===")
        root_size = fs._root.size()
        print(f"Total size of root: {root_size} bytes")

        # Try some error cases
        print("\n=== Testing error cases ===")
        try:
            fs.create_file("invalid/name", 100)  # Invalid name
        except ValueError as e:
            print(f"Expected error: {e}")

        try:
            fs.change_directory("nonexistent")  # Directory doesn't exist
        except ValueError as e:
            print(f"Expected error: {e}")

        try:
            fs.change_directory("report.txt")  # Not a directory
        except ValueError as e:
            print(f"Expected error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    demonstrate_composite()
