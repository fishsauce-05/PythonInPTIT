from collections import Counter

cnt_chr = Counter(input())
print('YES' if cnt_chr['4'] + cnt_chr['7'] == 4 or cnt_chr['4']+cnt_chr['7'] == 7 else 'NO')