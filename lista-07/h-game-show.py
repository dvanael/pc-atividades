jogadas = int(input())
saldo = 100
melhor_s = saldo
for i in range(jogadas):
    a = int(input())
    saldo += a
    if melhor_s < saldo:
        melhor_s = saldo
print(melhor_s)
