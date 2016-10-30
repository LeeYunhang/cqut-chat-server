from sanic import Sanic
from sanic.response import json
from pymongo import MongoClient

client = MongoClient('cqut-chat_mongo_1', 27017)
app = Sanic(__name__)

@app.route("/")
async def test(request):
    return json(client)

app.run(host="127.0.0.1", port=8888)

