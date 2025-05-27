from usa_socket import USASocketInterface


class ElectricKettle:
    """
    USA electric kettle that requires 120V and doesn't need earth connection.
    """

    def __init__(self, power_source: USASocketInterface):
        """
        Initialize the kettle with a power source.

        Args:
            power_source: The power source must implement USASocketInterface

        Raises:
            TypeError: If the power source doesn't implement USASocketInterface
            ValueError: If the voltage is incorrect
        """
        if (
            not hasattr(power_source, "voltage")
            or not hasattr(power_source, "live")
            or not hasattr(power_source, "neutral")
        ):
            raise TypeError("Power source must implement USASocketInterface")

        self._power_source = power_source

        if self._power_source.voltage() != 120:
            raise ValueError("This kettle requires 120V power source")

    def boil(self) -> str:
        """Boil water using the provided power source."""
        if self._power_source.live() == 1 and self._power_source.neutral() == -1:
            return "Boiling water with 120V"
        return "Cannot boil - incorrect power connection"
