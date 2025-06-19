# Prova 02 - Listas e funções recursivas
print("Prova 02 - Listas e funções recursivas\n")


def alt_list(lista):
    x = lista[0] + lista[3]
    lista.append(x)
    lista.append(x + lista[1])
    lista[0] = lista[3] + lista[4]
    return lista


a1 = alt_list([5, 9, 2, 2])
a2 = alt_list([5, 5, 1, 9])
a3 = alt_list([7, 5, 1, 6, 7])

print("1.")
print("5 9 2 2   ->", *a1)
print("5 5 1 9   ->", *a2)
print("7 5 1 6 7 ->", *a3)
print("")


def alt_list2(lista, x):
    lista.append(x)
    lista.append(1)
    t = len(lista)
    lista.append(t)
    return lista[1], lista[t - 2], lista[t]


print("2.")
print(f"9 2    x = 9  -> {alt_list2([9, 2], 9)}")
print(f"7 5    x = 9  -> {alt_list2([7, 5], 9)}")
print(f"4 1 2  x = 14 -> {alt_list2([4,1, 2], 14)}")
print("")


def f_rec(a, b):
    if a == b:
        return 0
    elif a < b:
        return 1 + f_rec(a + 2, b)
    else:
        return 1 + f_rec(a, b + 1)


print("3.")
print(f"22 30 -> {f_rec(22, 30)}")
print(f"22 20 -> {f_rec(22, 20)}")
print(f"24 28 -> {f_rec(24, 28)}")
print("")


def lista_rec(lis):
    if len(lis) == 0:
        return []
    else:
        r = lista_rec(lis[:-1])
        if lis[-1] % 2 == 1:
            r.append(lis[-1])
        return r


a4 = lista_rec([1, 2, 1, 3, 11])
a5 = lista_rec([3, 4, 4, 3, 11])
a6 = lista_rec([9, 8, 1, 8, 2, 11])

print("4.")
print(f"1 2 1 3   ->", *a4)
print(f"3 4 4 3   ->", *a5)
print(f"9 8 1 8 2 ->", *a6)
print("")


def soma_algoritmos(n):
    l = list(map(int, str(n)))

    def soma_rec(lista):
        if len(lista) == 0:
            return 0
        else:
            return lista[-1] + soma_rec(lista[:-1])

    return soma_rec(l)


print("5.")
print(f"123456 -> {soma_algoritmos(123456)}")
print(f"1234   -> {soma_algoritmos(1234)}")
print("")


def soma_impares_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        if lista[-1] % 2 == 1:
            return lista[-1] + soma_impares_lista(lista[:-1])
        else:
            return soma_impares_lista(lista[:-1])


print("6.")
print(f"123456 -> {soma_impares_lista([1, 2, 3, 4, 5, 6])}")
print(f"1234   -> {soma_impares_lista([1, 2, 3, 4])}")
print("")
