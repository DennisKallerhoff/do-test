import logging
import os
from mongodb_manager import MongoDBManager
from typing import Optional, Dict, List


def main(args: Dict[str, Optional[str]]):
    # setup logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    MONGO_DB_CONNECTION_STRING = os.getenv('DATABASE_CONNECTION')
    MONGO_DB_DATABASE = os.getenv('DATABASE')

    # Instantiate MongoDB manager
    # Initialize MongoDB manager and check the connection
    print(f"MONGO_DB_DATABASE: {MONGO_DB_DATABASE}")

    mongodb = MongoDBManager(MONGO_DB_CONNECTION_STRING, MONGO_DB_DATABASE)
    if not mongodb.is_connected():
        print(
            "MongoDB instance is not available. Please check the connection string.")
        sys.exit(1)

    return {
        "statusCode": 200,
        "body": "connected to mongodb"
    }