from Crypto.Hash import MD5
from configs import get_config
import time


redis = get_config(key='redis')

def get_token(username, password):
    tmp = username + '+' + password + '+' + str(time.time())
    m = MD5.new()

    m.update(bytes(tmp, encoding='utf-8'))
    return m.hexdigest()

def parse_token(token):
    username = redis.get(token)
    return username if username else None

def padded(string):
    while len(string) != 32:
        string += 'x'

    return string