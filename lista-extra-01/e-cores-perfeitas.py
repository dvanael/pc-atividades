a, b, c = map(int, input().split())
lista= [a, b, c]
lista.sort()
if lista[1] - lista[0 ] == lista[2] - lista[1]:
    print("S")
else:
    print("N")