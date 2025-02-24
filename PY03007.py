"""
Fishsauce
"""
from sys import stdin

strings = list(map(str.lower, stdin.read().split()))
strings[0] = strings[0].capitalize()
flag = False
for i in range(len(strings)):
	xau = strings[i] + " "
	if flag:
		flag = False
		strings[i] = strings[i].capitalize()
		xau = strings[i] + " "
	if strings[i][-1] == "." or strings[i][-1] == "!" or strings[i][-1] == "?":
		flag = True
		xau = strings[i][:-1] + "\n" if i != len(strings) - 1 else strings[i][:-1]
	print(xau, end = "")