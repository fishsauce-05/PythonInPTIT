from sys import stdin as inp
class Solution:
	def solve(self, n, nums):
		nums.sort(reverse = True)
		return eval(str(nums[1]))

Fishsauce = Solution()
n = int(inp.readline().strip())
nums = []
for _ in range(n):
	nums.append(int(inp.readline().strip()))
print('Silver =', Fishsauce.solve(n, nums))