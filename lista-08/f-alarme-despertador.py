# F. Alarme Despertador
def horas_para_segundos(hora: int, minuto: int) -> int:
    return hora * 3600 + minuto * 60


def calcular_minutos_diferença(h1: int, m1: int, h2: int, m2: int) -> int:
    h_inicial = horas_para_segundos(h1, m1)
    h_final = horas_para_segundos(h2, m2)

    diferença = h_final - h_inicial
    if diferença < 0:
        diferença += 24 * 3600

    minutos = diferença // 60
    return minutos


while True:
    h1, m1, h2, m2 = map(int, input().split())

    if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
        break

    print(calcular_minutos_diferença(h1, m1, h2, m2))
