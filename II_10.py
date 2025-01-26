m, v, t, d = input().split()
print(int(v)*int(t) % int(m) if d == 'A' else int(m) - (int(v)*int(t) % int(m)))