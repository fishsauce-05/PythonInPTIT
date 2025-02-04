class Solution:
    def solve(self, n, nums):
        nums.sort()
        res = 0
        for i in range(n):
            if nums[i] > 0:
                break
            j = i + 1
            k = n - 1
            target = 0 - nums[i]
            while (j < k):
                if nums[j] + nums[k] < target:
                    j += 1
                else:
                    if nums[j] + nums[k] > target:
                        k -= 1
                    else:
                        res += 1
                        j += 1
        return res
        
Fishsauce = Solution()
for cases in range(int(input())):
    n = int(input())
    nums = sorted(list(map(int, input().split())))
    print(Fishsauce.solve(n, nums))