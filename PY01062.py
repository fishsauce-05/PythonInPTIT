class Solution:
	def __init__(self):
		self.prime = [True] * 626
		self.prime[0] = self.prime[1] = False
		for i in range(26):
			if self.prime[i]:
				for j in range(i*i, 626, i):
					self.prime[j] = False
	def solve(self, strNum):
		n = len(strNum)
		digit = 0
		for char in strNum:
			if self.prime[int(char)]:
				digit += 1
		return 'YES' if self.prime[n] and digit > n/2 else 'NO'

Fishsauce = Solution()
for case in range(int(input())):
	ans = Fishsauce.solve(input())
	print(ans)