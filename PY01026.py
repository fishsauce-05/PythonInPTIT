class Solution:
	def solve(self, s1, s2):
		n = len(s1)
		for i in range(n):
			if s1[i] != s2[i]:
				return 'NO'
		return 'YES' if len(s1) == len(s2) else 'NO'
		
Fishsauce = Solution()
for case in range(int(input())):
	ans = Fishsauce.solve(sorted(input()), sorted(input()))
	print('Test', str(case+1)+':', ans)