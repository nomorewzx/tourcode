import csv
def main():
	fopen = open("touristInfo.csv")
	touristInfoReader = csv.reader(fopen)
	notegeodataReader = csv.reader(open("notegeodata.csv"))

def genLabelUser(classifications):
	#gen csv file with info: (uid, spot_lat, spot_lng, cluster_label,publication date)
	result = classifications
	notegeodataReader = csv.reader(open("../python_analytic_data/notegeodata.csv"))
	index = 0
	dictCluster = {}
	notes = []
	for row in notegeodataReader:
		notes.append(row)
	for i in range(0,len(classifications)):
		notes[i].append(classifications[i])
	fopen = open("../python_analytic_data/clustersLabels.csv","w")
	writer = csv.writer(fopen)
	for i in range(0,len(notes)):
		if classifications[i] != None:
			writer.writerow((notes[i][1],notes[i][8],notes[i][7],notes[i][9],notes[i][6]))
	fopen.close()
def genLabelUser2():
	notegeodataReader = csv.reader(open("../python_analytic_data/notegeodata.csv"))
	for row in notegeodataReader:
		print row
if __name__ == '__main__':
	genLabelUser2()

	

