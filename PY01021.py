class Solution:
	def solve(self, strX):
		strX.sort(key = lambda x: -x.isalpha())
		pos = next((i for i, char in enumerate(strX) if char.isdigit()), -1)
		return ''.join(sorted(strX[:pos])) + str((sum(map(int, strX[pos:]))))
		
Fishsauce = Solution()
for case in range(int(input())):
	ans = Fishsauce.solve(list(input()))
	print(ans)