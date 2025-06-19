def conta_divisores(n):
    def conta(d):
        if d == 0:
            return 0
        elif n % d == 0:
            return 1 + conta(d - 1)
        else:
            return conta(d - 1)

    return conta(n)


print(conta_divisores(int(input())))
