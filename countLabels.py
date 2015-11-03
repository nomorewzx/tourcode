#-*- encoding:utf8 -*-

def countLabel(classifications):
	countDict = {}
	for label in classifications:
		if label not in countDict:
			countDict[label] = 1
		else:
			countDict[label]+=1
	f = open('countLabels.txt','w')
	for k,v in countDict.iteritems():
		f.write(str(k)+','+str(v)+'\n')
	f.close()

