import math
class Solution:
	def solve(self, strNum):
		def prime(n):
			for i in range(2, int(math.sqrt(n))+1):
				if n % i == 0:
					return False
			return n > 1
		return 'YES' if prime(int(strNum[-4:])) else 'NO'
		
Fishsauce = Solution()
for case in range(int(input())):
	strNum = input()
	ans = Fishsauce.solve(strNum)
	print(ans)