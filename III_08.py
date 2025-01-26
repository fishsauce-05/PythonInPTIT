from sys import stdin as inp
ln = int(input())
nums = [int(num) for num in inp.read().split('\n')[:ln-1]]
for i in range(ln):
	if i+1 not in nums:
		print(i+1)
		break
