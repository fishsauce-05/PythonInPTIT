from collections import defaultdict as df

prime_numbers = df(lambda: True)
prime_numbers[0] = prime_numbers[1] = False
for prime in range(1001):
	if prime_numbers[prime]:
		for sq_prime in range(prime*prime, 1000001, prime):
			prime_numbers[sq_prime] = False

t = int(input())
for cases in range(t):
	num = int(input())
	cnt = 0
	for i in range(5, num-5):
		if prime_numbers[i] and prime_numbers[i+2] and prime_numbers[i+6] or prime_numbers[i] and prime_numbers[i+4] and prime_numbers[i+6]:
			cnt += 1
	print(cnt)