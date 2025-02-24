from collections import deque
class Solution:
	def __init__(self):
		self.lst = []
		q = deque([('1', 0), ('2', 1)])
		while True:
			cur, cnt = q.popleft()
			if cnt > len(cur) >> 1:
				self.lst.append(int(cur))
			if len(self.lst) == 1000:
				break
			q.append((cur+'0', cnt))
			q.append((cur+'1', cnt))
			q.append((cur+'2', cnt+1))
	def solve(self):
		return sorted(self.lst)

Fishsauce = Solution()
nums = Fishsauce.solve()
for case in range(int(input())):
	n = int(input())
	for ac in nums[:n]:
		print(ac, end = " ")
	print()