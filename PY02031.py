'''
Fishsauce
'''
import math
def Prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1 if n > 1 else 0

r, c = map(int, input().split())
nums = []
for _ in range(r):
    nums.append(list(map(int, input().split())))

for i in range(r):
    for j in range(c):
        print(Prime(nums[i][j]), end=' ')
    print()