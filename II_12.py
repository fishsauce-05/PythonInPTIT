from datetime import datetime as dt, timedelta

st_time = input()
en_time = input()
fmt = "%H %M %S"

st_d = dt.strptime(st_time, fmt)
en_d = dt.strptime(en_time, fmt)
diff = en_d - st_d
if en_d < st_d:
	diff += timedelta(days=1)
print(int(diff.total_seconds()))