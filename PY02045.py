'''
Fishsauce
'''
s = input()
while len(s) > 1 :
    s = str(int(s[:int(len(s) / 2):]) + int(s[int(len(s) / 2)::]))
    print(s)