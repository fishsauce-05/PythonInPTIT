zodiac = {
	(("Bach Duong"), (21, 3), (19, 4)),
	(("Kim Nguu"), (20, 4), (20, 5)),
	(("Song Tu"), (21, 5), (20, 6)),
	(("Cu Giai"), (21, 6), (22, 7)),
	(("Su Tu"), (23, 7), (22, 8)),
	(("Xu Nu"), (23, 8), (22, 9)),
	(("Thien Binh"), (23, 9), (22, 10)),
	(("Thien Yet"), (23, 10), (22, 11)),
	(("Nhan Ma"), (23, 11), (21, 12)),
	(("Ma Ket"), (22, 12), (19, 1)),
	(("Bao Binh"), (20, 1), (18, 2)),
	(("Song Ngu"), (19, 2), (20, 3))
}
t = int(input())
for cases in range(t):
	d, m = map(int, input().split(' '))
	flag = False
	for sign, time_st, time_en in zodiac:
		if (d >= time_st[0] and m == time_st[1]) or (d <= time_en[0] and m == time_en[1]):
			print(sign)
			flag = True
			break
	if not flag:
		print()
