class Solution:
	def __init__(self):
		self.fibo = [0, 1, 1]
		for i in range(3, 100):
			self.fibo.append(self.fibo[i-1] + self.fibo[i-2])
	def solve(self, a, b):
		return self.fibo[a:b+1]
		
Fishsauce = Solution()
for case in range(int(input())):
	left, right = map(int, input().split())
	ans = Fishsauce.solve(left, right)
	for res in ans:
		print(res, end = " ")
	print()