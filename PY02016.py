from collections import Counter
class Solution:
	def solve(self, n, counts):
		return counts.most_common(1)[0][0] if counts.most_common(1)[0][1] > n/2 else 'NO'
		
Fishsauce = Solution()
for case in range(int(input())):
	n = int(input())
	ans = Fishsauce.solve(n, Counter(list(map(int, input().split()))))
	print(ans)