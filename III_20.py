from sys import stdin as inp

ln = int(input())
nums = list(map(int, inp.read().split('\n')))
nums.sort()
print('Silver =', nums[-2])