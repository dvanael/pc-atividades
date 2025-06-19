def divisores(n, k=None):
    d = []

    if k == None:
        k = n

    def adiciona_div(x, y):
        if x == 0 or y == 0:
            return d

        if x % y == 0:
            d.append(y)

        return adiciona_div(x, y - 1)

    return adiciona_div(n, k)


div = int(input())

print(divisores(div))
