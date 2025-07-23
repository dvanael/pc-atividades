# J. Fase
n = int(input())
k = int(input())

pontuacoes = []
for _ in range(n):
    ponto = int(input())
    pontuacoes.append(ponto)

pontuacoes.sort(reverse=True)
pontuacao_minima = pontuacoes[k - 1]

classificados = 0
for p in pontuacoes:
    if p >= pontuacao_minima:
        classificados += 1
classificados = sum(1 for p in pontuacoes if p >= pontuacao_minima)

print(classificados)
