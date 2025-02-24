from sys import stdin

class Solution:
	def __init__(self):
		self.res = 0
	def solve(self, n, m, mat, kernel):
		def multi(r, c):
			if r > n - 3:
				return
			if c > m - 3:
				multi(r + 1, 0)
				return
			total = 0
			for i in range(3):
				for j in range(3):
					total += mat[r + i][c + j] * kernel[i][j]
			self.res += total
			multi(r, c + 1)
		multi(0, 0)
		return self.res

for case in range(int(input())):
	Fishsauce = Solution()
	n, m = map(int, input().split())
	mat = []
	for _ in range(n):
		mat.append(list(map(int, stdin.readline().split())))
	kernel = []
	for _ in range(3):
		kernel.append(list(map(int, stdin.readline().split())))

	ans = Fishsauce.solve(n, m, mat, kernel)
	print(ans)