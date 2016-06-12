#-*- encoding:utf8 -*-
import numpy as np
import math
import latlonDist
import json
import csv
from datetime import date
import operator

from collections import defaultdict
from sklearn.neighbors import NearestNeighbors


def genMatrix():
	a = np.genfromtxt("notegeodata.csv",delimiter=',')
	m = np.matrix(a[:,-2:])
	return a[:,-2:]

def getDistance(p, q):
	assert type(p) is np.ndarray, 'p is not matrix!'
	assert type(q) is np.ndarray, 'q is not matrix!'
	pointA = (p[1], p[0])
	pointB = (q[1], q[0])
	return latlonDist._dist(pointA,pointB)

#获取到p点的所有bandwidth距离内的点的索引，存储于index_neighbors列表，并返回列表
def getNeighbors(p, X,bandwidth):
	index_neighbors = []
	index = 0
	for q in X:
		if getDistance(p,q)<=bandwidth:
			index_neighbors.append(index)
		index+=1
	return index_neighbors

def meanshift(X,bandwidth):
	stop_thresh = 1e-3*bandwidth
	n_points, m_features = X.shape
	labels = [0]*n_points #存放点的所属聚类
	center_intensity_dict = {}

	for my_mean in X:
		while True:
			index_nbrs = getNeighbors(my_mean, X, bandwidth)
			# 取出 my_mean 在 bandwidth 距离内的点，放入points_within
			points_within = X[np.asarray(index_nbrs)]
			# 如果 与 my_mean 距离 bandwidth 的点不存在，则跳出while迭代，选取下一点
			if(len(points_within)==0):
				break
			#存储当前 my_mean，并计算新的my_mean
			my_old_mean = my_mean
			my_mean = np.mean(points_within,axis=0)
			# 如果均值偏移向量收敛，则将簇所包含的元素数目增加
			if getDistance(my_mean,my_old_mean) <stop_thresh:
				# tuple(my_mean)将一个array对象转换为元组类型
				# 如果tuple(my_mean)点已经存在于dict中，则旧长度加新长度
				# 否则就将dict[tuple(my_mean)]设置为初始点的邻居数目
				# 表明以该收敛点为中心的收敛点数目
				if tuple(my_mean) in center_intensity_dict:
					old = center_intensity_dict[tuple(my_mean)]
					center_intensity_dict[tuple(my_mean)] = len(points_within)+old
				else:
					center_intensity_dict[tuple(my_mean)] = len(points_within)
				break

	if not center_intensity_dict:
		raise ValueError("No point was within bandwidth=%f of any seed."
                         " Try a different seeding strategy or increase the bandwidth."
                         % bandwidth)

	# 后续处理：移除相近的核，如果两个核的距离小于bandwidth，则移除数目较小的那个核
	# 处理采用以下步骤：
	# 1. center_intensity_dict字典按照value值降序排序；即按照簇中包含点数目排序
	# 2. 取出排序后的center_intensity_dict的key值，转换为 ndarray，sorted_center
	# 3. 依次对sorted_center中的点，计算其bandwidth距离内的其它点，如果存在，则用当前
	# 	核心点替换掉其它邻近点
	sorted_by_intensity = sorted(center_intensity_dict.items(),
								key = lambda tup: tup[1],reverse=True)
	sorted_centers = np.array([tup[0] for tup in sorted_by_intensity])
	unique = np.ones(len(sorted_centers),dtype=np.bool)
	for i, center in enumerate(sorted_centers):
		if unique[i] == True:
			index_nbrs = getNeighbors(center, sorted_centers, bandwidth)
			unique[index_nbrs] = 0
			# 当前点为保留的中心点，移除其它bandwidth距离内的点
			unique[i] = 1
	cluster_centers = sorted_centers[unique]

	# 找出所有的聚类中心点，接下来将X中的每个点分配到其所属的簇，
	# 分配原则为，找到距离当前点最近的中心点，若距离小于bandwidth，
	# 则该点不属于任何簇；否则该点的簇编号，为中心点在cluster_centers
	# 中的索引值

	idx = []
	labels = np.zeros(n_points,dtype=np.int)
	labels.fill(-1)
	# 首先取出最小距离的索引
	for i,point in enumerate(X):
		minDist = bandwidth*2
		cluster_label = -1
		for j, center in enumerate(cluster_centers):
			if getDistance(point, center) < minDist:
				minDist = getDistance(point, center)
				cluster_label = j
		if minDist<=bandwidth:
			labels[i] = cluster_label

	return cluster_centers,labels

def defineClusterName(classifications):
    reader = csv.reader(open("./data/notegeodata.csv"))
    dictCount = {}
    i = 0
    for item in reader:
        label = classifications[i]
        # check if label or city in dictCount.
        #if label in dictCount, but city not in dictCount[label],then add city.
        if label  not in dictCount:
            dictCount[label]={item[5]:1}
        elif item[5] not in dictCount[label]:
            dictCount[label][item[5]]=1
        else:
            dictCount[label][item[5]]+=1
        i+=1
    print "has %d labels in" % i
    print 'has %d points has been assigned' % len(dictCount)
    classificationsName = classifications
    dictCount_new ={}
    for key,value in dictCount.iteritems():
       sorted_city = sorted(value.items(), key = operator.itemgetter(1),reverse=True)
       dictCount_new[key]=sorted_city[0][0]
    for i in range(0,len(classifications)):
        label = classifications[i]
        classificationsName[i] = dictCount_new[label]
    fopen = open('./data/clusterName-meanshift.txt','w')
    for k,v in dictCount_new.iteritems():
        fopen.write(str(k)+','+str(v)+'\n')
    fopen.close()
    # return  dictCount_new, classificationsName

def runWithParam(n):
	m = genMatrix()
	cluster_centers,labels = meanshift(m,n)
	name = 'meanshift-%d.txt' % n
	f = open(name,'w')
	label_list = []
	for i in range(0,len(labels)):
		label_list.append(labels[i])
	for label in label_list:
		f.write(str(label))
		f.write('\n')
	f.close()

def clusterName(bandwidth,labels):
	cluster_number = len(list(set(labels)))
	file_name = "./data/%d-number-%d-name.txt" % (bandwidth,cluster_number)
	reader = csv.reader(open('./data/notegeodata.csv'))
	dictCount = {}
	i = 0
	for item in reader:
		label = labels[i]
		# check if label or city in dictCount.
		#if label in dictCount, but city not in dictCount[label],then add city.
		if label not in dictCount:
			dictCount[label]={item[5]:1}
		elif item[5] not in dictCount[label]:
			dictCount[label][item[5]]=1
		else:
			dictCount[label][item[5]]+=1
		i+=1
	dictCount_new ={}
	for key,value in dictCount.iteritems():
		sorted_city = sorted(value.items(), key = operator.itemgetter(1),reverse=True)
		dictCount_new[key]=sorted_city[0][0]
	print 'has %d cluster has defined names' % len(dictCount_new)

	f = open(file_name,'w')
	for k,v in dictCount_new.iteritems():
		f.write(str(k)+','+v+'\n')
	f.close()

def genLabelsFromtxt(file_name,bandwidth):
	f = open(file_name,'r')
	lines = f.readlines()
	labels = []
	for line in lines:
		labels.append(int(line))
	clusterName(bandwidth,labels)


def runMulti():
	runWithParam(150)
	runWithParam(50)

# 比较DBSCAN聚类结果中与MeanShift聚类结果中有多少是相同的个数
# 注意MeanShift文件需要在代码中更改
def compareTwo(bandwidth,cluster_number):
	mean_shift_path = "./dat/%d-number-%d-name.txt" % (bandwidth,cluster_number)
	f_dbscan = open('./data/clusterName-dbscan.txt','r')
	f_meanshift = open(mean_shift_path,'r')
	db_names = genClusterName(f_dbscan)
	mf_names = genClusterName(f_meanshift)
	same_names = []
	for name in db_names:
		if name in mf_names:
			same_names.append(name)

	print 'DBSCAN and meanshift with %d bandwidth has %d same names' % (bandwidth,len(same_names))
	f = open('./data/same_names-150.txt','w')
	for name in same_names:
		f.write(name+'\n')
	f.close()

def genClusterName(file1):
	cluster_names = []
	lines = file1.readlines()
	for line in lines:
		label,name = line.split(',')
		cluster_names.append(name)
	return cluster_names
if __name__ == '__main__':
	m = genMatrix()
	print 'runing...'
	cluster_centers,labels = meanshift(m,150)
	print "共有簇数目为：%d" % len(cluster_centers)


	f = open('./data/labels.txt','a')
	for label in labels:
		f.writeln(label)
	f.close()

	print "共有噪音点数目为: %d" % (len(labels)-count)
	print "所有簇中包含点数目为: %d" % count