class Solution:
	def solve(self, num):
		return "YES" if num.count('4') + num.count('7') == len(num) else 'NO'

t = int(input())
for cases in range(t):
	num = input()
	Fishsauce = Solution()
	print(Fishsauce.solve(num))