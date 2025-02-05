import math
class Solution:
	def solve(self, n, x, m):
		x /= 100
		s = math.log(m/n, 1+x)
		if s != int(s):
			s += 1
		return int(s)

Fishsauce = Solution()
for case in range(int(input())):
	n, x, m = map(float, input().split())
	print(Fishsauce.solve(n, x, m))