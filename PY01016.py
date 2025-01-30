class Solution:
	def solve(self, code):
		freq = 0
		i = 0
		n = len(code)
		chrC = 'a'
		codeFi = str()

		while i < n:
			if i < n:
				while i<n and code[i].isdigit():
					freq = freq*10 + int(code[i])
					i += 1
				codeFi += chrC * freq
			else:
				freq = 0
				codeFi = code[i]
				i += 1
		return codeFi

Fishsauce = Solution()
t = int(input())
for cases in range(t):
	code = input()
	print(Fishsauce.solve(code))