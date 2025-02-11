from collections import deque
import statistics as stat
class Solution:
    def solve(self, n, nums):
        nums.sort()
        cntL = nums.count(nums[0])
        cntR = nums.count(nums[-1])
        q = deque(nums)
        while cntR > 0:
            q.pop()
            cntR -= 1
        while cntL > 0:
            q.popleft()
            cntL -= 1
        return stat.mean(q)
        
Fishsauce = Solution()
n = int(input())
nums = list(map(float, input().split()))
ans = Fishsauce.solve(n, nums)
print("{:.2f}".format(ans))