'''
Fishsauce
'''
for case in range(int(input())):
	strNum = input()
	sumN = sum(map(int, strNum))
	print('YES' if str(sumN) == str(sumN)[::-1] and sumN > 9 else 'NO')