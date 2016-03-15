import numpy
import csv
import time
from weatherTuple import *

data =""
with open("../raw_data/raw_data_weather/processed_data.csv", 'rb') as raw_data_weather:
	weather_data = csv.reader(raw_data_weather, delimiter=" ", quotechar='|')
	for row in weather_data:
		row_data = csv.reader(row, delimiter=",", quotechar='|')
		count = 0
		for row_data in row:
			if row_data != ",":
	       			count = count + 1
			if count <= 6 and row_data != ",":
				if count == 1:
					date_data = time.strptime(str(row_data)[2:],"%y%m%d")
					data = data + time.strftime("%b", date_data)
					data = data + ","
					data = data + time.strftime("%d", date_data)
				else:
					data = data + str(row_data)
				if count != 6:
					data = data + ","
		count = 0
		data = data + "\n"

writeFile = open('../formatted_data/formatted_weather.csv', 'w')
writeFile.write(data)
