'''
Fishsauce
'''
from sys import stdin as inp
ln = int(input())
print(len(set(list(inp.read().split('\n')[:ln]))))