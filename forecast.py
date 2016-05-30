import json
import requests
from weather import Weather

filename = "keys.txt"
with open(filename, 'r') as f:
	stuff = f.read().splitlines()

stuff =  stuff[0].split('=')

apikey = stuff[1] 
city = requests.get('http://api.wunderground.com/api/' + apikey + '/conditions/q/CA/Santa_Ana.json')


r = Weather(city.json()['current_observation'])
print(r.get_temp())
