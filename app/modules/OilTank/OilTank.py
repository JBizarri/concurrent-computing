from flask_restful import Resource
import random
import time
import os
import requests

oil_tank = {
    'Nome': 'Tanque de oleo',
    'volume': random.randint(100, 200)
}

BASE_URL = os.environ['BASE_URL']

class OilTank(Resource):
    def __init__(self):
        self.endpoint = '/oleo'
    def get(self):
        return oil_tank, 200
    
    def put(self):
        oil_tank['volume'] += random.randint(100, 200)
        return 200

    def run(self):
        url = BASE_URL + self.endpoint
        while (True):
            time.sleep(5)
            try:
                requests.put(url)
            except Exception as e:
                print(e)             
        