from pymongo import MongoClient, errors
from typing import Any, Dict, List


class MongoDBManager:
    """
    This class manages interactions with a MongoDB database.
    """

    def __init__(self, connection_string: str, database: str):
        """
        Initialize a connection to a MongoDB database.

        Parameters:
        connection_string (str): The connection string for the MongoDB database.
        database (str): The name of the database.
        """
        self.client = MongoClient(connection_string)
        self.db = self.client[database]

    def is_connected(self) -> bool:
        """
        Check if the MongoDB database is available.

        Returns:
        bool: True if the MongoDB database is available, else False.
        """
        try:
            self.client.admin.command('ismaster')
            return True
        except errors.ServerSelectionTimeoutError:
            return False
        except errors.OperationFailure:
            return False

    def save(self, collection_name: str, data: Dict[str, Any]) -> Any:
        """
        Save a document to the specified collection.

        Parameters:
        collection_name (str): The name of the collection.
        data (Dict[str, Any]): The document to save.

        Returns:
        Any: The result of the save operation.
        """
        collection = self.db[collection_name]
        return collection.insert_one(data)