import math
class Solution:
	def solve(self, num):
		for i in range(2, int(math.sqrt(num)) + 1):
			if num % i == 0:
				return 'NO'
		return 'YES'
		
Fishsauce = Solution()
for case in range(int(input())):
	num = sum(list(map(int, input())))
	ans = Fishsauce.solve(num)
	print(ans)