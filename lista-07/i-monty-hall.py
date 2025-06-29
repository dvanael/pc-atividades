n = int(input())
ganhos = 0

for x in range(n):
    porta_carro = int(input())
    if porta_carro != 1:
        ganhos += 1

print(ganhos)
