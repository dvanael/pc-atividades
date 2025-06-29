a = int(input())
divisores = []
for i in range(1, a + 1):
    if a % i == 0:
        divisores.append(i)

print(*divisores)
