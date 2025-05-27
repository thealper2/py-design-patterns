from typing import Protocol


class USASocketInterface(Protocol):
    """Interface for USA-style power sockets that expect 120V."""

    def voltage(self) -> int:
        """Returns the voltage provided by the socket."""
        pass

    def live(self) -> int:
        """Returns the live wire connection."""
        pass

    def neutral(self) -> int:
        """Returns the neutral wire connection."""
        pass


class USASocket:
    """Concrete implementation of a USA power socket (120V)."""

    def voltage(self) -> int:
        return 120

    def live(self) -> int:
        return 1

    def neutral(self) -> int:
        return -1
