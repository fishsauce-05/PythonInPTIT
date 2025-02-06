class Solution:
	def solve(self, nums):
		n = len(nums)
		if n == 2:
			return 'YES' if nums[n-1] == nums[n-2] else 'NO'
		for i in range(2, n, 2):
			if i + 2 >= n:
				return 'YES' if nums[i-1] == nums[i+1] else 'NO'
			if nums[i-1] != nums[i+1] or nums[i] != nums[i-2]:
				return 'NO'
		return 'YES'
		
Fishsauce = Solution()
for case in range(int(input())):
	nums = list(map(int, input()))
	ans = Fishsauce.solve(nums)
	print(ans)