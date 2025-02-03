class Solution:
    def solve(self, n, nums):
        def binary_search(left, k):
            l = left
            r = n - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == k:
                    return 1
                elif nums[mid] < k:
                    l = mid + 1
                else:
                    r = mid - 1
            return 0

        res = 0
        nums.sort()
        for i in range(n - 1):
            for j in range(i + 1, n):
                num3 = 0 - (nums[i] + nums[j])
                res += binary_search(j + 1, num3)
        return res

Fishsauce = Solution()
for cases in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    print(Fishsauce.solve(n, nums))