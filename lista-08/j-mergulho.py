# J. Mergulho

n, r = map(int, input().split())
retornados = list(map(int, input().split()))
not_r = []

for i in range(1, n + 1):
    if i not in retornados:
        not_r.append(i)

if not_r:
    print(*not_r, end=" ")
else:
    print("*")
