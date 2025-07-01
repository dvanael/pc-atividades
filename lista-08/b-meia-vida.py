s, mi = map(int, input().split())
massa = float(mi)
divisoes = 0

while massa >= 0.5:
    massa /= 2
    divisoes += 1

tempo = s * divisoes

dias = tempo // 86400
horas = (tempo % 86400) // 3600
minutos = (tempo % 3600) // 60
segundos = tempo % 60

dias = f"{dias} dias"
horas = "{:02}".format(horas)
minutos = "{:02}".format(minutos)
segundos = "{:02}".format(segundos)

print(f"{dias} {horas}:{minutos}:{segundos}")
