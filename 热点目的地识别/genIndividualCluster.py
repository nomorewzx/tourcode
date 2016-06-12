# individual cluster csv file contains 5 cols, which are [uid,slat,slng,numberNotes,ulat,ulng]
# In touristInfo.csv, cols represent [uid, noteNumber, residenceLat, residenceLng]
# In clustersLabels.csv, cols represent [uid, spotLat, spotLng, clusterLabels, publicationDate]
# First, Merge touristInfo.csv and clustersLabels.csv files into one file which contains info below:
# 			[uid,clusterLabel,noteNumber,dist,publicationDate]
# The file we name as {pca_all.txt}, in which delimeter should be comma.
# What we really need is distSpotResidence, publicationDate and numberNotes.
import csv
import latlonDist
import datetime

def genAll():
	clusterLabels = csv.reader(open("clustersLabels.csv","r"))
	touristInfo = csv.reader(open("touristInfo.csv","r"))
	dictAll = {}
	touristDict = {}

	for row in touristInfo:
		touristDict[row[0]] = [row[1],row[2],row[3]]
	count = 0
	for row in clusterLabels:
		if row[0] in touristDict:
			for item in touristDict[row[0]]:
				row.append(item)
			dictAll[count] = row
			count+=1
	for key, value in dictAll.iteritems():
		temp = []
		spot = (float(value[1]),float(value[2]))
		residence = (float(value[-2]), float(value[-1]))
		dist = latlonDist._dist(residence,spot)
		temp.append(value[0]) #uid
		temp.append(value[3]) #clusterLabel
		temp.append(value[5]) #noteNumber
		temp.append(dist)	#distResidenceSpot
		temp.append(value[4]) #publicationDate
		dictAll[key]  = temp
	return dictAll

def genPCAFile():
	dictAll = genAll()
	f = open('PCAFile.csv','wb')
	writer = csv.writer(f)
	for key,value in dictAll.iteritems():
		writer.writerow(value)
	f.close()

# generate individual clusters
def genClusters():
	dictAll = genAll()
	clusterDict = {}
	for key,value in dictAll.iteritems():
		# extract month of the publication date
		dateNote = value[4]
		monthNote = datetime.datetime.strptime(dateNote,"%Y-%m-%d").month
		if value[1] not in clusterDict:
			clusterDict[value[1]] = [[value[0],value[2],value[3],monthNote]]
		else:
			clusterDict[value[1]].append([value[0],value[2],value[3],monthNote])
	for k,v in clusterDict.iteritems():
		f = open("./cluster/"+k+".csv","wb")
		writer = csv.writer(f)
		for items in v:
			writer.writerow(items)
		f.close()




if __name__ == '__main__':
	genClusters()