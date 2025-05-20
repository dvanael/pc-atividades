a, b, c = map(int, input().split())

if a == c or b == c or a == b:
    print("S")
elif a + b == c or b + c == a or a + c == b:
    print("S")
else:
    print("N")