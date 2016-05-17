#-*- coding:utf8 -*-
import gini

def main():
	#所有国外目的地列表
	abroadSpots = []
	for i in open('offshore_destination.txt','r').readlines():
		abroadSpots.append(i.strip())
	print abroadSpots[2]

	#目的地为国外的游记列表
	notesWithAbroadDestinations = []
	for i in open('notewithdate.txt','r').readlines():
		if i.split(',')[5] in abroadSpots:
			notesWithAbroadDestinations.append(i.split(',')[2])

	print len(notesWithAbroadDestinations)
	# 出境游月份-人次字典
	monthTrafficAbroad = {}
	for i in notesWithAbroadDestinations:
		month = (int)(i.split('-')[1])
		if month not in monthTrafficAbroad:
			monthTrafficAbroad[month] = 1
		else:
			monthTrafficAbroad[month]+=1

	for k,v in monthTrafficAbroad.items():
		print k,
		print '----',
		print v


if __name__ == '__main__':
	main()
	print gini.calGini('./data/domesticMonthlyTraffic.txt')
	print gini.calGini('./data/abroadMonthlyTraffic.txt')
	print gini.calGini('./data/authorityOverSeasTripTrafficQuartly.txt')
