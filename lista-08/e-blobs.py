# E. Blobs
def metade_comida_por_dia(comida: float) -> str:
    dias = 0
    while comida > 1.0:
        dias += 1
        comida /= 2
    return f"{dias} dias"


def blobs(n: int) -> str:
    for i in range(n):
        comida = float(input())
        print(metade_comida_por_dia(comida))
    return


num_testes = int(input())
blobs(num_testes)
