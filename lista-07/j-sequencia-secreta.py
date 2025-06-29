n = int(input())
seq = []
for x in range(n):
    seq.append(int(input()))

anterior = seq[0]
n_blocos = 1

for x in range(1, n):
    if seq[x] != anterior:
        n_blocos += 1
    anterior = seq[x]

print(n_blocos)
