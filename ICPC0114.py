from collections import defaultdict as df

primeNums = df(lambda: True)
primeNums[0] = primeNums[1] = False
for i in range(1001):
	if primeNums[i]:
		for j in range(i*i, 100001, i):
			primeNums[j] = False
def sumOfN(n):
	s = 0
	while n != 0:
		s += n%10
		n //= 10
	return s
def rev(n):
	r = 0
	while n != 0:
		r = n%10
		n //= 10
	return r
def check(n):
	if not (primeNums[n] and primeNums[rev(n)] and primeNums[sumOfN(n)]):
		return False
	while n != 0:
		if not primeNums[n%10]:
			return False
		n //= 10
	return True

t = int(input())
for cases in range(t):
	num = int(input())
	if check(num):
		print("Yes")
	else:
		print("No")
