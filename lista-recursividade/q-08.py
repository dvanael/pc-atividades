def indice_do_maior(lista):
    def busca_index(index, maior):
        if index == len(lista):
            return maior
        if lista[index] > lista[maior]:
            maior = index
        return busca_index(index + 1, maior)

    return busca_index(1, 0)


print(indice_do_maior([2, 3, 7, 2, 9, 0]))  # -> 4
