class Weather:
	#setup the object, get two lists from two api calls to wunderground
	#forecast1 = current conditions, forecast2 = 3 day forecast
	#we can do more with the info later, for now, just the basics
	def __init__(self, forecast1, forecast2):
		self.forecast1 = forecast1['current_observation']
		self.forecast2 = forecast2['forecast']	# this is needed for chance of rain, which isnt in current conditions

	def get_temp(self):
		return self.forecast1['temperature_string']

	def get_weather(self):
		return self.forecast1['weather']

	def get_location(self): #get city name
		return self.forecast1['display_location']['full'] #nested dictionaries

	def get_wind(self):
		pass

	def get_rain(self):
		return self.forecast2['txt_forecast']['forecastday'][6]['pop'] #we have a nested dictionarys, forecastday
																	   #contains nested lists of dictionaries, confused?

	#gather all the info we need to return the day's basic forecast
	def get_forecast(self):
		self.info = {}
		self.info['temp'] = self.get_temp()
		self.info['weather'] = self.get_weather()
		self.info['rain'] = self.get_rain()
		self.info['location'] = self.get_location()

		return self.info