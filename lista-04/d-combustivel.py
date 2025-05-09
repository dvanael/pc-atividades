c = int(input())
d = int(input())
t = int(input())
g = d / c - t
if 0 >= g:
    print(0.0)
else:
    print("{:.1f}".format(g))
