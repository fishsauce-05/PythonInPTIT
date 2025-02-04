n = int(input())
nums = []

for _ in range(n - 1):
    nums.append(int(input().strip()))

sum_of_numbers = sum(nums)
expected_sum = n * (n + 1) // 2
missing_number = expected_sum - sum_of_numbers
print(missing_number)