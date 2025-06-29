x = int(input())
numeros = list(map(int, input().split()))

media = sum(numeros) / len(numeros)

print("{:.1f}".format(media))

maior, menor = 0, 0
for i in range(x):
    if numeros[i] < media:
        menor += 1
    else:
        maior += 1

print(menor)
print(maior)
