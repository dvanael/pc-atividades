# F. Fita Colorida
qntd_quadrados = int(input())
fita = list(map(int, input().split()))


# find 0
def zero_positions(fita: list[int]) -> list[int]:
    return [i for i, x in enumerate(fita) if x == 0]


def paint(
    zeros: list[int],
    fita: list[int],
    blank: int,
    length: int,
) -> list[int]:

    for index in range(length):
        if not blank in fita:
            return fita

        for i in zeros:
            if i - index >= 0:
                if fita[i - index] == blank:
                    fita[i - index] = index if index < 9 else 9

            if i + index < length:
                if fita[i + index] == blank:
                    fita[i + index] = index if index < 9 else 9

    return fita


print(*paint(zeros=zero_positions(fita), fita=fita, length=qntd_quadrados, blank=-1))
