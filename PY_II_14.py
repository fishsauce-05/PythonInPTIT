from datetime import datetime

h, m, s = map(int, input().split(' '))
angle_time = h*30 + m*0.5 + s*(0.5/60)
if angle_time > 180:
	angle_time = 360 - angle_time
print('Angle:', angle_time)