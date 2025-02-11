class Solution:
	def solve(self, n, lst):
		lst.sort(key = lambda x: x[1])
		flagOdd = flagEven = flag = False
		cnt = 0
		for num in lst:
			if num[0] & 1 and not flagOdd:
				flagOdd = True
				cnt += num[1]
			elif not num[0] & 1 and not flagEven:
				flagEven = True
				cnt += num[1]
			if flagOdd and flagEven:
				flag = True
				break
		return cnt if flag else -1

Fishsauce = Solution()
for case in range(int(input())):
	ans = Fishsauce.solve(int(input()), list(zip(list(map(int, input().split())), list(map(int, input().split())))))
	print(ans)