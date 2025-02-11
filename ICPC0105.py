'''
Fishsauce
'''
import re
for case in range(int(input())):
	print(max(list(map(int, re.findall(r'\d+', input())))))