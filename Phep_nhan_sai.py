class Solution:
	def solve(self, y, z):
		return z // (sum(map(int, list(str(y)))))

Fishsauce = Solution()
while True:
	s = input()
	if s == "-1":
		break
	else:
		y, z = map(int, s.split())
		ans = Fishsauce.solve(y, z)
		print(ans)