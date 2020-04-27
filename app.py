from flask import Flask, request
import threading
import time

app = Flask(__name__)

volume = 0

@app.route('/secador', methods=['POST'])
def postVolume():
    data = request.get_json()

    global volume
    volume += (data['solucao'] * 0.99)

    response = {
        'volume': volume
    }

    return response


@app.route('/secador', methods=['GET'])
def getVolume():
    global volume
    response = {
        'biodiesel': volume
    }
    return response


class Secador(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            global volume
            if volume > 0:
                time.sleep(3)
                request = {
                    'biodiesel': volume
                }
                print('sending volume to storage tank')
                print(request)
                #fazer callout pro tanque de biodisel
                volume = 0



def create_app():
    global app
    print('starting logic thread...')
    sec = Secador()
    sec.start()
    print('logic thread started!')
    print('starting flask server')
    app.run()