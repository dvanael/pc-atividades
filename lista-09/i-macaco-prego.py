# I. Macaco Prego
test_num = 1
while True:
    N = int(input())
    if N == 0:
        break

    xs = []
    ys = []
    us = []
    vs = []

    for _ in range(N):
        X, Y, U, V = map(int, input().split())
        xs.append(X)
        ys.append(Y)
        us.append(U)
        vs.append(V)

    # inversao
    X_i = max(xs)
    Y_i = min(ys)
    U_i = min(us)
    V_i = max(vs)

    print(f"Teste {test_num}")

    # inversao valida
    if X_i <= U_i and V_i <= Y_i:
        print(X_i, Y_i, U_i, V_i)
    else:
        print("nenhum")

    print()
    test_num += 1
