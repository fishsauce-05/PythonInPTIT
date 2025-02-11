from collections import defaultdict as df
class Solution:
	def __init__(self):
		self.prime = df(lambda: True)
		self.prime[0] = self.prime[1] = False
		for i in range(1001):
			if self.prime[i]:
				for j in range(i*i, 100001, i):
					self.prime[j] = False
	def solve(self, strNum):
		return 'YES' if self.prime[int(strNum[:3])] and self.prime[int(strNum[-3:])] else 'NO'
		
Fishsauce = Solution()
for case in range(int(input())):
	ans = Fishsauce.solve(input())
	print(ans)