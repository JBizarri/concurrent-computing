from threading import Thread
from flask import Flask, request
from flask_restful import Api

from app.modules.OilTank.OilTank import OilTank

app = Flask(__name__)
api = Api(app)

api.add_resource(OilTank, '/oleo')


def create_app():
    global app
    threads_classses = [OilTank]
    
    threads = [Thread(target=thread().run) for thread in threads_classses]
    for thread in threads:
        thread.start()
        
    return app


def create_app_local():
    global app
    threads_classses = [OilTank]
    
    threads = [Thread(target=thread().run) for thread in threads_classses]
    for thread in threads:
        thread.start()
    
    app.run()
