class Solution:
	def solve(self, nums):
		down = False
		cur = nums[0]
		n = len(nums)
		if n < 3:
			return 'NO'
		for num in nums[1:]:
			if num == cur:
				return 'NO'
			if num > cur and down:
				return 'NO'
			if num < cur:
				down = True
			cur = num
		return 'YES' if down else 'NO'
		
Fishsauce = Solution()
for case in range(int(input())):
	nums = list(map(int, input()))
	ans = Fishsauce.solve(nums)
	print(ans)