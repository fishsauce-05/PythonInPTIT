'''
Fishsauce
'''
from sys import stdin
def main():
    n = int(stdin.readline())
    sumN = n*(n+1) // 2
    cur = 0
    for _ in range(n-1):
        cur += int(stdin.readline())
    num = int(sumN - cur)
    print(f"{num}")

if __name__ == "__main__":
    main() 