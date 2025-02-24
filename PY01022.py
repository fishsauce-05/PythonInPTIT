class Solution:
	def __init__(self):
		self.cnt = 0
	def solve(self, strN):
		if len(strN) == 1:
			return self.cnt
		num = 0
		for char in strN:
			num += ord(char) - 48
		self.cnt += 1
		return self.solve(str(num))

		
Fishsauce = Solution()
ans = Fishsauce.solve(input())
print(ans)