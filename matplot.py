#-*- coding:utf8 -*-
import numpy as np
import matplotlib.pyplot as plt
import kMeans
import base
import sklearn.datasets as d


def generateRandomDots():
	LEN = 500
	# 随机生成1000个数
	plt.subplot(121)
	plt.title('(a)')
	xrarray = np.random.random(size=LEN)*20
	yrarray = np.random.random(size=LEN)*20
	for i in range(LEN):
		plt.plot(xrarray[i],yrarray[i],'ro')
	plt.axis([0,20,0,20])

	# 使用sklearn的make_blobs函数生成 聚类样例数据
	blobs = d.make_blobs(LEN,centers=3,center_box=(0,20))
	plt.subplot(122)
	plt.title("(b)")
	plt.axis([0,20,0,20])
	plt.plot(blobs[0][:, 0], blobs[0][:, 1], 'g^')
	plt.show()

def printBasicInfo(centroids,clusterAssment,norMat):
	minCount = 10000
	maxCount = 0

def main():
	dataSet = kMeans.loadfromcsv('./data/cluster/8.csv')
	dataMat = np.mat(dataSet)
	# normalize dataMat
	norMat = kMeans.normalize(dataMat)
	# centroids is the center of clusters
	# clusterAssment[cluster_index,deviation],in which deviation represents the dist
	# from current point to centroids. 
	centroids, clusterAssment = kMeans.biKmeans(norMat,4)
	cluster_label = clusterAssment[:,0]
	clusters = [[],[],[],[]]
	for i in range(0,len(cluster_label)):
		clusters[(int)(cluster_label[i])].append(np.asarray(norMat)[i])
	clusters = np.asarray(clusters)
	for i in range(0,len(clusters)):
		clusters[i] = np.asarray(clusters[i])
	clusters = np.asarray(clusters)

	max_cluster = 0
	min_cluster = 0
	for i in range(0,len(clusters)):
		if minCount > len(clusters[i]):
			minCount = len(clusters[i])
		if maxCount < len(clusters[i]):
			maxCount = len(clusters[i])
		if longest_cluster < len(clusters[i]):
			longest_cluster = i
		if len(clusters[max_cluster]) < len(clusters[i]):
			max_cluster = i
		if len(clusters[min_cluster]) > len(clusters[i]):
			min_cluster = i
		print "%d cluster has %d elements " % (i, len(clusters[i])),
		print "the centroids is",
		print centroids[i]
	number_weight = float(len(clusters[max_cluster]))/(len(clusters[min_cluster]))
	print centroids[max_cluster]
	di = base.dunn(clusters)
	NDunnIndex = di*(maxCount/minCount)
	print di
	print NDunnIndex

	print "original dunn is %f" % di
	print "weighted dunn is %f" % (number_weight*di)

def plot2Cluster():
	dataSetShangHai = kMeans.loadfromcsv('./data/cluster/8.csv')
	dataSetXiAn = kMeans.loadfromcsv('./data/cluster/51.csv')

	dataMatXiAn = np.mat(dataSetXiAn)
	dataMatShangHai = np.mat(dataSetShangHai)

	norMatXiAn = kMeans.normalize(dataMatXiAn)
	norMatShangHai = kMeans.normalize(dataMatShangHai)

# shanghai
	plt.subplot(121)
	
	pointClusNumShangHai = clusterAssmentShangHai[:,0].A.T
	n = np.shape(pointClusNumShangHai)[1]
	plt.title(u'上海')
	for i in range(n):
		if 0.0 == pointClusNumShangHai.item(i):
			plt.plot(norMatShangHai[i,0],norMatShangHai[i,1],'g^')
		elif 1.0 == pointClusNumShangHai.item(i):
			plt.plot(norMatShangHai[i,0],norMatShangHai[i,1],'b*')
		elif 2.0 == pointClusNumShangHai.item(i):
			plt.plot(norMatShangHai[i,0],norMatShangHai[i,1],'k<')
		elif 3.0 == pointClusNumShangHai.item(i):
			plt.plot(norMatShangHai[i,0],norMatShangHai[i,1],'ms')

	plt.plot(centroidsShangHai[:,0],centroidsShangHai[:,1],'ro')
	plt.axis([0,4.0,0,12])
	plt.xticks([0,1,2,3])
	# plt.xlabel(u'Distance Index')
	# plt.ylabel(u'Activity Degree Index')


	# XiAn
	plt.subplot(122)
	pointClusNumXiAn = clusterAssmentXiAn[:,0].A.T
	n = np.shape(pointClusNumXiAn)[1]
	plt.title(u'西安')
	for i in range(n):
		if 0.0 == pointClusNumXiAn.item(i):
			plt.plot(norMatXiAn[i,0],norMatXiAn[i,1],'g^')
		elif 1.0 == pointClusNumXiAn.item(i):
			plt.plot(norMatXiAn[i,0],norMatXiAn[i,1],'b*')
		elif 2.0 == pointClusNumXiAn.item(i):
			plt.plot(norMatXiAn[i,0],norMatXiAn[i,1],'k<')
		elif 3.0 == pointClusNumXiAn.item(i):
			plt.plot(norMatXiAn[i,0],norMatXiAn[i,1],'ms')

	plt.plot(centroidsXiAn[:,0],centroidsXiAn[:,1],'ro')
	plt.axis([0,4.0,0,12])
	plt.xticks([0,1,2,3])
	# plt.xlabel(u'Distance Index')
	# plt.ylabel(u'Activity Degree Index')
	plt.show()

def plotCluster():
	dataSetShangHai = kMeans.loadfromcsv('./data/cluster/8.csv')
	dataSetXiAn = kMeans.loadfromcsv('./data/cluster/51.csv')
	dataSetQingDao = kMeans.loadfromcsv('./data/cluster/19.csv')
	dataSetSanYa = kMeans.loadfromcsv('./data/cluster/14.csv')
	dataSetJiuZhaigou = kMeans.loadfromcsv('./data/cluster/1.csv')
	dataSetTaiShan = kMeans.loadfromcsv('./data/cluster/36.csv')

	dataMatXiAn = np.mat(dataSetXiAn)
	dataMatQingDao = np.mat(dataSetQingDao)
	dataMatShangHai = np.mat(dataSetShangHai)
	dataMatSanYa = np.mat(dataSetSanYa)
	dataMatTaiShan = np.mat(dataSetTaiShan)
	dataMatJiuZhaigou = np.mat(dataSetJiuZhaigou)


	norMatXiAn = kMeans.normalize(dataMatXiAn)
	norMatQingDao = kMeans.normalize(dataMatQingDao)
	norMatShangHai = kMeans.normalize(dataMatShangHai)
	norMatSanYa = kMeans.normalize(dataMatSanYa)
	norMatTaiShan = kMeans.normalize(dataMatTaiShan)
	norMatJiuZhaigou = kMeans.normalize(dataMatJiuZhaigou)

	centroidsShangHai, clusterAssmentShangHai = kMeans.biKmeans(norMatShangHai,4)
	centroidsXiAn, clusterAssmentXiAn = kMeans.biKmeans(norMatXiAn,4)
	centroidsQingDao, clusterAssmentQingDao = kMeans.biKmeans(norMatQingDao,4)
	centroidsSanYa, clusterAssmentSanYa = kMeans.biKmeans(norMatSanYa,4)
	centroidsJiuZhaigou, clusterAssmentJiuZhaigou = kMeans.biKmeans(norMatJiuZhaigou,4)
	centroidsTaiShan, clusterAssmentTaiShan = kMeans.biKmeans(norMatTaiShan,4)

	print "==================上海聚类结果=========="
	printBasicInfo(centroidsShangHai,clusterAssmentShangHai,norMatShangHai)

	print "==================西安聚类结果=========="
	printBasicInfo(centroidsXiAn, clusterAssmentXiAn, norMatXiAn)

	print "==================青岛聚类结果=========="
	printBasicInfo(centroidsQingDao, clusterAssmentQingDao, norMatQingDao)

	print "==================三亚聚类结果=========="
	printBasicInfo(centroidsSanYa, clusterAssmentSanYa, norMatSanYa)

	print "==================九寨沟聚类结果========"
	printBasicInfo(centroidsJiuZhaigou, clusterAssmentJiuZhaigou, norMatJiuZhaigou)

	print "==================泰山聚类结果=========="
	printBasicInfo(centroidsTaiShan, clusterAssmentTaiShan, norMatTaiShan)

	# shanghai
	plt.subplot(321)
	
	pointClusNumShangHai = clusterAssmentShangHai[:,0].A.T
	n = np.shape(pointClusNumShangHai)[1]
	plt.title(u'上海')
	for i in range(n):
		if 0.0 == pointClusNumShangHai.item(i):
			plt.plot(norMatShangHai[i,0],norMatShangHai[i,1],'g^')
		elif 1.0 == pointClusNumShangHai.item(i):
			plt.plot(norMatShangHai[i,0],norMatShangHai[i,1],'b*')
		elif 2.0 == pointClusNumShangHai.item(i):
			plt.plot(norMatShangHai[i,0],norMatShangHai[i,1],'k<')
		elif 3.0 == pointClusNumShangHai.item(i):
			plt.plot(norMatShangHai[i,0],norMatShangHai[i,1],'ms')

	plt.plot(centroidsShangHai[:,0],centroidsShangHai[:,1],'ro')
	plt.axis([0,4.0,0,12])
	plt.xticks([0,1,2,3])
	# plt.xlabel(u'Distance Index')
	# plt.ylabel(u'Activity Degree Index')


	# XiAn
	plt.subplot(322)
	pointClusNumXiAn = clusterAssmentXiAn[:,0].A.T
	n = np.shape(pointClusNumXiAn)[1]
	plt.title(u'西安')
	for i in range(n):
		if 0.0 == pointClusNumXiAn.item(i):
			plt.plot(norMatXiAn[i,0],norMatXiAn[i,1],'g^')
		elif 1.0 == pointClusNumXiAn.item(i):
			plt.plot(norMatXiAn[i,0],norMatXiAn[i,1],'b*')
		elif 2.0 == pointClusNumXiAn.item(i):
			plt.plot(norMatXiAn[i,0],norMatXiAn[i,1],'k<')
		elif 3.0 == pointClusNumXiAn.item(i):
			plt.plot(norMatXiAn[i,0],norMatXiAn[i,1],'ms')

	plt.plot(centroidsXiAn[:,0],centroidsXiAn[:,1],'ro')
	plt.axis([0,4.0,0,12])
	plt.xticks([0,1,2,3])
	# plt.xlabel(u'Distance Index')
	# plt.ylabel(u'Activity Degree Index')

	# QingDao
	plt.subplot(323)
	pointClusNumQingDao = clusterAssmentQingDao[:,0].A.T
	n = np.shape(pointClusNumQingDao)[1]
	plt.title(u'青岛')
	for i in range(n):
		if 0.0 == pointClusNumQingDao.item(i):
			plt.plot(norMatQingDao[i,0],norMatQingDao[i,1],'g^')
		elif 1.0 == pointClusNumQingDao.item(i):
			plt.plot(norMatQingDao[i,0],norMatQingDao[i,1],'b*')
		elif 2.0 == pointClusNumQingDao.item(i):
			plt.plot(norMatQingDao[i,0],norMatQingDao[i,1],'k<')
		elif 3.0 == pointClusNumQingDao.item(i):
			plt.plot(norMatQingDao[i,0],norMatQingDao[i,1],'ms')

	plt.plot(centroidsQingDao[:,0],centroidsQingDao[:,1],'ro')
	plt.axis([0,4.0,0,12])
	plt.xticks([0,1,2,3])
	# plt.xlabel(u'Distance Index')
	# plt.ylabel(u'Activity Degree Index')

	# SanYa
	plt.subplot(324)
	pointClusNumSanYa = clusterAssmentSanYa[:,0].A.T
	n = np.shape(pointClusNumSanYa)[1]
	plt.title(u'三亚')
	for i in range(n):
		if 0.0 == pointClusNumSanYa.item(i):
			plt.plot(norMatSanYa[i,0],norMatSanYa[i,1],'g^')
		elif 1.0 == pointClusNumSanYa.item(i):
			plt.plot(norMatSanYa[i,0],norMatSanYa[i,1],'b*')
		elif 2.0 == pointClusNumSanYa.item(i):
			plt.plot(norMatSanYa[i,0],norMatSanYa[i,1],'k<')
		elif 3.0 == pointClusNumSanYa.item(i):
			plt.plot(norMatSanYa[i,0],norMatSanYa[i,1],'ms')

	plt.plot(centroidsSanYa[:,0],centroidsSanYa[:,1],'ro')
	plt.axis([0,4.0,0,12])
	plt.xticks([0,1,2,3])
	# plt.xlabel(u'Distance Index')
	# plt.ylabel(u'Activity Index')

	# JiuZhaigou
	plt.subplot(325)
	pointClusNumJiuZhaigou = clusterAssmentJiuZhaigou[:,0].A.T
	n = np.shape(pointClusNumJiuZhaigou)[1]
	plt.title(u'九寨沟')
	for i in range(n):
		if 0.0 == pointClusNumJiuZhaigou.item(i):
			plt.plot(norMatJiuZhaigou[i,0],norMatJiuZhaigou[i,1],'g^')
		elif 1.0 == pointClusNumJiuZhaigou.item(i):
			plt.plot(norMatJiuZhaigou[i,0],norMatJiuZhaigou[i,1],'b*')
		elif 2.0 == pointClusNumJiuZhaigou.item(i):
			plt.plot(norMatJiuZhaigou[i,0],norMatJiuZhaigou[i,1],'k<')
		elif 3.0 == pointClusNumJiuZhaigou.item(i):
			plt.plot(norMatJiuZhaigou[i,0],norMatJiuZhaigou[i,1],'ms')

	plt.plot(centroidsJiuZhaigou[:,0],centroidsJiuZhaigou[:,1],'ro')
	plt.axis([0,4.0,0,12])
	plt.xticks([0,1,2,3])
	plt.xlabel(u'Distance Index')
	plt.ylabel(u'Activity Index')

	# TaiShan
	plt.subplot(326)
	pointClusNumTaiShan = clusterAssmentTaiShan[:,0].A.T
	n = np.shape(pointClusNumTaiShan)[1]
	plt.title(u'泰山')
	for i in range(n):
		if 0.0 == pointClusNumTaiShan.item(i):
			plt.plot(norMatTaiShan[i,0],norMatTaiShan[i,1],'g^')
		elif 1.0 == pointClusNumTaiShan.item(i):
			plt.plot(norMatTaiShan[i,0],norMatTaiShan[i,1],'b*')
		elif 2.0 == pointClusNumTaiShan.item(i):
			plt.plot(norMatTaiShan[i,0],norMatTaiShan[i,1],'k<')
		elif 3.0 == pointClusNumTaiShan.item(i):
			plt.plot(norMatTaiShan[i,0],norMatTaiShan[i,1],'ms')

	plt.plot(centroidsTaiShan[:,0],centroidsTaiShan[:,1],'ro')
	plt.axis([0,4.0,0,12])
	plt.xticks([0,1,2,3])
	plt.xlabel(u'Distance Index')
	plt.ylabel(u'Activity Index')

	plt.show()



if __name__ == '__main__':
	# main()
	plotCluster()
	# generateRandomDots()
	# generateClusterDataset()