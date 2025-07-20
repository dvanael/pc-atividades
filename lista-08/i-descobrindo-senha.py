# I. Descobrindo Senha
def ordena(par):
    oleo, digito = par
    return (-oleo, digito)  # Ordem descrescente de oleosidade


caso = 1
while True:
    try:
        n = int(input())

        v = list(map(float, input().split()))

        pad = []
        for i in range(len(v)):
            pad.append((v[i], i))
        pad.sort(key=ordena)

        senha = ""
        for i in range(n):
            digito = pad[i][1]
            senha += str(digito)

        print(f"Caso {caso}: {senha}")
        caso += 1

    except EOFError:
        break
