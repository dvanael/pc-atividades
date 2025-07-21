# A. Jogo de Estrátegia
j, r = map(int, input().split())
pontos_v = list(map(int, input().split()))

# Separa os pontos de cada rodada em uma lista
pontos_rodada = []
slice_start = 0
slice_end = j
for i in range(r):
    pontos_rodada.append(pontos_v[slice_start:slice_end])
    slice_start += j
    slice_end += j

# Faz uma lista dos jogadores
jogador_pontos = []
for i in range(j):
    jogador_pontos.append([i])

# Soma os pontos de cada rodada ao jogador especifico
for p in pontos_rodada:
    for i, x in enumerate(p):
        if len(jogador_pontos[i]) > 1:
            jogador_pontos[i][1] += x
        else:
            jogador_pontos[i].append(x)

# Jogador com maior pontos
maior = -1
vencedor = 0
for i, x in enumerate(jogador_pontos):
    if x[1] >= maior:
        maior = x[1]
        vencedor = i + 1

print(vencedor)
