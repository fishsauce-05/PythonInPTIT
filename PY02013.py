class Solution:
	def __init__(self):
		self.step = 1
	def solve(self, num):
		if num == 1:
			return self.step
		self.step += 1
		if num & 1:
			return self.solve(num * 3 + 1)
		else:
			return self.solve(num >> 1)

while True:
	num = int(input())
	if num == 0:
		break
	Fishsauce = Solution()
	print(Fishsauce.solve(num))