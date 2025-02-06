class Solution:
	def solve(self, num):

		def Try(num, step):
			if step == 1000:
				return -1
			if num % 7 == 0:
				return num
			cur = num + int(str(num)[::-1])
			return Try(cur, step+1)

		res = Try(num, 0)
		return res
		
Fishsauce = Solution()
for case in range(int(input())):
	num = int(input())
	ans = Fishsauce.solve(num)
	print(ans)