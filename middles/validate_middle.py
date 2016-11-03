from sanic import Sanic
from sanic.response import json
from configs import get_config
from others import get_token, parse_token
from sanic.request import json_loads


app = get_config(key='app')
redis = get_config(key='redis')


@app.middleware('request')
async def login_middle(request):
    token = None

    if request.query_string:
        query_string_array = request.query_string.split('&')
        token = [query.split('=')[1] for query in query_string_array
                 if query.find('token') !=  -1][0]


    if token and redis.get(token):
        redis.expire(name=token, time=3600)
        return json({ 'msg': 'ok' })

    if request.url == '/api/token' and request.method.lower() == 'post':
        return
    elif request.url == '/api/users' and request.method.lower() == 'post':
        return
    elif request.url == '/api/sms' and request.method.lower() == 'post':
        return
    else:
        return validate_error()

def validate_error():
    return json({
        'error': 401
    }, 401)
