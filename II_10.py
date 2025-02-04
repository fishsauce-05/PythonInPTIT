class Solution:
	def solve(self, m, v, t, d):
		if d == 'A':
			return (v*t)%m
		else:
			return m - ((v*t) % m)

Fishsauce = Solution()
m, v, t, d = (lambda x: (int(x[0]), int(x[1]), int(x[2]), x[3]))(input().split())
print(Fishsauce.solve(m, v, t, d))