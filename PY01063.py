class Solution:
	def solve(self, s, n):
		i = 0
		ln = len(n)
		cnt = 0
		while i < len(s):
			try:
				if s[i:i+ln] == n:
					cnt += 1
					i += ln
				else:
					i += 1
			except:
				break
		return cnt

Fishsauce = Solution()
for case in range(int(input())):
	xauS = input()
	strN = input()
	ans = Fishsauce.solve(xauS, strN)
	print(ans)