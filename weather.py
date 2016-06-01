class Weather:
	#setup the object, get two lists from two api calls to wunderground
	def __init__(self, forecast1, forecast2):
		self.forecast1 = forecast1['current_observation']
		self.forecast2 = forecast2['forecast']

#		print(self.forecast2, self.forecast1)

	def get_temp(self):
		return self.forecast1['temperature_string']

	def get_weather(self):
		return self.forecast1['weather']

	def get_location(self):
		pass

	def get_wind(self):
		pass

	def get_rain(self):
		return self.forecast2['txt_forecast']['forecastday'][6]['pop']


	def get_forecast(self):
		self.info = {}
		self.info['temp'] = self.get_temp()
		self.info['weather'] = self.get_weather()
		self.info['rain'] = self.get_rain()
		return self.info