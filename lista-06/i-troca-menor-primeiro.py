def lista_troca_menor_primeiro(lista):
    menor = lista[0]
    counter = 0
    # menor item
    for index, item in enumerate(lista):
        if menor > item:
            menor = item
            counter = index
    if menor == lista[0]:
        return 0
    else:
        valor = lista[counter]
        lista[counter] = lista[0]
        lista[0] = valor
        return 1


# print(lista_troca_menor_primeiro([-101, 4, 6, 8, 2, 3, -5, 7]))
