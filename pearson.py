import numpy as np
import csv
def loadDataSet():
	dataSet = np.genfromtxt("./data/distTraffic.csv",delimiter=",")
	return dataSet
def pearson(dataSet):
	# covMat is the covariance matrix, elements are cov(a,a) cov(a,b) cov(b,a) and cov(b,b)
	# covMat[0,1] is the covariance expected.
	covMat = np.cov(dataSet,rowvar=0)
	covariance = covMat[0,1]
	stdDevs = np.std(dataSet,axis=0)
	pearson_correlation = covariance/(stdDevs[0]*stdDevs[1])
	return pearson_correlation

	

if __name__ == '__main__':
	dataSet = loadDataSet()
	print pearson(dataSet)
