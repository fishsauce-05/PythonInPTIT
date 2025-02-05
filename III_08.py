from sys import stdin
class Solution:
    def solve(self, n, nums):
        sumN = int(n*(n+1)/2)
        return sumN - sum(nums)

Fishsauce = Solution()
n = int(input())
nums = list(map(int, stdin.read().split('\n')))
print(Fishsauce.solve(n, nums))