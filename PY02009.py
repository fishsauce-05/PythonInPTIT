from collections import Counter
from sys import stdin

class Solution:
	def solve(self, counts):
		maxFreq = max(counts.values())
		return min([key for key, value in counts.items() if value == maxFreq])
		
Fishsauce = Solution()
for case in range(int(input())):
	n = int(input())
	nums = []
	for i in range(n):
		nums.append(int(stdin.readline().strip()))
	ans = Fishsauce.solve(Counter(nums))
	print(ans)