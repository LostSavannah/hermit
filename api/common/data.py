from typing import TypeVar, Callable
from uuid import uuid4
from pydantic import BaseModel
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

username = "root"
password = "12345678"
host = "localhost"
port = 27017

connection_string = f"mongodb://{username}:{password}@{host}:{port}/"

T = TypeVar("T")

ConnectionCallback = Callable[[Database,], T]
CollectionCallback = Callable[[Collection,], T]

def connection(callback:ConnectionCallback) -> T:
    with MongoClient(connection_string) as client:
        database = client["antshive"]
        return callback(database)

def collection(name:str, callback:CollectionCallback) -> T:
    with MongoClient(connection_string) as client:
        database = client["antshive"]
        collection = database[name]
        return callback(collection)
    
def create_record(data:BaseModel):
    return {**dict(data), "code": str(uuid4())}