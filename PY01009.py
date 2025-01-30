class Solution:
	def check(self, strXau):
		lower = 0
		upper = 0
		for chrX in strXau:
			if chrX.isupper():
				upper += 1
			elif chrX.islower():
				lower += 1
		return upper > lower
	def solve(self, strXau):
		return strXau.upper() if self.check(strXau) else strXau.lower()

strXau = input()
Fishsauce = Solution()
print(Fishsauce.solve(strXau))