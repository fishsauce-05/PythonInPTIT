class Solution:
	def solve(self, num):
		cnt = 0
		strNum = ''
		while num:
			strNum += str(num%10)
			cnt += 1
			if cnt == 3 and num > 9:
				cnt = 0
				strNum += ','
			num //= 10
		return strNum[::-1]
		
Fishsauce = Solution()
num = int(input())
print(Fishsauce.solve(num))