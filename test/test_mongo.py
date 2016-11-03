
from pymongo import MongoClient

client = MongoClient(host='mongo', port=27017)

print(client)

