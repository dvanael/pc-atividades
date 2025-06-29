x = int(input())
numeros = list(map(int, input().split()))

media = sum(numeros) / len(numeros)
print("{:.1f}".format(media))

maior, menor = 0, 0
l_maior, l_menor = [], []
for i in range(x):
    if numeros[i] < media:
        menor += 1
        l_menor.append(numeros[i])
    else:
        maior += 1
        l_maior.append(numeros[i])

print(menor, *l_menor)
print(maior, *l_maior)
