d = int(input())
v = int(input())
h = d / v
hr = int(h)
m = int((h - hr) * 60)
print("{:02}".format(hr), "{:02}".format(m), sep=":")
