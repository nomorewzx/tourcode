#-*- encoding:utf8 -*-
import numpy as np
import math
import latlonDist
import json
import csv
from datetime import date
import operator

UNCLASSIFIED = False
NOISE = None

def _dist(p,q):
    assert type(p) is np.matrix, 'p is not matrix!'
    assert type(q) is np.matrix, 'q is not matrix!'
    spot1 = (p.item(0,1), p.item(0,0))
    spot2 = (q.item(0,1), q.item(0,0))
    return latlonDist._dist(spot1,spot2)
    #return math.sqrt(np.power(p-q,2).sum())

def _eps_neighborhood(p,q,eps):
    return _dist(p,q) < eps

def _region_query(m, point_id, eps):
    n_points = m.shape[0]
    seeds = []
    for i in range(0,n_points):
        if not i == point_id:
            if _eps_neighborhood(m[i,:], m[point_id,:], eps):
            	seeds.append(i)
    return seeds

def _expand_cluster(m, classifications, point_id, cluster_id, eps, min_points):
	seeds = _region_query(m,point_id,eps)
	if len(seeds) < min_points:
		classifications[point_id] = NOISE
		return False
	else:
	    classifications[point_id] = cluster_id
	    for seed_id in seeds:
	    	classifications[seed_id] = cluster_id
	    while len(seeds)>0:
	    	current_point = seeds[0]
	    	results = _region_query(m, current_point, eps)
	    	if len(results) >= min_points:
	    	    for i in range(0, len(results)):
	    	    	result_point = results[i]
	    	    	if classifications[result_point] == UNCLASSIFIED or classifications[result_point] == NOISE:
	    	    		if classifications[result_point] == UNCLASSIFIED:
	    	    		    seeds.append(result_point)
	    	        classifications[result_point] = cluster_id

	    	seeds = seeds[1:]
	    return True

def dbscan(m, min_points, eps):
    cluster_id = 1
    n_points = m.shape[0]
    classifications = [UNCLASSIFIED] * n_points
    for point_id in range(0, n_points):
        point = m[point_id,:]
        if classifications[point_id] == UNCLASSIFIED:
        	if _expand_cluster(m, classifications, point_id, cluster_id, eps, min_points):
        		cluster_id +=1
    return classifications

def _runDbscan(m,eps,min_points):
    #assert dbscan(m, eps, min_points) == [1, 1, 1, 2, 2, 2, None]
    classifications = dbscan(m, min_points, eps)
    fopen = open("./data/result.txt",'w')
    for i in classifications:
        fopen.write(str(i))
        fopen.write('\n')
    fopen.close()
    return classifications

def _genMatrixFromtxt():
    a = np.genfromtxt('./data/notegeodata.csv',delimiter=',')
    m = np.matrix(a[:,-2:])
    return m

def _dumpToJson(matrix, classifications):
    jsonList = []
    for i in range (0,len(classifications)):
        if classifications[i] != None:
           dic =  dict(zip(['label','lng','lat'], [str(classifications[i]), matrix[i,:].item(0,0), matrix[i,:].item(0,1)]))
           jsonList.append(dic)
    fopen = open('./data/jsonResult.json','w')
    json.dump(jsonList,fopen)
    fopen.close()
def _defineClusterName(classifications, csvFile):
    reader = csv.reader(open("./data/notegeodata.csv"))
    dictCount = {}
    i = 0
    for item in reader:
        label = classifications[i]
        # check if label or city in dict.
        #if label in dict, but city not in dict[label],then add city.
        if label  not in dictCount:
            dictCount[label]={item[5]:1}
        elif item[5] not in dictCount[label]:
            dictCount[label][item[5]]=1
        else:
            dictCount[label][item[5]]+=1
        i+=1
    classificationsName = classifications
    dictCount_new ={}
    for key,value in dictCount.iteritems():
        # see https://wiki.python.org/moin/HowTo/Sorting for more details about operator.itemgetter() func
       sorted_city = sorted(value.items(), key = operator.itemgetter(1))
       dictCount_new[key]=sorted_city[-1][0]
    for i in range(0,len(classifications)):
        label = classifications[i]
        classificationsName[i] = dictCount_new[label]
    fopen = open('./data/clusterName.txt','w')
    for k,v in dictCount_new.iteritems():
        fopen.write(str(k)+','+v+'\n')
    fopen.close()
    return  dictCount_new, classificationsName