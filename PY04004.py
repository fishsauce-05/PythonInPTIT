'''
Fishsauce
'''
import math

class Fraction: 
	def __init__(self, tu, mau):
		self.tu = tu
		self.mau = mau
		self.usc =  math.gcd(tu, mau)
		self.rutgon()
	def rutgon(self):
		self.tu //= self.usc
		self.mau //= self.usc
		return self
	def __add__(self, other):
		tu = self.tu * other.mau + other.tu * self.mau
		mau = self.mau * other.mau
		return Fraction(tu, mau)
	def __str__(self):
		return f"{self.tu}/{self.mau}"

if __name__ == "__main__":
	arr = input().split()
	fractionP = Fraction(int(arr[0]), int(arr[1]))
	fractionQ = Fraction(int(arr[2]), int(arr[3]))
	fractionRes = fractionP + fractionQ
	print(fractionRes)