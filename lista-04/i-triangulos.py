a, b, c = map(int, input().split())
lista = [a, b, c]
if (a + b > c) and (a + c > b) and (b + c > a):
    x = max(lista)
    z = min(lista)
    y = sum(lista) - x - z
    if y**2 + z**2 == x**2:
        print("r")
    elif y**2 + z**2 < x**2:
        print("o")
    else:
        print("a")
else:
    print("n")
