def ocorrencias(lista, x):
    if len(lista) == 0:
        return 0
    else:
        if lista[-1] == x:
            return 1 + ocorrencias(lista[:-1], x)
        else:
            return ocorrencias(lista[:-1], x)


print(ocorrencias([1, 2, 5, 4, 5, 6, 7, 8, 9, 10], 5))
