from sys import stdin as inp

ln = int(input())
nums = list(map(int, inp.read().split('\n')))
nums.sort()
print('Silver =', eval(str(nums[-2])))