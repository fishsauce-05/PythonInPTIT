for cases in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))   
    min_st = min_nd = min_rd = float('inf')
    for num in nums:
        if num < min_st:
            min_rd = min_nd
            min_nd = min_st
            min_st = num
        elif num < min_nd:
            min_rd = min_nd
            min_nd = num
        elif num < min_rd:
            min_rd = num
    print(min_st + min_nd + min_rd)