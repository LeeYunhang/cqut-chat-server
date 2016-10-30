
from pymongo import MongoClient
from ..configs import setMongoClient, getMongoClient

client = MongoClient('localhost', 27017)
setMongoClient(client)


__all__ = []