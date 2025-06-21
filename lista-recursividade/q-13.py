def inverter_lista(lista):
    if len(lista) == 0:
        return []
    else:
        return [lista[-1]] + inverter_lista(lista[:-1])


print(inverter_lista([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
