class WeatherTuple:	
	def __init__(self, month = "", day = 0, TMAX = 0, TMIN = 0, SNWD = 0, SNOW = 0, PRCP = 0):
		self.month = month
		self.day = day
		self.TMAX = TMAX
		self.TMIN = TMIN
		self.SNWD = SNWD
		self.SNOW = SNOW
		self.PRCP = PRCP
	
	def printWeather(self):
		print "Weather found on date " + str(self.month) + " " + str(self.day) + " TMAX " + str(self.TMAX) + " TMIN " + str(self.TMIN)

	def __str__(self):
		return "Weather found on date " + str(self.month) + " " + str(self.day) + " TMAX " + str(self.TMAX) + " TMIN " + str(self.TMIN)

	def month(self):
		return month

	def day(self):
		return day

	def TMAX(self):
		return TMAX

	def TMIN(self):
		return TMIN

	def SNWD(self):
		return SNWD

	def SNOW(self):
		return SNOW

	def PRCP(self):
		return PRCP
