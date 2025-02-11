'''
Fishsauce
'''
import re
for case in range(int(input())):
	print(min(list(map(int, re.findall(r'\d+', input())))))