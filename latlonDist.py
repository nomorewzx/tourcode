import math

R = 6371

def _deg2rad(degree):
	return degree* math.pi/180

def _dist(point1, point2):

	lat1 = _deg2rad(point1[0])
	lon1 = _deg2rad(point1[1])
	lat2 = _deg2rad(point2[0])
	lon2 = _deg2rad(point2[1])

	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = math.sin(dlat/2)*math.sin(dlat/2) + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)*math.sin(dlon/2)
	c = 2 * math.atan2( math.sqrt(a), math.sqrt(1-a) )
	d = R * c
	d = round(d*1000)/1000
	return d

def calBearing(point1, point2):
	lat1 = _deg2rad(point1[0])
	lon1 = _deg2rad(point1[1])
	lat2 = _deg2rad(point2[0])
	lon2 = _deg2rad(point2[1])
	dlon = lon2 - lon1
	
	y = math.sin(dlon)*math.cos(lat2)
	x = math.cos(lat1)*math.sin(lat2) - math.sin(lat1)*math.cos(lat2)*math.cos(dlon)
	bearing = math.atan2(y,x)
	return bearing


def test_dist():
	point1 = (39.929986, 116.395645)
	point2 = (39.143930, 117.210813)
	print _dist(point2,point1)

def test_bearing():
	point1 = (39.143930,118.456453)
	point2 = (38.143930,118.456453)
	print "the bearing between p1 and p2 is " ,calBearing(point1, point2)
if __name__ == '__main__':

	test_dist()
