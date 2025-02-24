class Solution:
	def solve(self, n, nums):
		stack = [(nums[0], 1)]
		for i in range(1, n):
			top, cnt = stack[-1]
			if nums[i] < top:
				stack.append((nums[i], 1))
		return 0


		
Fishsauce = Solution()
ans = Fishsauce.solve()
print(ans)