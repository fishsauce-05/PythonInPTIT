t = int(input())
for cases in range(t):
	num_str = input()
	if num_str[0] == num_str[-1]:
		print("YES")
	else:
		print("NO")