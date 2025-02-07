class Solution:
	def solve(self, nums):
		n = len(nums)
		for i in range(0, n, 2):
			if i + 2 >= n:
				break
			if nums[i] != nums[i+2]:
				return 'NO'
		return 'YES' if n%2 == 1 and nums[0] != nums[1] else 'NO'
		
Fishsauce = Solution()
for case in range(int(input())):
	nums = list(map(int, input()))
	ans = Fishsauce.solve(nums)
	print(ans)