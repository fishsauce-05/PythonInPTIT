'''
Fishsauce
'''
from sys import stdin
while True:
    n = int(input())
    if n == 0:
        break
    raw = []
    for _ in range(n):
        raw.append(int(stdin.readline()))
    nums = sorted(list(set(raw)))
    print('BANG NHAU' if len(nums) == 1 else f"{nums[0]} {nums[-1]}")