from collections import defaultdict as df
import math

primeNums = df(lambda: True)
primeNums[0] = primeNums[1] = False
for i in range(1001):
	if primeNums[i]:
		for j in range(i*i, 100001, i):
			primeNums[j] = False

t = int(input())
for cases in range(t):
	n = int(input())
	k = 0
	for i in range(1, n):
		if math.gcd(i, n) == 1:
			k += 1
	print('YES' if primeNums[k] else 'NO')