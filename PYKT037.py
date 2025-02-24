import string
class Solution:
	def __init__(self):
		xau = '0123456789' + string.ascii_uppercase
		self.base = {i: char for i, char in enumerate(xau)}
	def solve(self, n, b):
		res = str()
		while n:
			bas = n % b
			res += self.base[bas]
			n //= b
		return res[::-1]
		
Fishsauce = Solution()
for case in range(int(input())):
	n, b = map(int, input().split())
	ans = Fishsauce.solve(n, b)
	print(ans)