from typing import Any, Dict, Optional


class DatabaseConnection:
    """
    A singleton class that manages a database connection to ensure only one instance exists.

    Attributes:
        _instance (Optional[DatabaseConnection]): The single instance of the class
        connection_params (Dict[str, Any]): Dictonary storing connection parameters
        is_connected (bool): Flag indicating if the connection is active.
    """

    _instance: Optional["DatabaseConnection"] = None

    def __new__(cls, *args: Any, **kwargs: Any) -> "DatabaseConnection":
        """
        Override the __new__ method to control instance creation.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            The single instance of DatabaseConnection
        """
        if not cls._instance:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)

        return cls._instance

    def __init__(self, connection_params: Optional[Dict[str, Any]] = None) -> None:
        """
        Initialize the database connection with optional parameters.

        Args:
            connection_params: Dictionary containing connection parameters like host, port, username, etc. Defaults to None.
        """
        if not hasattr(self, "is_connected"):  # Prevent reinitialization
            self.connection_params = connection_params or {}
            self.is_connected = False

    def connect(self) -> None:
        """
        Establish the database connection.

        Raises:
            ConnectionError: If connection parameters are missing or connection fails.
        """
        if self.is_connected:
            print("Already connected to the database")
            return

        if not self.connection_params:
            raise ConnectionError("Connection parameters are not set")

        # Simulate connection establishment
        try:
            print(f"Connecting to database with params: {self.connection_params}")
            self.is_connected = True
            print("Database connection established successfully")

        except Exception as e:
            raise ConnectionError(f"Failed to connect to database: {str(e)}")

    def disconnect(self) -> None:
        """
        Close the database connection.
        """
        if not self.is_connected:
            print("No active connection to disconnect")
            return

        # Simulate disconnection
        print("Disconnecting from database...")
        self.is_connected = False
        print("Database connection closed")

    def execute_query(self, query: str) -> None:
        """
        Execute a database query.

        Args:
            query: The SQL query to execute

        Raises:
            ConnectionError: If not connected to the database.
        """
        if not self.is_connected:
            raise ConnectionError("Not connected to the database")

        print(f"Executing query: {query}")
        print("Query executed successfully")
