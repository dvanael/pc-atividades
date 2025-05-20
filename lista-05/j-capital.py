a, b, c, d = map(int, input().split())

if (a*d == b*c) or (a*b == c*d) or (a*c == b*d):
    print("S")
else:
    print("N")