from numpy import *

def loadDataSet(fileName, delim='\t'):
	fr = open(fileName)
	stringArr = [line.strip().split(delim) for line in fr.readlines()]
	datArr = [map(float,line) for line in stringArr]
	return mat(dataArr)

def loadClusterCSV(fileName):
	#1 extract [noteNumber, dist, month]
	path = "D:\\python_develop\\cluster\\"+ fileName
	a = genfromtxt(path,delimiter=',')
	m = a[:,1:]
	# need to normalize dataset m by using averaging method.
	meanVals = mean(m,axis=0)
	normalizedDataset = m/meanVals

	# return matrix
	return matrix(normalizedDataset)

def pca(dataMat, topNfeat=999999):
	# 1 calculate the eigen values
	# If rowvar is non-zero (default), then each row represents a variable, with observations in the columns. 
	# Otherwise, the relationship is transposed: each column represents a variable, while the rows contain observations.
	covMat = cov(dataMat, rowvar=0)

	# calculate the eigenvalues and corresponding eigen vectors of covariance matrix
	eigVals, eigVects = linalg.eig(mat(covMat))

	# returns an array of indices of the same shape as a that index data along the given axis in sorted order. 
	# sort the eigen values which would be processed in step 2.
	eigValInd = argsort(eigVals)[::-1]
	chosenEigValsSum = eigVals[eigValInd[0]]+eigVals[eigValInd[1]]
	weight = eigVals/chosenEigValsSum
	result = weight*eigVects
	print result
	# return eigVects[eigValInd[0]]
	return result
	# 2 sort N values ascending
	# eigValInd = eigValInd[:-(topNfeat+1):-1]
	# redEigVects = eigVects[:,eigValInd]
if __name__ == '__main__':
	count_max = {}
	count_min = {}
	count_max_counter= {}
	count_min_counter = {}
	for i in range(1,69):
		fileStr = "%d.csv" % i
		m = loadClusterCSV(fileStr)
		eigVect = pca(m,1)
		weightInd = eigVect.A1.argsort()
		if weightInd[-1] not in count_max:
			count_max[weightInd[-1]] = 1
			count_max_counter[weightInd[-1]] = [i]
		else:
			count_max[weightInd[-1]]+=1
			count_max_counter[weightInd[-1]].append(i)

		if weightInd[0] not in count_min:
			count_min[weightInd[0]] = 1
			count_min_counter[weightInd[0]] = [i]
		else:
			count_min[weightInd[0]]+=1
			count_min_counter[weightInd[0]].append(i)
		
	print "count_max:"
	for k,v in count_max.iteritems():
		print "	%d : %d" %(k,v)
	print "count_max_counter"
	for k,v in count_max_counter.iteritems():
		print str(k)+":"+str(v)
	print "============================"
	print "count_min:"
	for k,v in count_min.iteritems():
		print "	%d : %d" % (k,v)
	print "count_min_counter"
	for k,v in count_min_counter.iteritems():
		print str(k)+":"+str(v)
	# m = loadClusterCSV("1.csv")
	# eigVect = pca(m,1)