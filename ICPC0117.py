from sys import stdin as inp
ln = int(input())
lst_str = inp.read().split('\n')[:ln]
set_str = set(lst_str)
print(len(set_str))