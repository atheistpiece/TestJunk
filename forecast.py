import json
import requests
from weather import Weather

passwords = {}
filename = "keys.txt"
with open(filename, 'r') as f:
	for line in f:
		(key,val) = line.split('=')
		passwords[key] = val.rstrip()

apikey = str(passwords['wunderground'])
conditions = requests.get('http://api.wunderground.com/api/' + apikey + '/conditions/q/CA/Santa_Ana.json')
forecast = requests.get('http://api.wunderground.com/api/' + apikey + '/forecast/q/CA/Santa_Ana.json')

r = Weather(conditions.json(), forecast.json())

new = r.get_forecast()

