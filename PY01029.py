import math
class Solution:
	def solve(self, num):
		def rev(n):
			tmp = 0
			while n:
				tmp += n%10
				tmp *= 10
				n //= 10
			return tmp
		return 'YES' if math.gcd(num, rev(num)) == 1 else 'NO'

Fishsauce = Solution()
for case in range(int(input())):
	num = int(input())
	print(Fishsauce.solve(num))