'''
Fishsauce
'''
n = int(input())
nums = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
    for j in range(i-1, -1, -1):
        if nums[i] % nums[j] == 0:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))