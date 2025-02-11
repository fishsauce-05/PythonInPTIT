class Solution:
	def solve(self, n, lstA, lstB):
		for i in range(n):
			if lstA[i] > lstB[i]:
				return 'NO'
		return 'YES'
		
Fishsauce = Solution()
for case in range(int(input())):
	ans = Fishsauce.solve(int(input()), sorted(list(map(int, input().split()))), sorted(list(map(int, input().split()))))
	print(ans)