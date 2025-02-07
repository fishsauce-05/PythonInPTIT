import math
class Solution:
	def solve(self, nums):
		flagOdd = False
		sumN = 0
		for num in nums:
			if num % 2 != 0 and not flagOdd:
				return 'NO'
			if num % 2 == 0 and flagOdd:
				return 'NO'
			sumN += num
			if num % 2 == 0:
				flagOdd = True
			else:
				flagOdd = False
		for i in range(2, int(math.sqrt(sumN))+1):
			if sumN % i == 0:
				return 'NO'
		return 'YES'
		
Fishsauce = Solution()
for case in range(int(input())):
	nums = list(map(int, input()))
	ans = Fishsauce.solve(nums)
	print(ans)