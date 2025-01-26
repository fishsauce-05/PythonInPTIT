t = int(input())
for cases in range(t):
    n = int(input())
    nums = [int(num) for num in input().split()]    
    max_st = max_nd = max_rd = float("inf")
    for num in nums:
        if num > max_st:
            max_rd = max_nd
            max_nd = max_st
            max_st = num
        elif num > max_nd:
            max_rd = max_nd
            max_nd = num
        elif num > max_rd:
            max_rd = num
    print(max_st + max_nd + max_rd)