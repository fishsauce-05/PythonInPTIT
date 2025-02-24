import math
import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def distance(p1, p2):
        x = p1.x - p2.x
        y = p1.y - p2.y
        return math.sqrt(x**2 + y**2)

    @staticmethod
    def check(p1, p2, p3):
        return not (p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y) == 0)

class Triangle:
    def __init__(self, a, b, c):
        self.ab = Point.distance(a, b)
        self.bc = Point.distance(b, c)
        self.ac = Point.distance(a, c)
        self.flag = Point.check(a, b, c)

    def perimeter(self):
        if self.ab + self.bc <= self.ac or self.ab + self.ac <= self.bc or self.bc + self.ac <= self.ab or not self.flag:
            return "INVALID"
        return '{:.3f}'.format(self.ab + self.bc + self.ac)

input_data = sys.stdin.read().split()
cnt = 0
n = len(input_data)
tri = []
results = []
for i in range(1, n):
    tri.append(int(input_data[i]))
    cnt += 1
    if cnt == 6:
        p1 = Point(int(tri[0]), int(tri[1]))
        p2 = Point(int(tri[2]), int(tri[3]))
        p3 = Point(int(tri[4]), int(tri[5]))
        tamgiac = Triangle(p1, p2, p3)
        results.append(str(tamgiac.perimeter()))
        cnt = 0
        tri.clear()
for res in results:
	print(res)