import numpy
import csv
from weatherTuple import *
from sys import argv
from time import strftime

script, filename = argv
currentFile = open(filename)
currentLine = currentFile.readline()
while currentLine != "":
	items = currentLine.split(',')
	for item in items:
		print item
	print "\n"
	currentLine = currentFile.readline()
