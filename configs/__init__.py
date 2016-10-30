def setApp(_app):
    global app
    app = _app

def getApp():
    global app
    return app

def setMongoClient(client):
    global mongoClient
    mongoClient = client

def getMongoClient():
    global mongoClient
    return mongoClient

__all__ = [setApp, getApp,   \
           setMongoClient, getMongoClient, \
           ]