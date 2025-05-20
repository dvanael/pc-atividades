a = int(input())
b = int(input())
c = int(input())
d = int(input())

s1 = abs((a+b) - (c+d))
s2 = abs((a+c) - (b+d))
s3 = abs((a+d) - (b+c))

print(min(s1, s2, s3))