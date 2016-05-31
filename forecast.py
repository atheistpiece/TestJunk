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
city = requests.get('http://api.wunderground.com/api/' + apikey + '/conditions/q/CA/Santa_Ana.json')


r = Weather(city.json()['current_observation'])
print(r.get_temp())
