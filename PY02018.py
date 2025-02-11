from collections import defaultdict

class Solution:
	def solve(self, nums):
		cur = nums[0]
		for num in nums[1:]:
			if num - cur != 1:
				return cur + 1
			cur = num
		return nums[-1] + 1
		
Fishsauce = Solution()
n = int(input())
ans = Fishsauce.solve(sorted(list(map(int, input().split()))))
print(ans)