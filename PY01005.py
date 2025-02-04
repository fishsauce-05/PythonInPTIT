from collections import Counter

num = int(input())
cnt_chr = Counter(str(num))
print('YES' if cnt_chr['4'] + cnt_chr['7'] == 4 or cnt_chr['4']+cnt_chr['7'] == 7 else 'NO')