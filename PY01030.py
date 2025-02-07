import math
class Solution:
	def solve(self, n, k):
		left = 10**(k-1)
		right = 10**k 
		nums = []
		for i in range(left, right):
			if math.gcd(n, i) == 1:
				nums.append(i)
		return nums

Fishsauce = Solution()
n, k = map(int, input().split())
lst = Fishsauce.solve(n, k)
cnt = 0
for ele in lst:
	print(ele, end = " ")
	cnt += 1
	if cnt % 10 == 0:
		print()