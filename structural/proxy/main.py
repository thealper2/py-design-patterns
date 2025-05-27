import time
from abc import abstractmethod
from typing import Optional, Protocol, runtime_checkable


@runtime_checkable
class Image(Protocol):
    """Interface for real images and image proxies."""

    @abstractmethod
    def display(self) -> None:
        """Display the image."""
        ...

    @property
    @abstractmethod
    def filename(self) -> str:
        """Get the image filename."""
        ...

    @property
    @abstractmethod
    def size(self) -> int:
        """Get the image size in bytes."""
        ...


class RealImage(Image):
    """Real image class that loads the actual image file."""

    def __init__(self, filename: str):
        """
        Initialize with image filename.

        Args:
            filename: Path to the image file

        Raises:
            ValueError: If filename is empty
        """
        if not filename.strip():
            raise ValueError("Filename cannot be empty")
        self._filename = filename
        self._size: Optional[int] = None
        self._loaded = False

    @property
    def filename(self) -> str:
        return self._filename

    @property
    def size(self) -> int:
        """Get image size (loads file if not already loaded)."""
        if self._size is None:
            self._load_image()
        return self._size or 0

    def _load_image(self) -> None:
        """Simulate loading image from disk."""
        print(f"Loading image '{self._filename}' from disk...")
        time.sleep(2)  # Simulate slow loading
        # In a real app, we'd actually read the file and get its size
        self._size = len(self._filename) * 1000  # Simulated size
        self._loaded = True
        print(f"Finished loading image '{self._filename}'")

    def display(self) -> None:
        """Display the image (loads it first if needed)."""
        if not self._loaded:
            self._load_image()
        print(f"Displaying image '{self._filename}' ({self.size} bytes)")


class ImageProxy(Image):
    """
    Proxy class for images that controls access to the RealImage.
    Implements lazy loading and access control.
    """

    def __init__(self, filename: str):
        """
        Initialize with image filename.

        Args:
            filename: Path to the image file

        Raises:
            ValueError: If filename is empty
        """
        if not filename.strip():
            raise ValueError("Filename cannot be empty")
        self._filename = filename
        self._real_image: Optional[RealImage] = None

    @property
    def filename(self) -> str:
        return self._filename

    @property
    def size(self) -> int:
        """Get image size (delegates to real image when needed)."""
        if self._real_image is None:
            # Simulate getting size from metadata without full load
            return len(self._filename) * 1000  # Same simulated size as RealImage
        return self._real_image.size

    def display(self) -> None:
        """
        Display the image using lazy loading.

        Raises:
            RuntimeError: If image fails to load
        """
        try:
            if self._real_image is None:
                print(f"[Proxy] Creating real image for '{self._filename}'")
                self._real_image = RealImage(self._filename)

            print(f"[Proxy] Checking access permissions for '{self._filename}'")
            time.sleep(0.5)  # Simulate access check

            print(f"[Proxy] Forwarding display request for '{self._filename}'")
            self._real_image.display()
        except Exception as e:
            raise RuntimeError(f"Failed to display image: {e}") from e


class ImageGallery:
    """
    Client class that uses images through the proxy.
    Demonstrates how the proxy pattern can optimize performance.
    """

    def __init__(self):
        self._images: list[Image] = []

    def add_image(self, filename: str, use_proxy: bool = True) -> None:
        """
        Add an image to the gallery.

        Args:
            filename: Path to the image file
            use_proxy: Whether to use a proxy for this image

        Raises:
            ValueError: For invalid filenames
        """
        try:
            if use_proxy:
                self._images.append(ImageProxy(filename))
                print(f"Added proxy for image '{filename}'")
            else:
                self._images.append(RealImage(filename))
                print(f"Added real image '{filename}'")
        except ValueError as e:
            print(f"Error adding image: {e}")
            raise

    def display_all(self) -> None:
        """Display all images in the gallery."""
        print("\nDisplaying gallery contents:")
        for i, image in enumerate(self._images, 1):
            print(f"\nImage {i}: {image.filename}")
            try:
                start_time = time.time()
                image.display()
                elapsed = time.time() - start_time
                print(f"Display time: {elapsed:.2f} seconds")
            except RuntimeError as e:
                print(f"Error displaying image: {e}")

    def show_image_info(self) -> None:
        """Show info for all images without loading them."""
        print("\nGallery image info (no loading performed):")
        for i, image in enumerate(self._images, 1):
            print(f"Image {i}: {image.filename} ({image.size} bytes)")


def demonstrate_proxy():
    """Demonstrate the Proxy pattern with image loading."""
    try:
        gallery = ImageGallery()

        # Add some images (some with proxies, some without)
        gallery.add_image("vacation.jpg")
        gallery.add_image("profile.png", use_proxy=True)
        gallery.add_image("family.jpg", use_proxy=False)
        gallery.add_image("")

        # Show info without loading images
        gallery.show_image_info()

        # Display all images (will load as needed)
        gallery.display_all()

        print("\n=== Testing Error Cases ===")
        try:
            gallery.add_image("corrupted.jpg")
            gallery.display_all()
        except Exception as e:
            print(f"Expected error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    demonstrate_proxy()
