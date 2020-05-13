from flask_restful import Resource, request
import random
import time
import os
import requests
import json

oil_tank = {
    'nome': "oleo",
    'volume': random.randint(100, 200)
}

BASE_URL = os.environ['BASE_URL']

class OilTank(Resource):
    def __init__(self):
        self.oil_url = BASE_URL + '/oleo'
        
    def get(self):
        return oil_tank, 200
    
    def post(self):
        json_data = request.get_json(force=True)
        volume = json_data.get('volume', None)
        
        if volume is None:
            json = {
                "status_code": 400,
                "body": "Bad Request"
            }
            
        if oil_tank['volume'] < int(volume):
            json = {
                "status_code": 204,
                "body": "Nao ha volume suficiente no tanque"
            }
        else:
            json = {
                "status_code": 200,
                "nome": "oleo",
                "volume": volume 
            }
            print(f"Envia {volume}L de oleo")
            oil_tank['volume'] -= int(volume)
        
        # requests.post(url=REATOR_URL, json=json, headers={"Content_Type": "application/json"})
        return json
    
    def put(self):
        volume = random.randint(100, 200)
        oil_tank['volume'] += volume
        print(f"Recebe {volume}L de oleo")
        return 200

    def run(self):
        
        while (True):
            time.sleep(5)
            try:
                requests.put(url=self.oil_url)
            except Exception as e:
                print(e)             
