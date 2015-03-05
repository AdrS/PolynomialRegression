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

if __name__ == '__main__':
	pass
