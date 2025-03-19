from math import *
class Solution:
	def solve(self, n):
		m = 2 * n
		cnt = 0
		for i in range(1, int(sqrt(m))+1):
			if m % i == 0:
				k1 = i
				if k1 >= 2:
					d1 = m // k1
					tmp1 = d1 - k1 + 1
					if tmp1 % 2 == 0 and tmp1 > 0:
						st1 = tmp1 // 2
						if st1 >= 1:
							cnt += 1
				k2 = m // i
				if k2 >= 2 and k2 > k1:
					d2 = m // k2
					tmp2 = d2 - k2 + 1
					if tmp2 % 2 == 0 and tmp2 > 0:
						st2 = tmp2 // 2
						if st2 >= 1:
							cnt += 1
		return cnt
		
Fishsauce = Solution()
for case in range(int(input())):
	ans = Fishsauce.solve(int(input()))
	print(ans)