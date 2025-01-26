import re
t = int(input())
for i in range(t):
	str_x = input()
	sub_num = re.findall(r'\d+', str_x)
	print(min([int(num) for num in sub_num]))