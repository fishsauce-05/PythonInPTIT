class Solution:
	def solve(self, num):
		return "CHAN" if num % 2 == 0 else "LE"

num = int(input())
fishsauce = Solution()
print(fishsauce.solve(num))