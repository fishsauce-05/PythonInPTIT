n = int(input())
nums = list(map(int, input().split()))
stack = []

for i in range(n):
    nums[i] %= 2
    if not stack: 
        stack.append(nums[i])
        continue
    if nums[i] != stack[-1]:
        stack.append(nums[i])
    else:
        while stack and nums[i] == stack[-1]:
            stack.pop()

print(len(stack))