def func2(l01, num):
    q = 0
    for i in range(len(l01)):
        for j in range(i + 1, len(l01)):
            print(f"{l01[i]} + {l01[j]} = {l01[j]+l01[i]}")
            if l01[j] + l01[i] >= num:
                q += 1
    return q


# n = int(input())
# lista = list(map(int, input().split()))
# lista.append(n - 1)
# print(func2(lista, n))


def g(l01):
    if len(l01) == 0:
        return 1000
    else:
        n = l01[-1]
        print(n)
        if n % 2 == 1 and n > 0:
            return min(n, g(l01[:-1]))
        else:
            return g(l01[:-1])


# lista = list(map(int, input().split()))
# lista.append(len(lista) - 2)
# print(g(lista))

lista01 = list(map(input().split()))
lista02 = list(map(input().split()))
lista02 = [x for x in lista02 if x not in lista01]
print(lista02)
