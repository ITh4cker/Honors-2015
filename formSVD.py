import numpy as np

if __name__ == '__main__':
	filename = raw_input()
	f = open(filename)
	matrix = []
	for line in f:
		line = line.strip()[1:-1]
		line = line.split(',')
		m = []
		for j in line:
			m.append(str(j))
		matrix.append(m)
	U,s,V = np.linalg.svd(matrix)
	print U
	print
	print s
	print
	print V
