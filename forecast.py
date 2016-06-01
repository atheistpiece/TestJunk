import requests
from weather import Weather

passwords = {}
filename = "keys.txt" #we'll store our api keys here

# create a dict with our api keys
with open(filename, 'r') as f:
	for line in f:
		(key,val) = line.split('=')
		passwords[key] = val.rstrip()

apikey = passwords['wunderground']

#get current conditions and 3 day forecast from wunderground
conditions = requests.get('http://api.wunderground.com/api/' + apikey + '/conditions/q/CA/Santa_Ana.json')
forecast = requests.get('http://api.wunderground.com/api/' + apikey + '/forecast/q/CA/Santa_Ana.json')

#create a weather object with our two forecasts
r = Weather(conditions.json(), forecast.json())

#get the forecast
todayWeather = r.get_forecast() #contains location, temp, weather, rain as keys

for key in todayWeather:
	print(todayWeather[key])
