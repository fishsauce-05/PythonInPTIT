'''
Fishsauce
'''

n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c, d = {}, {}
for i in a : c[i] = 1
for i in b : d[i] = 1
print('YES' if c == d else 'NO')