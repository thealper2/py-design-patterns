from adapter import EuropeanToUSASocketAdapter
from european_socket import EuropeanSocket
from kettle import ElectricKettle


def demonstrate_adapter():
    """Demonstrate the adapter pattern with the socket example."""
    try:
        # Create a European socket (incompatible with USA kettle)
        european_socket = EuropeanSocket()

        # Create an adapter to make the European socket work with USA devices
        adapter = EuropeanToUSASocketAdapter(european_socket)

        # Create a USA kettle that works with the adapted socket
        kettle = ElectricKettle(adapter)

        # Use the kettle
        print(kettle.boil())  # Output: Boiling water with 120V

        # Try to use the European socket directly (should fail)
        try:
            bad_kettle = ElectricKettle(european_socket)  # type: ignore
            print(bad_kettle.boil())
        except ValueError as e:
            print(f"Expected error when not using adapter: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    demonstrate_adapter()
