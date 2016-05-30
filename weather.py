class Weather:
	def __init__(self, forecast):
		self.forecast = forecast

	def get_temp(self):
		return self.forecast['temperature_string']
