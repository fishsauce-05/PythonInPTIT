'''
Fishsauce
'''
n = int(input())
nums = list(map(int, input().split()))
cnt = 0
for i in range(n):
	try:
		if nums[i] != nums[i+1]:
			cnt += 1
	except:
		break
print(cnt)