'''
Fishsauce
'''
lst = []
for case in range(int(input())-1):
    lst.append(int(input()))
a = min(lst)
b = max(lst)
mark = set(x for x in lst)
for i in range(a, b):
    if i not in mark:
        print(i)
        break