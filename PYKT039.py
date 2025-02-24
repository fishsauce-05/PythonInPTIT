class Solution:
	def solve(self, n, lstA, lstB):
		for i in range(n):
			if lstA[i] > lstB[i]:
				return 'NO'
		return 'YES'

Fishsauce = Solution()
for case in range(int(input())):
	n = int(input())
	lstA = sorted(list(map(int, input().split())))
	lstB = sorted(list(map(int, input().split())))
	ans = Fishsauce.solve(n, lstA, lstB)
	print(ans)