from typing import Optional

from compute_builder import ComputerBuilder


class Director:
    """
    The director class that defines the construction process using a builder.
    Knows how to construct different types of computer configurations.
    """

    def __init__(self) -> None:
        self._builder: Optional[ComputerBuilder] = None

    @property
    def builder(self) -> ComputerBuilder:
        """Get the current builder instance."""
        if self._builder is None:
            raise ValueError("Builder not set")
        return self._builder

    @builder.setter
    def builder(self, builder: ComputerBuilder) -> None:
        """Set the builder to use for construction."""
        self._builder = builder

    def build_basic_computer(self) -> None:
        """Construct a computer with minimal configuration."""
        self.builder.set_cpu()
        self.builder.set_ram()
        self.builder.set_storage()

    def build_standard_computer(self) -> None:
        """Construct a computer with standard configuration."""
        self.build_basic_computer()
        self.builder.set_gpu()
        self.builder.set_cooling()

    def build_premium_computer(self) -> None:
        """Construct a computer with all premium features."""
        self.build_standard_computer()
        self.builder.add_extras()
