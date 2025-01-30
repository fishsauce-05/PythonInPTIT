class Solution:
	def solve(self, strN):
		return "YES" if strN[0:2] == strN[-2:] else "NO"

t = int(input())
for cases in range(t):
	strN = input()
	Fishsauce = Solution()
	print(Fishsauce.solve(strN))