class Solution:
	def __init__(self):
		self.primes = [True] * 626
		self.primes[0] = self.primes[1] = False
		for i in range(2, 26):
			if self.primes[i]:
				for j in range(i*i, 626, i):
					self.primes[j] = False
	def solve(self, num):
		cntPrime = 0 
		cntNon = 0
		while num:
			digit = num % 10
			if self.primes[digit]:
				cntPrime += 1
			else:
				cntNon += 1
			num //= 10
		return 'YES' if self.primes[cntPrime + cntNon] and cntPrime > cntNon else 'NO'

Fishsauce = Solution()
for case in range(int(input())):
	ans = Fishsauce.solve(int(input()))
	print(ans)