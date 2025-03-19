a, b, m = map(int, input().split())
res = a**(b+1) - 1
res //= a-1
print(res % m)