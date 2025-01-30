class Fishsauce:
	def solve(self, num: str) -> str:
		nums = list(map(int, num))
		n = len(nums)
		if len(nums) == 1:
			return nums[0]
		for i in range(n-1, 0, -1):
			if nums[i] >= 5:
				nums[i-1] += 1
		return str(nums[0]) + '0' * (n-1)
t = int(input())
for cases in range(t):
	num = input()
	solution = Fishsauce()
	print(solution.solve(num))