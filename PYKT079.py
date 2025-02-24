class Solution:
	def solve(self, n, nums):
		cnt = 0
		for i in range(n):
			try: 
				if nums[i+1] - nums[i] > 1:
					cnt += nums[i+1] - nums[i] - 1
			except:
				break
		return cnt
		
Fishsauce = Solution()
for case in range(int(input())):
	n = int(input())
	nums = sorted(list(map(int, input().split())))
	ans = Fishsauce.solve(n, nums)
	print(ans)