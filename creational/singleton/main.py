from database import DatabaseConnection

def demonstrate_singleton() -> None:
    """
    Demonstrate the Singleton pattern with the DatabaseConnection class.
    """
    print("=== Singleton Pattern Demonstration ===")

    # First connection instance
    params1 = {
        "host": "localhost",
        "port": 5432,
        "username": "admin",
        "password": "secret"
    }
    db1 = DatabaseConnection(params1)
    print(f"DB1 ID: {id(db1)}")

    # Second connection instance - should be the same as db1
    params2 = {
        "host": "example.com",
        "port": 3306
    }
    db2 = DatabaseConnection(params2)
    print(f"DB2 ID: {id(db2)}")

    # Verify they are the same instance
    print(f"Same instance? {db1 is db2}")

    # Show that connection parameters weren't overwritten
    print(f"DB1 params: {db1.connection_params}")
    print(f"DB2 params: {db2.connection_params}")

    # Demonstrate connection usage
    try:
        db1.connect()
        db1.execute_query("SELECT * FROM users")
        db2.execute_query("DROP TABLE temp_data") # db2 is same instance as db1
        db1.disconnect()

    except ConnectionError as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    demonstrate_singleton()