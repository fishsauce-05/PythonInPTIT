import math
from collections import defaultdict as df
class Solution:
	def __init__(self):
		self.primes = df(lambda: True)
		self.primes[0] = self.primes[1] = False
		for i in range(1001):
			if self.primes[i]:
				for j in range(i*i, 100001, i):
					self.primes[j] = False
	def sum(self, n):
		sumN = 0
		while n:
			sumN += n%10
			n //= 10
		return sumN
	def solve(self, a, b):
		return 'YES' if self.primes[self.sum(math.gcd(a, b))] else 'NO'

Fishsauce = Solution()
t = int(input())
for cases in range(t):
	a, b = map(int, input().split(' '))
	print(Fishsauce.solve(a, b))