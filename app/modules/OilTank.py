from flask_restful import Resource
import random

oil_tank = {
    'Nome': 'Tanque de oleo',
    'volume': random.randint(100, 200)
}


class OilTank(Resource):
    def get(self):
        return oil_tank
