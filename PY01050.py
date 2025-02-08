from collections import deque
class Solution:
	def __init__(self):
		self.orgin = "ABC"
		self.lst = []
	def solve(self, n):

		def check(strXau):
			cntA = cntB = cntC = 0
			for xau in strXau:
				if xau == 'A':
					cntA += 1
				elif xau == 'B':
					cntB += 1
				else:
					cntC += 1
			return cntA and cntB and cntC and cntA <= cntB <= cntC

		q = deque([x for x in self.orgin])
		while q:
			cur = q.popleft()
			if len(cur) == n:
				break
			for c in self.orgin:
				curXau = cur + c
				q.append(curXau)
				if check(curXau):
					self.lst.append(curXau)
		return self.lst						

		
Fishsauce = Solution()
ans = Fishsauce.solve(int(input()))
for res in ans:
	print(res)