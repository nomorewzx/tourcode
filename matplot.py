#-*- coding:utf8 -*-
import numpy as np
import matplotlib.pyplot as plt
import kMeans
import base
def main():
	dataSet = kMeans.loadfromcsv('./data/cluster/19.csv')
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

	longest_cluster = 0
	for i in range(0,len(clusters)):
		if longest_cluster < len(clusters[i]):
			longest_cluster = i
		print "%d cluster has %d elements " % (i, len(clusters[i])),
		print "the centroids is",
		print centroids[i]
	print "%d cluster mean type is" % longest_cluster,
	print centroids[longest_cluster]
	di = base.dunn(clusters)
	print di

def plotCluster():
	dataSetPingYao = kMeans.loadDataSet('7.csv')
	dataSetLaSa = kMeans.loadDataSet('15.csv')
	dataSetShangHai = kMeans.loadDataSet('8.csv')
	# dataSetBeiJing = kMeans.loadDataSet('20.csv')
	dataSetHaerBin = kMeans.loadDataSet('30.csv')

	dataMatPingYao = np.mat(dataSetPingYao)
	dataMatLaSa = np.mat(dataSetLaSa)
	dataMatShangHai = np.mat(dataSetShangHai)
	dataMatHaerBin = np.mat(dataSetHaerBin)


	norMatPingYao = kMeans.normalize(dataMatPingYao)
	norMatLaSa = kMeans.normalize(dataMatLaSa)
	norMatShangHai = kMeans.normalize(dataMatShangHai)
	norMatHaerBin = kMeans.normalize(dataMatHaerBin)

# haerbin
	plt.subplot(221)
	centroidsHaerBin, clusterAssmentHaerBin = kMeans.kMeans(norMatHaerBin,4)
	pointClusNumHaerBin = clusterAssmentHaerBin[:,0].A.T
	n = np.shape(pointClusNumHaerBin)[1]
	plt.title(u'哈尔滨游客聚类结果')
	for i in range(n):
		if 0.0 == pointClusNumHaerBin.item(i):
			plt.plot(norMatHaerBin[i,0],norMatHaerBin[i,1],'g^')
		elif 1.0 == pointClusNumHaerBin.item(i):
			plt.plot(norMatHaerBin[i,0],norMatHaerBin[i,1],'b*')
		elif 2.0 == pointClusNumHaerBin.item(i):
			plt.plot(norMatHaerBin[i,0],norMatHaerBin[i,1],'k<')
		elif 3.0 == pointClusNumHaerBin.item(i):
			plt.plot(norMatHaerBin[i,0],norMatHaerBin[i,1],'ms')

	plt.plot(centroidsHaerBin[:,0],centroidsHaerBin[:,1],'ro')
	plt.axis([0,4.0,0,12])
	plt.xticks([0,1,2,3])
	plt.xlabel(u'距离指标')
	plt.ylabel(u'活跃度指标')

# pingyao
	plt.subplot(222)
	centroidsPingYao, clusterAssmentPingYao = kMeans.kMeans(norMatPingYao,4)
	pointClusNumPingYao = clusterAssmentPingYao[:,0].A.T
	n = np.shape(pointClusNumPingYao)[1]
	plt.title(u'平遥游客聚类结果')
	for i in range(n):
		if 0.0 == pointClusNumPingYao.item(i):
			plt.plot(norMatPingYao[i,0],norMatPingYao[i,1],'g^')
		elif 1.0 == pointClusNumPingYao.item(i):
			plt.plot(norMatPingYao[i,0],norMatPingYao[i,1],'b*')
		elif 2.0 == pointClusNumPingYao.item(i):
			plt.plot(norMatPingYao[i,0],norMatPingYao[i,1],'k<')
		elif 3.0 == pointClusNumPingYao.item(i):
			plt.plot(norMatPingYao[i,0],norMatPingYao[i,1],'ms')

	plt.plot(centroidsPingYao[:,0],centroidsPingYao[:,1],'ro')
	plt.axis([0,4.0,0,12])
	plt.xticks([0,1,2,3])
	plt.xlabel(u'距离指标')
	plt.ylabel(u'活跃度指标')


# shanghai
	plt.subplot(223)
	centroidsShangHai, clusterAssmentShangHai = kMeans.kMeans(norMatShangHai,4)
	pointClusNumShangHai = clusterAssmentShangHai[:,0].A.T
	n = np.shape(pointClusNumShangHai)[1]
	plt.title(u'上海游客聚类结果')
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
	plt.xlabel(u'距离指标')
	plt.ylabel(u'活跃度指标')


# 
# lasa
	plt.subplot(224)
	centroidsLaSa, clusterAssmentLaSa = kMeans.kMeans(norMatLaSa,4)
	pointClusNumLaSa = clusterAssmentLaSa[:,0].A.T
	n = np.shape(pointClusNumLaSa)[1]
	plt.title(u'拉萨游客聚类结果')
	for i in range(n):
		if 0.0 == pointClusNumLaSa.item(i):
			plt.plot(norMatLaSa[i,0],norMatLaSa[i,1],'g^')
		elif 1.0 == pointClusNumLaSa.item(i):
			plt.plot(norMatLaSa[i,0],norMatLaSa[i,1],'b*')
		elif 2.0 == pointClusNumLaSa.item(i):
			plt.plot(norMatLaSa[i,0],norMatLaSa[i,1],'k<')
		elif 3.0 == pointClusNumLaSa.item(i):
			plt.plot(norMatLaSa[i,0],norMatLaSa[i,1],'ms')

	plt.plot(centroidsLaSa[:,0],centroidsLaSa[:,1],'ro')
	plt.axis([0,4.0,0,12])
	plt.xticks([0,1,2,3])
	plt.xlabel(u'距离指标')
	plt.ylabel(u'活跃度指标')

if __name__ == '__main__':
	main()