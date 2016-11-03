from sanic import Sanic
from sanic.response import json
from pymongo import MongoClient
from configs import save_config
import redis

# initial----------------------------------------------
app = Sanic(__name__)
_redis = redis.Redis(host='redis', port=6379, db=0)
save_config(key='app', value=app)
save_config(key='redis', value=_redis)

client = MongoClient(host='mongo', port=27017)
save_config(key='mongo', value=client['cqut'])

save_config(key='app_key', value='cbe36a100c9977c74c296a6777e920ec')
save_config(key='enviroment', value='development')

import middles
import routes
import others
# -----------------------------------------------------

app.run(host="0.0.0.0", port=8888, debug=True)