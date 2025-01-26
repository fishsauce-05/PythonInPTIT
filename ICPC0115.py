factorial = [fac for fac in range(21)]
factorial[0] = 1
for i in range(1, 21):
	factorial[i] *= factorial[i-1]
t = int(input())
for cases in range(t):
	num = numSt = int(input())
	numCheck = 0
	while num != 0:
		numCheck += factorial[num%10]
		num //= 10
	if numCheck == numSt:
		print("Yes")
	else:
		print("No")
