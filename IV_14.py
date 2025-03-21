'''
Fishsauce
'''
s = input().split()
s.sort(key = lambda x: -len(x))
print(s[0], len(s[0]))