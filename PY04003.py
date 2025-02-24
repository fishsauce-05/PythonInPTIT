'''
Fishsauce
'''
import math
class Fraction:
	def __init__(self, tu, mau):
		self.tu = tu
		self.mau = mau
		self.usc = math.gcd(tu, mau)
	def rutgon(self):
		return '{}/{}'.format(self.tu//self.usc, self.mau//self.usc)

if __name__ == "__main__":
	arr = input().split()
	fraction = Fraction(int(arr[0]), int(arr[1]))
	print(fraction.rutgon())