a, b = map(int, input().split())
multiplos = []

for i in range(1, b + 1):
    if i % a == 0:
        multiplos.append(i)

print(*multiplos)
