'''
Fishsauce
'''
n = int(input())
nums = list(map(int, input().split()))
cnt = 0

for i in range(n):
	for j in range(i+1, n):
		try: 
			if nums[i] > nums[j]:
				cnt += 1
		except:
			break
print(cnt)