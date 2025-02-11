'''
Fishsauce
'''
for case in range(int(input())):
    n = int(input())
    nums = list(input().split())
    nums_sorted = sorted(nums, key=lambda x: (sum(map(int, x)), int(x)))
    print(" ".join(nums_sorted))