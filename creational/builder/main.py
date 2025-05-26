from compute_builder import GamingComputerBuilder, OfficeComputerBuilder
from director import Director


def demonstrate_builder_pattern() -> None:
    """
    Demonstrate the Builder pattern by creating different computer configurations.
    """
    print("=== Builder Design Pattern Demonstration ===\n")

    # Create the director that will manage the construction process
    director = Director()

    try:
        # Build a premium gaming computer
        print("Building premium gaming computer:")
        gaming_builder = GamingComputerBuilder()
        director.builder = gaming_builder

        director.build_premium_computer()
        gaming_computer = gaming_builder.product
        gaming_computer.display()

        # Build a standard office computer
        print("Building standard office computer:")
        office_builder = OfficeComputerBuilder()
        director.builder = office_builder

        director.build_standard_computer()
        office_computer = office_builder.product
        office_computer.display()

        # Build a custom computer without using the director
        print("Building custom computer directly with builder:")
        custom_builder = GamingComputerBuilder()
        custom_builder.set_cpu("AMD Ryzen 9 7950X")
        custom_builder.set_gpu("AMD Radeon RX 7900 XTX")
        custom_builder.set_ram("64GB DDR5 6000MHz")
        custom_builder.set_storage("4TB NVMe SSD")
        custom_builder.set_cooling("Custom Liquid Cooling Loop")
        custom_builder.add_extras("OLED Display")
        custom_builder.add_extras("Mechanical Keyboard")

        custom_computer = custom_builder.product
        custom_computer.display()

    except ValueError as e:
        print(f"Error during computer construction: {e}")


if __name__ == "__main__":
    demonstrate_builder_pattern()
