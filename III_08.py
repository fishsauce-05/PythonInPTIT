from sys import stdin
class Solution:
    def solve(self, n, nums):
        sumN = int(n*(n+1)/2)
        return sumN - sum(nums)

Fishsauce = Solution()
n = int(stdin.readline().strip())
nums = []
for _ in range(n-1):
    nums.append(int(stdin.readline().strip()))
print(Fishsauce.solve(n, nums))