'''
Fishsauce
'''
import math
n = int(input())
nums = sorted(list(map(int, input().split())))
for i in range(n-1):
	for j in range(i+1, n):
		if math.gcd(nums[i], nums[j]) == 1:
			print(nums[i], nums[j])