t = int(input())
for cases in range(t):
	p, q = map(int, input().split())
	x1 = input()
	x2 = input()
	p, q = max(p, q), min(p, q)
	print(int(x1.replace(str(p), str(q))) + int(x2.replace(str(p), str(q))), end = " ")
	print(int(x1.replace(str(q), str(p))) + int(x2.replace(str(q), str(p))))