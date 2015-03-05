import sys
def readPoints(filePath):
	'''reads in list of points from file with format x1, y2\\nx2, y2 ...'''
	points = []
	with open(filePath, 'r') as f:
		for line in f:
			parts = line.split(',')
			#TODO: make sure entries are actual numbers
			if len(parts) != 2:
				print "bad line (only two values per line): " + line
				continue
			try:
				px = float(parts[0])
				py = float(parts[1])
			except ValueError:
				print "bad line (entries must be numbers): " + line
			else:
				points.append((px,py))
	return points
def getLValues(points, degree):
	assert(degree > 0)
	values = []
	for n in range(0, degree + 1):
		lsum = 0.0
		for x, y in points:
			lsum = lsum + (x**n) * y
		values.append(lsum)
	return values
def getSumsOfPowersOfXCords(points, degree):
	values = []
	for i in range(0, degree * degree + 1):
		rsum = 0.0
		for x, y in points:
			rsum = rsum + x**i
		values.append(rsum)
	return values
def getRValues(points, degree):
	powers = getSumsOfPowersOfXCords(points, degree)
	values = []
	for i in range(0, degree + 1):
		row = []
		for j in range(0, degree + 1):
			row.append(powers[i + j])
		values.append(row)
	return values
def usage():
	print "python2 polyReg.py data.csv <degree>"
	print "where data.csv list x,y pairs and degree is a natural number"
if __name__ == '__main__':
	if len(sys.argv) != 3:
		usage()
		exit(2)
	if not sys.argv[2].isdigit():
		print "error: second parameter should be a positive integer"
		exit(1)
	degree = int(sys.argv[2])
	pts = readPoints(sys.argv[1])
	print getLValues(pts, degree)
	print getRValues(pts, degree)
	
