

from sanic.response import json as sainc_json
from configs import get_config
from configs import password_invalid, username_invalid,\
    username_unique, mob_number_unique, vcode_invalid, \
    mob_number_invalid
import urllib.request
import random
import re
import json
from others import sms_request, encrypt_password
import math
import time

app = get_config('app')
redis = get_config(key='redis')
mongo = get_config('mongo')

@app.route('/api/users', methods=['POST'])
async def add_user(request):
    mob_number = request.form.get('mob_number')
    vcode = request.form.get('vcode')
    password = request.form.get('password')
    username = request.form.get('username')
    users_mongo = mongo.users

    if validate_username(username) is None:
        return sainc_json({'error': username_invalid }, status=401)
    if validate_password(password) is None:
        return sainc_json({ 'error': password_invalid }, status=401)

    tmp = redis.get(mob_number)
    if tmp == vcode:
        query_result = users_mongo.find_one({ 'username': username })

        if query_result is not None:
            return sainc_json({ 'error': username_unique }, status=401)

        query_result = users_mongo.find_one({ 'mob_number': mob_number })
        if query_result is not None:
            return sainc_json({ 'error': mob_number_unique }, status=401)

        password = encrypt_password(password)
        users_mongo.insert_one({
            'username': username,
            'password': password,
            'mob_number': mob_number,
            'create_date': math.floor(time.time())
        })

        return sainc_json({ 'status': '用户创建成功' }, status=201)
    else:
        return sainc_json({ 'error': vcode_invalid }, status=401)


@app.route('/api/sms', methods=['POST'])
async def send_sms(request):
    mob_number = request.form.get('mob_number')

    if validate_mob_number(mob_number):

        random_number = str(random.random())[-4:]
        result = sms_request(mob_number, vcode=random_number)
        result = json.loads(result, encoding='UTF-8')

        redis.set(mob_number, random_number)
        redis.expire(mob_number, 300)

        return sainc_json({ 'error': result })
    else:
        return sainc_json({ 'error': mob_number_invalid })


def validate_mob_number(mob_number):
    return re.match('^[0-9]{11}$', mob_number)


def validate_username(username):
    if username is None:
        return
    elif len(username) < 4 or len(username) > 16:
        return
    elif re.match(pattern='[\'\" ]', string=username):
        return

    return True


def validate_password(password):
    if password is None:
        return
    elif len(password) < 6 or len(password) > 16:
        return
    elif re.match(pattern='[\'\"]', string=password):
        return

    return True



