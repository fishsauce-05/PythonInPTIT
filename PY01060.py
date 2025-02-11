class Solution:
	def solve(self, nums):
		even, odd = 1, 0
		n = len(nums)
		for i in range(n):
			if i & 1:
				odd += nums[i]
			else:
				if nums[i] != 0:
					even *= nums[i]
		return (even, odd)
		
Fishsauce = Solution()
for case in range(int(input())):
	ans = Fishsauce.solve(list(map(int, input())))
	print(ans[0], ans[1])