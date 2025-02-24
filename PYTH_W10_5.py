'''
Fishsauce
'''
from sys import stdin

while True:
	n = int(stdin.readline())
	if n == -1:
		break
	print('YES' if n % 11 == 0 else 'NO')