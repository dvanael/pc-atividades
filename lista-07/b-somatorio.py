a = int(input())
s = 0

for i in range(1, a + 1):
    s += 1 / i

print("{:.4f}".format(s))
