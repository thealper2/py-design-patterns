from european_socket import EuropeanSocketInterface


class EuropeanToUSASocketAdapter:
    """
    Adapter that allows a USA device to work with a European socket.
    Converts 230V to 120V and handles the missing earth wire.
    """

    def __init__(self, european_socket: EuropeanSocketInterface):
        """
        Initialize the adapter with a European socket.

        Args:
            european_socket: The European socket to adapt

        Raises:
            TypeError: If the provided socket doesn't implement EuropeanSocketInterface
        """
        if not isinstance(european_socket, EuropeanSocketInterface):
            raise TypeError(
                "The provided socket must implement EuropeanSocketInterface"
            )
        self._european_socket = european_socket

    def voltage(self) -> int:
        """Convert 230V to 120V."""
        return self._european_socket.voltage() - 110

    def live(self) -> int:
        """Pass through the live wire unchanged."""
        return self._european_socket.live()

    def neutral(self) -> int:
        """Pass through the neutral wire unchanged."""
        return self._european_socket.neutral()
