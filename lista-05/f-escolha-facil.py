c1, b1, p1 = map(int, input().split())
c2, b2, p2 = map(int, input().split())

c = b = p = 0

if c2 > c1:
    c = c2 - c1

if b2 > b1:
    b = b2 - b1

if p2 > p1:
    p = p2 - p1

print(int(c+b+p))