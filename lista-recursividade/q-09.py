def soma_pares(lista):
    if len(lista) == 0:
        return 0
    else:
        if lista[-1] % 2 == 0:
            return lista[-1] + soma_pares(lista[:-1])
        else:
            return soma_pares(lista[:-1])
