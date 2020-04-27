import threading
import time

from flask import Flask, request
from flask_restful import Api

from app.modules.OilTank import OilTank

app = Flask(__name__)
api = Api(app)

api.add_resource(OilTank, '/oleo')


def create_app():
    global app
    return app


def create_app_local():
    global app
    app.run()
