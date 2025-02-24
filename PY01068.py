class Solution:
	def solve(self, n, k, lst):
		res = []
		def fi(i, cnt, nums):
			if cnt == k:
				res.append(nums[:])
				return
			for j in range(i, n):
				try:
					nums.append(lst[j])
				except:
					return
				fi(j+1, cnt+1, nums)
				nums.pop()
		fi(0, 0, [])
		return res

Fishsauce = Solution()
n, k = map(int, input().split())
ans = Fishsauce.solve(n, k, sorted(list(set(input().split()))))
for row in ans:
	for num in row:
		print(num, end = " ")
	print()