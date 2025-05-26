from characters import CharacterRegistry, GameCharacter


def demonstrate_prototype_pattern() -> None:
    """
    Demonstrate the Prototype pattern by creating and cloning character templates.
    """
    print("=== Prototype Design Pattern Demonstration ===\n")

    try:
        # Create prototype registry
        registry = CharacterRegistry()

        # Create and register some base prototypes
        warrior = GameCharacter(
            character_type="Warrior",
            health=150,
            mana=30,
            abilities={"Sword Mastery": 5, "Shield Block": 4},
            appearance={"armor": "Plate", "weapon": "Greatsword", "color": "Steel"},
            inventory=["Health Potion", "Repair Kit"],
        )

        mage = GameCharacter(
            character_type="Mage",
            health=70,
            mana=150,
            abilities={"Fireball": 5, "Teleport": 3, "Shield": 2},
            appearance={"robe": "Silk", "staff": "Elderwood", "color": "Blue"},
            inventory=["Mana Potion", "Spellbook"],
        )

        registry.register_prototype("default_warrior", warrior)
        registry.register_prototype("default_mage", mage)

        # Display registered prototypes
        print("Registered prototypes:", registry._prototypes)

        # Clone and customize a warrior
        print("\nCreating customized warrior:")
        custom_warrior = registry.clone_prototype(
            "default_warrior",
            health=180,
            abilities={"Sword Mastery": 6, "Berserker Rage": 3},
            appearance={"armor": "Dragonbone", "color": "Red"},
            inventory=["Health Potion", "Strength Elixir", "War Banner"],
        )
        custom_warrior.display()

        # Clone and customize a mage
        print("\nCreating customized mage:")
        custom_mage = registry.clone_prototype(
            "default_mage",
            character_type="Archmage",
            mana=200,
            abilities={"Fireball": 7, "Ice Storm": 4, "Teleport": 5},
            inventory=["Mana Potion", "Ancient Tome", "Crystal Ball"],
        )
        custom_mage.display()

        # Demonstrate serialization/deserialization
        print("\nDemonstrating serialization:")
        mage_json = mage.to_json()
        print(f"Serialized mage: {mage_json[:80]}...")

        deserialized_mage = GameCharacter.from_json(mage_json)
        print("\nDeserialized mage:")
        deserialized_mage.display()

        # Show that clones are independent
        print("Demonstrating clone independence:")
        original = registry.clone_prototype("default_warrior")
        clone = original.clone()

        original.add_item("Golden Apple")
        clone.add_ability("Whirlwind", 2)

        print("\nOriginal after modification:")
        original.display()

        print("\nClone after modification:")
        clone.display()

    except Exception as e:
        print(f"Error in prototype demonstration: {str(e)}")


if __name__ == "__main__":
    demonstrate_prototype_pattern()
