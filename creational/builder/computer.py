from typing import Any, Dict, List, Optional


class Computer:
    """
    The product class representing a computer with multiple components.
    This is the complex object that will be constructed by the builder.
    """

    def __init__(self) -> None:
        self._components: Dict[str, Any] = {
            "cpu": None,
            "gpu": None,
            "ram": None,
            "storage": None,
            "cooling": None,
            "extras": [],
        }

    def add_component(self, component_type: str, value: Any) -> None:
        """
        Add or update a component in the computer configuration.

        Args:
            component_type: The type of component
            value: The component specification or value
        """
        if component_type in self._components:
            if component_type == "extras":
                self._components["extras"].append(value)
            else:
                self._components[component_type] = value

        else:
            raise ValueError(f"Invalid component type: {component_type}")

    def get_specs(self) -> Dict[str, Any]:
        """
        Get the complete computer specifications.

        Returns:
            Dictionary containing all configured components
        """
        return self._components.copy()

    def display(self) -> None:
        """
        Display the computers configuration in a readable format.
        """
        print("\nComputer Configuration:")
        print("--------------------")
        for key, value in self._components.items():
            if key == "extras" and value:
                print(f"Extras: {', '.join(value)}")
            elif value is not None and key != "extras":
                print(f"{key.upper()}: {value}")

        print("--------------------")
