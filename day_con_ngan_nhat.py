from math import gcd

class Solution:
    def solve(self, n, k, nums):
        res = 1005
        for i in range(n):
            cur = nums[i]
            if cur == k:
                return 1
            if cur < k: 
                continue
            for j in range(i + 1, n):
                cur = gcd(cur, nums[j])
                if cur == k:
                    res = min(res, j - i + 1)
                    break
                if cur < k:
                    break
        return res if res != 1005 else -1

Fishsauce = Solution()
for cases in range(int(input())):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    ans = Fishsauce.solve(n, k, nums)
    print(ans)