from sanic import Sanic
from configs import getApp, setApp

app = getApp()

@app.middleware('request')
async def validate(request):
    print('hello world')


# __all__ = [validate]