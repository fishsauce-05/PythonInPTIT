class Solution:
	def __init__(self):
		self.step = 0
	def solve(self, nums):
		if nums[0] == nums[1] == nums[2] == nums[3]:
			return self.step
		self.step += 1
		newNums = [abs(nums[i] - nums[(i+1)%4]) for i in range(4)]
		return self.solve(newNums)

while True:
	nums = list(map(int, input().split()))
	if nums == [0, 0, 0, 0]:
		break
	Fishsauce = Solution()
	print(Fishsauce.solve(nums))