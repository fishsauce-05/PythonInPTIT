from collections import deque
import bisect

class Solution:
	def __init__(self):
		self.hamming = [1]
		mark = set()
		for num in self.hamming:
			for val in (num*2, num*3, num*5):
				if val > 10**18:
					break
				if val not in mark:
					self.hamming.append(val)
					mark.add(val)
		self.hamming.sort()

	def display(self):
		for it in self.hamming:
			print(it)
			if (it >= 90):
				break

	def solve(self, n):
		global it
		it = bisect.bisect_right(self.hamming, n)
		return self.hamming[it-1] == n

Fishsauce = Solution()
Fishsauce.display()
for case in range(int(input())):
	ans = Fishsauce.solve(int(input()))
	if ans:
		print(it)
	else:
		print("Not in sequence")
