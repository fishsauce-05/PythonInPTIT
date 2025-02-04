def solve():
    n = int(input())
    nums = sorted(list(map(int, input().split())))
    print(sum(nums) if n == 1 or n == 2 else sum(nums[0:3]))

for case in range(int(input())):
    solve()