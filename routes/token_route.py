from sanic.response import json
from configs import get_config, account_is_none, username_invalid, \
    mob_number_invalid
from others import get_token, encrypt_password
from others import validate_username, validate_mob_number

redis = get_config(key='redis')
app = get_config('app')
mongo = get_config('mongo')
enviroment = get_config('enviroment')


@app.route('/api/token', methods=['POST'])
async def add_token(request):
    username = request.form.get('username')
    password = request.form.get('password')
    mob_number = request.form.get('mob_number')
    users_mongo = mongo.users

    password = encrypt_password(password)
    if username is None and mob_number is None:
        return json({ 'error': account_is_none }, 401)
    if username is not None and validate_username(username) is None:
        return json({ 'error': username_invalid }, 401)
    if mob_number is not None and validate_mob_number(mob_number) is None:
        return json({ 'error': mob_number_invalid })

    result = users_mongo.find_one({
        'username': username
    })
    if result.get('password') == password:
        token = get_token(username, password)
        redis.set(token, username)
        redis.expire(name=token, time=3600)

        return json({ 'token': token })
