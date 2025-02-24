'''
Fishsauce
'''
import numpy as np
for case in range(int(input())):
	n, m = map(int, input())
	nums = []
	for _ in range(n):
		nums.append(list(map(int, input().split())))
	matrixA = np.array(nums)
	matrixB = np.transpose(matrixA)
	print(np.multiply(matrixA, matrixB))

