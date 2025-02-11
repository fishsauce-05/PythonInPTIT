from collections import defaultdict, Counter 
class Solution:
	def __init__(self):
		self.prime = defaultdict(lambda: True)
		self.prime[0] = self.prime[1] = False
		for i in range(1001):
			if self.prime[i]:
				for j in range(i*i, 100001, i):
					self.prime[j] = False
	def solve(self, n, nums):
		mark = set()
		counts = Counter(nums)
		lst = []
		for num in nums:
			if self.prime[num] and num not in mark:
				mark.add(num)
				lst.append([num, counts[num]])
		return lst

Fishsauce = Solution()
n = int(input())
ans = Fishsauce.solve(n, list(map(int, input().split())))
for res in ans:
	print(res[0], res[1])