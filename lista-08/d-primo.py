primo =  int(input())
n = primo + 1


def primo(p: int) -> bool:
    for i in range(1, p + 1):
        if p % i == 0:
            x += 1

    if x == 2:
        return True
    else:
        return False


def primo_maior_n(p: int) -> int:
    while True:
        for i in range(1, n + 1):
            if n % i == 0:
                x += 1

        if x == 2:
            print("Sim")
        else:
            print("Nao")
