'''
Fishsauce
'''
from sys import stdin
from collections import OrderedDict
from datetime import datetime

provinces = OrderedDict()
cnt = 1

#Dong Anh: (id, mua, tram)
for _ in range(int(input())):
    pos = stdin.readline().strip()
    st = stdin.readline().strip()
    en = stdin.readline().strip()
    rain = int(stdin.readline().strip())

    time_st = datetime.strptime(st, "%H:%M")
    time_en = datetime.strptime(en, "%H:%M")
    time_diff = time_en - time_st
    hour = time_diff.total_seconds() / 3600

    if pos not in provinces:
        id = "T0" + str(cnt)
        provinces[pos] = (id, [rain / hour])
        cnt += 1
    else:
        provinces[pos][1].append(rain / hour)

ans = sorted(provinces.items(), key=lambda x: -sum(x[1][1])/len(x[1][1]))
for key, value in ans:
	print(f"{value[0]} {key} {sum(value[1])/len(value[1]):.2f}")