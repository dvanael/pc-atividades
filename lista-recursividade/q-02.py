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


print(primo(int(input())))
