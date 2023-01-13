import pymongo
from sensor.constant.database import DATABASE_NAME
import certifi
ca = certifi.where


class MongoDBClient:
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:

            if MongoDBClient.client is None:
                MONGO_DB_URL = MONGO_DB_URL
                MongoDBClient.client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
      
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e

