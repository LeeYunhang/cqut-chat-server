from sanic.response import json

async def login(request):
    if (request.form.get('username') != 'cfc' or request.form.get('password') != 'cfc'):
        return json({
            'error': {
                'description': '用户名或密码不对'
            }
        }, 401)
    else:
        return True