'''
Fishsauce
'''
n = int(input())
nums = list(map(int, input().split()))
nums.sort(key = lambda x: (x&1))
r, l = 0, n-1
print(nums)
while True:
	if nums[r]&1 and not nums[l]&1:
		break
	if nums[l] & 1 and l > 0:
		print(nums[l], end = " ")
		l -= 1
	if not nums[r] &1 and r < n:
		print(nums[r], end = " ")
		r += 1
