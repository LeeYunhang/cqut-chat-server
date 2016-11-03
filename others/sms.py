import urllib.request
import urllib.parse
from configs import get_config

def sms_request(mob_number, vcode):
    data = urllib.parse.urlencode({
        'appid': get_config('appid'),
        'to': mob_number,
        'content': get_config(key='content') + vcode,
        'signature': get_config('app_key')
    })
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.submail.cn/message/send.json", method='POST')
    request.add_header("Content-Type", "application/x-www-form-urlencoded;charset=utf-8")
    f = urllib.request.urlopen(request, data)
    return f.read().decode('utf-8')