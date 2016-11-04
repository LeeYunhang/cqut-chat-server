
configs = {}

configs['app_key'] = 'cbe36a100c9977c74c296a6777e920ec'
configs['enviroment'] = 'development'
configs['appid'] = '12353'
configs['content'] = '【CQUT-CHAT】您的验证码是：'

def save_config(key, value):
    configs[key] = value

def get_config(key):
    return configs.get(key)


username_invalid = { 'code': 1, 'msg': '用户名长度在4到16之间, 不能有空格, 引号' }
password_invalid = { 'code': 2, 'msg': '密码长度在6到16之间, 不能有引号' }
username_unique = { 'code': 3, 'msg': '用户名不能重复' }
mob_number_unique = { 'code': 4, 'msg': '手机号不能重复' }
mob_number_invalid = { 'code': 5, 'msg': '手机号格式不合法' }
vcode_invalid = { 'code': 6, 'msg': '验证码错误, 重新发送验证码' }
account_is_none = { 'code': 7, 'msg': '登陆账号(手机号/用户名)不能为空' }
token_invalid = { 'code':8, 'msg': 'token不正确或者token已过期' }

__all__ = [save_config, get_config,
           username_invalid, password_invalid,
           username_unique, mob_number_unique,
           vcode_invalid, account_is_none, token_invalid
           ]