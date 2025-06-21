def ordenada(lista):
    # se uma lista nao tem elementos, ela é ordenada?
    if len(lista) == 0 or len(lista) == 1:
        return True
    else:
        if lista[-1] > lista[-2]:
            return ordenada(lista[:-1])
        else:
            return False
