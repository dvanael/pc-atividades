# B. OBI

competidores, min_pontos = map(int, input().split())
pontos = []
for _ in range(competidores):
    x, y = map(int, input().split())
    total_pts = x + y
    pontos.append(total_pts)

convidados = 0
for c in pontos:
    if c >= min_pontos:
        convidados += 1

print(convidados)
