class Solution:
	def __init__(self):
		self.prime = [True] * 626
		self.prime[0] = self.prime[1] = False
		for i in range(2, 26):
			if self.prime[i]:
				for j in range(i*i, 626, i):
					self.prime[j] = False
					
	def solve(self, nums):
		n = len(nums)
		for i in range(n):
			if self.prime[i]:
				if not self.prime[nums[i]]:
					return 'NO'
			else:
				if self.prime[nums[i]]:
					return 'NO'
		return 'YES'
		
Fishsauce = Solution()
for case in range(int(input())):
	nums = list(map(int, input()))
	ans = Fishsauce.solve(nums)
	print(ans)