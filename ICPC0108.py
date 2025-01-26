import bisect
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    numbers = set()
    n = len(nums)
    nums.sort()
    for i in range(n-2):
        for j in range(i+1, n-1):
            ij = nums[i] + nums[j]
            lower_bound = bisect.bisect_left(nums, -1 * ij, j+1)
            if lower_bound < n and nums[lower_bound] == -1 * ij:
                numbers.add((nums[i], nums[j], nums[lower_bound]))
    return len([list(triplet) for triplet in numbers])

t = int(input())
for cases in range(t):
    ln = int(input())
    nums = [int(x) for x in input().split()]
    print(threeSum(nums))