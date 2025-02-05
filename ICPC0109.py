MAX = 100000

def Print3Smallest(arr, n):
    firstmin = MAX
    secmin = MAX
    thirdmin = MAX

    for i in range(0, n):
        if arr[i] < firstmin:
            thirdmin = secmin
            secmin = firstmin
            firstmin = arr[i]
        elif arr[i] < secmin:
            thirdmin = secmin
            secmin = arr[i]
        elif arr[i] < thirdmin:
            thirdmin = arr[i]
    print(firstmin+ secmin + thirdmin)

for case in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    Print3Smallest(arr, n)
