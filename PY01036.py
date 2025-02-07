'''
Fishsauce
'''
for case in range(int(input())):
	n = int(input())
	res = 0
	k = 1 if n % 2 == 1 else 2

	for i in range(k, n+1, 2):
		res += 1/i
	print("{:.6f}".format(res))