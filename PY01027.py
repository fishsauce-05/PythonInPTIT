class Solution:
	def solve(self, strN):
		for i in range(len(strN)):
			if strN[i] != '6' and strN[i] != '8':
				return 'NO'
			if strN[i] == '8':
				try:
					if strN[i:i+3] == '888':
						return 'NO'
				except:
					continue
		return 'YES'

Fishsauce = Solution()
ans = Fishsauce.solve(input())
print(ans)