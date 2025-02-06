class Solution:
	def solve(self, n):
		cur = n%10
		n //= 10
		sumN = cur
		while n:
			tmp = n%10
			if abs(tmp-cur) != 2:
				return 'NO'
			cur = tmp
			sumN += cur
			n //= 10
		return 'YES' if sumN % 10 == 0 else 'NO'
		
Fishsauce = Solution()
for case in range(int(input())):
	num = int(input())
	print(Fishsauce.solve(num))