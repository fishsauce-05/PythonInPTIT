from collections import defaultdict as df

primeNums = df(lambda: True)
primeNums[0] = primeNums[1] = False
for i in range(1001):
	if primeNums[i]:
		for j in range(i*i, 100001, i):
			primeNums[j] = False
def rev(n):
	a = 0
	while n != 0:
		a = a*10 + n%10
		n //= 10
	return a

t = int(input())
for cases in range(t):
	num = int(input())
	for i in range(num+1):
		if primeNums[i] and primeNums[rev(i)] and rev(i) > i and rev(i) <= num:
			print(i, rev(i), end=" ")
	print()
