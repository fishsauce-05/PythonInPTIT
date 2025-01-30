class Solution:
	def solve(self, strNum):
		curN = strNum[0]
		for chrNum in strNum[1:]:
			if curN > chrNum:
				return 'NO'
			curN = chrNum
		return 'YES'

t = int(input())
Fishsauce = Solution()
for cases in range(t):
	strNum = input()
	print(Fishsauce.solve(strNum))