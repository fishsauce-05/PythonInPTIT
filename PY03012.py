'''
Fishsauce
'''
from sys import stdin

students = []
for _ in range(int(input())):
	name = [xau.capitalize() for xau in list(map(str.lower, stdin.readline().split()))]
	ac, sub = map(int, stdin.readline().split())
	tup = (name, ac, sub)
	students.append(tup)

students.sort(key = lambda x: (-x[1], x[2], x[0][2]))
for ac in students:
	print(' '.join(ac[0]), ac[1], ac[2])