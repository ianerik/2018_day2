#test for maxima.py

def test

	import numpy as np 

	cd /Users/IanErik/Documents/Python/2018_day2

	from maxima import *

	testcases1 = [[0, 1, 2, 1, 2, 1, 0], [-i**2 for i in range(-3, 4)],
              [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]]

	testcases2 = [[[4, 2, 1, 3, 1, 2], [4, 2, 1, 3, 1, 5], 
				[4, 2, 1, 3, 1]]

	testcases3 = [[1, 2, 2, 1]]

	testcases4 = [[1, 2, 2, 3, 1],
				[1, 3, 2, 2, 1],
				[3, 2, 2, 3]]
	
	for case in testcases1
		x = findmaxima(case)	
		print(x)

	for case in testcases2
		y = findmaxima(case)	
		print(y)

	for case in testcases3
		z = findmaxima(case)	
		print(z)

	for case in testcases4
		a = findmaxima(case)	
		print(a)