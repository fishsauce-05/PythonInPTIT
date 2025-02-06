class Solution:
	def solve(self, strNum):
		for char in strNum:
			if char != '1' or char != '2' or char != '3':
				return 'NO'
		return 'YES'
		
Fishsauce = Solution()
for case in range(int(input())):
	strNum = input()
	ans = Fishsauce.solve(strNum)
	print(ans)