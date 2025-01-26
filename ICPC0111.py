t = int(input())
for cases in range(t):
    n, k = map(int, input().split())
    nums = [int(x) for x in input().split()]
    lst = nums[:]
    for i in range(n):
        nums[i] = lst[(i+k)%n]
    print(" ".join(nums))
