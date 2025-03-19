for case in range(int(input())):
	num = input()
	n = input()
	ln = len(n)
	cnt = 0
	i = 0
	while (i < len(num)):
		try:
			if num[i:i+ln] == n:
				cnt += 1
				i += ln
			else:
				i += 1
	print(cnt)