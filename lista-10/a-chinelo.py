# A. Chinelos


def qntd_to_list(qntd: int) -> list:
    lista = []
    for _ in range(qntd):
        i = int(input())
        lista.append(i)
    return lista


estoque = qntd_to_list(int(input()))
pedidos = qntd_to_list(int(input()))

vendas = 0
for p in pedidos:
    if estoque[p - 1] > 0:
        vendas += 1
        estoque[p - 1] -= 1

print(vendas)
