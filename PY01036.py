class Solution:
	def __init__(self):
		self.S = [1, 1/2]
		for i in range(3, 10**4-1):
			self.S.append(1/i + self.S[i-3])
	def solve(self, n):
		return self.S[n-1]
		
Fishsauce = Solution()
for case in range(int(input())):
	num = int(input())
	number = Fishsauce.solve(num)
	print(f"{number:.6f}")