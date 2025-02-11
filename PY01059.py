class Solution:
    def solve(self, nums):
        n = len(nums)
        even, odd = 0, 1
        flagZero = False
        for i in range(n):
            if i % 2 == 0:
                even += nums[i]
            else:
                if nums[i] != 0:
                    odd *= nums[i]
                    flagZero = True
        if not flagZero:
            odd = 0
        return [even, odd]

Fishsauce = Solution()
for case in range(int(input())):
    ans = Fishsauce.solve(list(map(int, input())))
    print(ans[0], ans[1])