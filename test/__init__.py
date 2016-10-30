from sanic import Sanic
from sanic.response import json
from configs import setApp

app = Sanic(__name__)
setApp(app)

from test.test_middle import validate

@app.route("/")
async def test(request):
    return json({ "hello": "world" })

app.run(host='127.0.0.1', port=8000)
