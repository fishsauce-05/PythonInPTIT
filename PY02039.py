'''
Fishsauce
'''
from sys import stdin
n = int(input())
nums = []
sumN = 0
for _ in range(n):
	nums.append(list(map(int, stdin.readline().split())))
	sumN += sum(nums[_])
k = int(input())

main = dig = col = 0
for i in range(n):
	for j in range(col+1, n):
		main += nums[i][j]
	dig += nums[i][i]
	col += 1

aux = sumN - main - dig
print('YES' if abs(main - aux) <= k else 'NO')
print(abs(main-aux))