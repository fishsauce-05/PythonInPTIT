class Solution:
	def solve(self, strNum):
		return "YES" if len(strNum) >= 2 and strNum[-2:] == '86' else 'NO'

t = int(input())
for cases in range(t):
    strNum = input()
    Fishsauce = Solution()
    print(Fishsauce.solve(strNum))