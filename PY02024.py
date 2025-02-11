'''
Fishsauce
'''
def product(n):
	if n == 0:
		return 0
	return n if n < 10 else (n%10) * product(n // 10)

for case in range(int(input())):
	n = int(input())
	nums = list(map(int, input().split()))
	nums.sort(key = lambda x: (product(x), x))
	for num in nums:
		print(num, end = ' ')
	print()