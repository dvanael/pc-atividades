l = int(input())
c = int(input())

if (l == c) or ((l - c) % 2 == 0) or (l % 2 == 1 and c % 2 == 1):
    print(1)
else:
    print(0)
