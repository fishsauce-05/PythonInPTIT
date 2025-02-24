'''
Fishsauce
'''
class ThiSinh:
	def __init__(self, name, date, mon1, mon2, mon3):
		self.name = name
		self.date = date
		self.tong = mon1 + mon2 + mon3
	@staticmethod
	def display(self):
		print("{} {} {:.1f}".format(self.name, self.date, self.tong))

if __name__ == "__main__":
	ts = ThiSinh(input(), input(), float(input()), float(input()), float(input()))
	ThiSinh.display(ts)