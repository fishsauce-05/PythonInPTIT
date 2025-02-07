class Solution:
	def solve(self, strNum):
		n = len(strNum)
		for i in range(2, n):
			if strNum[i] != strNum[i-2]:
				return False
		return True
		
Fishsauce = Solution()
for case in range(int(input())):
	strNum = input()
	ans = Fishsauce.solve(strNum)
	if ans == True:
		print('YES')
	else:
		print('NO')