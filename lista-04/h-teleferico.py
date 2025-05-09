c = int(input())
a = int(input())

v = a / (c - 1)
if v % 1 == 0:
    print(int(v))
else:
    print(int(v) + 1)
