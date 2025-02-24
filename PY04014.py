'''
Fishsauce
'''
class SinhVien:
	def __init__(self, cnt, name, diemthi): #toan van nhan he so 2
		if cnt < 10:
			self.id = "HS0" + str(cnt)
		else:
			self.id = "HS" + str(cnt)
		self.name = name
		diemthi[0] *= 2
		diemthi[1] *= 2
		self.diem = sum(diemthi) / len(diemthi)
		diem = self.diem
		match diem:
			case _ if diem >= 9.0:
				self.rank = 'XUAT SAC'
			case _ if 8.0 <= diem < 9:
				self.rank = 'GIOI'
			case _ if 7.0 <= diem < 8:
				self.rank = 'KHA'
			case _ if 5.0 <= diem < 7:
				self.rank = 'TB'
			case _ if diem < 5:
				self.rank = 'YEU' 
	@staticmethod
	def display(self):
		return '{} {} {:.1f} {}'.format(self.id, self.name, self.diem, self.rank)

lst = []
for i in range(1, int(input()) + 1):
	sv = SinhVien(i, input(), list(map(float, input().split())))
	lst.append(sv)
lst.sort(key = lambda x: x.diem, reverse=True)
for l in lst:
	print(SinhVien.display(l))