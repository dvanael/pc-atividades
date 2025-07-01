def primo(p: int) -> bool:
    x = 0
    for i in range(1, p + 1):
        if p % i == 0:
            x += 1

    if x == 2:
        return True
    else:
        return False


def primo_maior_n(p: int) -> int:
    n = p + 1
    while not primo(n):
        n += 1
    return n


num = int(input())
print(primo_maior_n(num))
