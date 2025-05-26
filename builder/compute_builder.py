from abc import ABC, abstractmethod

from computer import Computer


class ComputerBuilder(ABC):
    """
    The abstract builder interface that defines all possible construction steps.
    """

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        """
        Reset the builder to create a new product.
        """
        self._computer = Computer()

    @property
    def product(self) -> Computer:
        """
        Get the constructed product and reset the builder.

        Returns:
            The fully constructed Computer object
        """
        computer = self._computer
        self.reset()
        return computer

    @abstractmethod
    def set_cpu(self, cpu: str) -> None:
        """
        Set the CPU component.
        """
        pass

    @abstractmethod
    def set_gpu(self, gpu: str) -> None:
        """
        Set the GPU component.
        """
        pass

    @abstractmethod
    def set_ram(self, ram: str) -> None:
        """
        Set the RAM component.
        """
        pass

    @abstractmethod
    def set_storage(self, storage: str) -> None:
        """
        Set the storage component.
        """
        pass

    @abstractmethod
    def set_cooling(self, cooling: str) -> None:
        """
        Set the cooling system.
        """
        pass

    @abstractmethod
    def add_extras(self, extra: str) -> None:
        """
        Add extra features or components.
        """
        pass


class GamingComputerBuilder(ComputerBuilder):
    """
    Concrete builder implementation for gaming computers.
    """

    def set_cpu(self, cpu: str = "Intel Core i9-13900K") -> None:
        """
        Set high-performance CPU for gaming.
        """
        self._computer.add_component("cpu", cpu)

    def set_gpu(self, gpu: str = "NVIDIA RTX 4090") -> None:
        """Set high-end GPU for gaming."""
        self._computer.add_component("gpu", gpu)

    def set_ram(self, ram: str = "32GB DDR5 5600MHz") -> None:
        """Set ample high-speed RAM for gaming."""
        self._computer.add_component("ram", ram)

    def set_storage(self, storage: str = "2TB NVMe SSD") -> None:
        """Set fast and spacious storage."""
        self._computer.add_component("storage", storage)

    def set_cooling(self, cooling: str = "Liquid Cooling System") -> None:
        """Set advanced cooling for high thermal loads."""
        self._computer.add_component("cooling", cooling)

    def add_extras(self, extra: str = "RGB Lighting") -> None:
        """Add gaming-specific extras."""
        self._computer.add_component("extras", extra)


class OfficeComputerBuilder(ComputerBuilder):
    """
    Concrete builder implementation for office computers.
    """

    def set_cpu(self, cpu: str = "Intel Core i5-12400") -> None:
        """Set efficient CPU for office tasks."""
        self._computer.add_component("cpu", cpu)

    def set_gpu(self, gpu: str = "Integrated Graphics") -> None:
        """Set basic graphics for office use."""
        self._computer.add_component("gpu", gpu)

    def set_ram(self, ram: str = "16GB DDR4 3200MHz") -> None:
        """Set sufficient RAM for office applications."""
        self._computer.add_component("ram", ram)

    def set_storage(self, storage: str = "512GB NVMe SSD") -> None:
        """Set adequate storage for documents."""
        self._computer.add_component("storage", storage)

    def set_cooling(self, cooling: str = "Air Cooling") -> None:
        """Set standard cooling for office use."""
        self._computer.add_component("cooling", cooling)

    def add_extras(self, extra: str = "Noise Reduction") -> None:
        """Add office-specific extras."""
        self._computer.add_component("extras", extra)
