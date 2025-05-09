b = int(input())
t = int(input())

base = 160
altura = 70
area_nota = base * altura

lista1 = [b, t]
l1 = max(lista1) - min(lista1)

area_corte1 = (altura * min(lista1)) + ((l1 * altura) / 2)

b2 = base - b
t2 = base - t
lista2 = [b2, t2]
l2 = max(lista2) - min(lista2)

area_corte2 = (altura * min(lista2)) + ((l2 * altura) / 2)

if area_corte1 > area_nota / 2:
    print(1)
elif area_corte2 > area_nota / 2:
    print(2)
else:
    print(0)
