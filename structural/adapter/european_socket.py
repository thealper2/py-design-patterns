from typing import Protocol, runtime_checkable


@runtime_checkable
class EuropeanSocketInterface(Protocol):
    """Interface for European-style power sockets that expect 230V."""

    def voltage(self) -> int:
        """Returns the voltage provided by the socket."""
        pass

    def live(self) -> int:
        """Returns the live wire connection."""
        pass

    def neutral(self) -> int:
        """Returns the neutral wire connection."""
        pass

    def earth(self) -> int:
        """Returns the earth wire connection."""
        pass


class EuropeanSocket:
    """Concrete implementation of a European power socket (230V)."""

    def voltage(self) -> int:
        return 230

    def live(self) -> int:
        return 1

    def neutral(self) -> int:
        return -1

    def earth(self) -> int:
        return 0
