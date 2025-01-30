import math
class Solution:
	def solve(self, n, x, m):
		return math.ceil(math.log(m/n)) / math.log(1+x/100)

t = int(input())
for cases in range(t):
	n, x, m = map(float, input().split(' '))
	Fishsauce = Solution()
	print(Fishsauce.solve(n, x, m))