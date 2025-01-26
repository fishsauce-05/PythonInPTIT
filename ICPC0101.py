n = int(input())
nums = [int(x) for x in input().split()]

for i in range(n):
	nums[i] %= 2
stack = []

for i in range(n):
    if not stack: 
        stack.append(nums[i])
        continue
    top = stack[-1]
    if nums[i] != top:
        stack.append(nums[i])
    else:
        while stack and nums[i] == stack[-1]:
            stack.pop()

print(len(stack))