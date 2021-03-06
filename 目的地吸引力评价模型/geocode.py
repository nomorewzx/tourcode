# -*- coding: utf-8 -*-
import csv
import latlonDist

def genGeoCodeDict():
	geocodeBuffer = {}
	with open('geocode/geocoding-spot.csv') as csvfile:
		spotGeocodeReader = csv.reader(csvfile)
		for row in spotGeocodeReader:
			geocodeBuffer[row[0]] = (float(row[1]),float(row[2]))
	with open('geocode/geocoding.csv') as csvfile:
		geocodeReader = csv.reader(csvfile)
		for row in geocodeReader:
			geocodeBuffer[row[0]] = (float(row[1]),float(row[2]))
	return geocodeBuffer

def convertGeoCode(filename,destname):
	geocodeBuffer = genGeoCodeDict()
	writeRows = []
	with open(filename) as rawCSV:
		rawContent = csv.reader(rawCSV)
		for row in rawContent:
			if row[1] != 'null' and row[1] in geocodeBuffer:
				distance = latlonDist._dist(geocodeBuffer[row[1]],geocodeBuffer[destname])
				writeRows.append((0,row[2],distance,0))
	print '%d tours are found' % len(writeRows)
	with open('data/'+filename,'wb') as destCSV:
		writer = csv.writer(destCSV)
		for row in writeRows:
			writer.writerow(row)



if __name__ == '__main__':
	# convertGeoCode('10195.csv','西安')
	convertGeoCode('./data/10444.csv','青岛')
	convertGeoCode('./data/10030.csv','三亚')
	convertGeoCode('./data/10136.csv','九寨沟')
	convertGeoCode('./data/10284.csv','泰山')


