class CrimeTuple:	
	def __init__(self, month = "", day = 0,  district = 0, time = 0, description = "", neighborhood = 0, xcoord = 0.0, ycoord = 0.0, ILEADSStr = "", CADStr = ""):
		self.month = month
		self.day = day
		self.time = time
		self.district = district
		self.description = description
		self.neighborhood = neighborhood
		self.xcoord = xcoord
		self.ycoord = ycoord
		self.ILEADSAddr = ILEADSAddr
		self.ILEADSStr = ILEADSStr
		self.CADStr = CADStr
	
	def printCrime(self):
		print "Crime found on date " + str(self.month) + " " + str(self.day) +  " at time " + str(self.description) + " at  " + str(self.CADStr)

	def __str__(self):
		return "Crime found on date " + str(self.month) + " " + str(self.day) +  " at time " + str(self.description) + " at  " + str(self.CADStr) 

	def month(self):
		return month

	def day(self):
		return day

	def time(self):
		return time

	def district(self):
		return district

	def description(self):
		return description

	def neighborhood(self):
		return neighborhood

	def xcoord(self):
		return xcoord

	def ycoord(self):
		return ycoord

	def ILEADSAddr(self):
		return ILEADSAddr

	def ILEADSStr(self):
		return ILEADSStr

	def CADStr(self):
		return CADStr
