n1, n2, n3, n4, n5, n6, n7, n8 = map(int, input().split())

lista = [n1, n2, n3, n4, n5, n6, n7, n8]

for i in lista:
    if i != 0 and i != 1:
        print("F")
        break
else:
    print("S")