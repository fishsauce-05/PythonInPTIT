class Solution:
	def check(self, strN):
		digits = ['0', '2', '4', '6', '8']:
		for chrN in strN:
			if chrN not in digits:
				return False
		return len(strN) % 2 == 1 
	def solve(self):
		print("Tao chep code")
t = int(input())
for cases in range(t):
	strN = input()
	Fishsauce = Solution()
	print(' '.Fishsauce.solve(strN))