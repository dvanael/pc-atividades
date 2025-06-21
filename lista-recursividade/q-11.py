def primo(n):
    def conta(d):
        if d == 0:
            return 0
        elif n % d == 0:
            return 1 + conta(d - 1)
        else:
            return conta(d - 1)

    if conta(n) == 2:
        return True
    else:
        return False


def primos(lista):
    l = []

    def adiciona_primo(l1):
        if len(l1) == 0:
            return l

        if primo(l1[-1]):
            l.append(l1[-1])

        return adiciona_primo(l1[:-1])

    return adiciona_primo(lista)
