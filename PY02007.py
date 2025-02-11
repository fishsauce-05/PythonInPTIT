'''
Fishsauce
'''
from sys import stdin
print(len(set(map(lambda x: x % 42, list(map(int, stdin.read().split()))))))