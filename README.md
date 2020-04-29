# concurrent-computing

## The API

This API was designed to be hosted on a Heroku App.

## How to run

#### On Heroku

* Fork or clone this repository to your own GitHub repository
* Upload it to Heroku
* Set up and enviroment variable. The KEY should be `BASE_URL` and the VALUE your API URL on Heroku
* Deploy master to Heroku
* Open App

#### Local

* Install the requirements from requirements.txt using `pip3 install -r requirements`
* Set up an enviroment variable for `BASE_URL`. It should be `htpp://localhost:5000` by default.
* Run main.py file using `python3 main.py`


## How it works

The API constantly updates the oil volume every 5 seconds to a random value between 100 and 200 liters.
You or someone else can make a POST request at `/oleo` and ask for oil, if the tank has enough oil it'll return your the amount you asked for.

Request Example:
```
json = {
  "volume": 30
}
```
