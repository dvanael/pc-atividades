l, d = map(int, input().split())
k, p = map(int, input().split())
v = l // d
t = k * l + p * v
print(int(t))
