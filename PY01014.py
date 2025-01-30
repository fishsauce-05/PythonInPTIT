class Solution:
	def solve(self, a, k, n):
		if k > n or a >= n:
			return [-1]
		lstB = []
		sumAB = a + k - a%k
		sign = 2
		while sumAB <= n:
			lstB.append(sumAB-a)
			sumAB = a + k*sign - a%k
			sign += 1
		return lstB if lstB else [-1]
		
Fishsauce = Solution()
a, k, n = map(int, input().split(' '))
print(' '.join(map(str, Fishsauce.solve(a, k, n))))