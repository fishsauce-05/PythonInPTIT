import string
class Solution:
	def __init__(self):
		self.xau = '0123456789' + string.ascii_uppercase
		self.base = {i: char for i, char in enumerate(self.xau)}
	def solve(self, n, b):
		res = ''
		while n:
			res += self.base[n%b]
			n //= b
		return res[::-1]

Fishsauce = Solution()
for case in range(int(input())):
	n, b = map(int, input().split())
	ans = Fishsauce.solve(n, b)
	print(ans)
