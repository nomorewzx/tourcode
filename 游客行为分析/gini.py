#-*- coding:utf8 -*-

def calGini(monthlyTrafficFile):
	monthTraffic = []
	fopen = open(monthlyTrafficFile,'r')
	for line in fopen.readlines():
		line = line.replace('\n','')
		line = line.split(' ')
		monthTraffic.append(int(line[1]))
	averageTraffic = sum(monthTraffic)/float(len(monthTraffic))
	meanDiff = 0
	print monthTraffic
	for i in range(0,len(monthTraffic)):
		for j in range(0,len(monthTraffic)):
			meanDiff+=abs(monthTraffic[i]-monthTraffic[j])/float(len(monthTraffic)**2)
	gini = meanDiff/(averageTraffic*2)
	fopen.close()
	return gini
