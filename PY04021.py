'''
Fishsauce
'''
from sys import stdin
from datetime import datetime

gamers = []

for _ in range(int(input())):
    code = stdin.readline().strip()
    name = stdin.readline().strip()
    st = stdin.readline().strip()
    en = stdin.readline().strip()
    
    time_st = datetime.strptime(st, "%H:%M")
    time_en = datetime.strptime(en, "%H:%M")
    time_diff = time_en - time_st
    hours, remainder = divmod(time_diff.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    tup = (code, name, hours, minutes)
    gamers.append(tup)

gamers.sort(key = lambda x: (-x[2], -x[3]))
for ac in gamers:
	print(f"{ac[0]} {''.join(ac[1])} {ac[2]} gio {ac[3]} phut")