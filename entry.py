from sanic import Sanic
from sanic.response import json
from pymongo import MongoClient

client = MongoClient('mongo', 27017)
app = Sanic(__name__)

@app.route("/")
async def test(request):
    return json(client)

app.run(host="0.0.0.0", port=8888)

