class Solution:
	def __init__(self):
		self.res = 1
	def solve(self, num):
		if num == 0:
			return self.res
		digit = num % 10
		self.res = self.res * digit if digit != 0 else self.res
		return self.solve(num//10)
		
for case in range(int(input())):
	Fishsauce = Solution()
	num = int(input())	
	ans = Fishsauce.solve(num)
	print(ans)