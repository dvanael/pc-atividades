s, mi = map(int, input().split())

tempo = 0
while mi > 0.5:
    mi = mi/2
    tempo += s

dias = tempo // 86400
horas = (tempo % 86400) // 3600
minutos = ((tempo % 86400) % 3600) // 60
segundos = int(((tempo % 86400) % 3600) % 60)

dias = f"{dias} dias"
horas = "{:02}".format(horas)
minutos = "{:02}".format(minutos)
segundos = "{:02}".format(segundos)

print(f"{dias} {horas}:{minutos}:{segundos}")