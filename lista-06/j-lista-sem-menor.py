def sublista_sem_menor(lista):
    x = lista[0]
    counter = 0
    for index, item in enumerate(lista):
        if x > item:
            counter = index
            x = item
    copia = lista.copy()
    copia.pop(counter)
    return copia


# print(sublista_sem_menor([2, 2, 8, 12, 3]))
