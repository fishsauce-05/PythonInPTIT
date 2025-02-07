'''
Fishsauce
'''
for case in range(int(input())):
	print('YES' if sum(list(map(int, input()))) % 3 == 0 else 'NO')