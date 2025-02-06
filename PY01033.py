import math
class Solution:
	def solve(self, l, r):
		triplets = []
		for i in range(l, r-1):
			for j in range(i+1, r):
				for k in range(j+1, r+1):
					if math.gcd(i, j) == 1 and math.gcd(j, k) == 1 and math.gcd(i, k) == 1:
						triplets.append((i, j, k))
		return triplets

Fishsauce = Solution()
l, r = map(int, input().split())
results = Fishsauce.solve(l, r)
for res in results:
	print(res)
