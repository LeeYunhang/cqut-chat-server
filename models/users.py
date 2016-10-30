from ..configs import getMongoClient, setMongoClient

client = getMongoClient()
db = client.cqutChat
collection = db.users

async def queryUsers(**kwargs):
    return await collection.find(kwargs)