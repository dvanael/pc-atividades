# E. Saltadores Alegres


def jolly_jumper_checker(seq: list[int]) -> bool:
    lenght = seq[0]
    if lenght == 1:
        return True
    seq.pop(0)

    diference = []
    for i in range(1, lenght):
        n = abs(seq[i] - seq[i - 1])
        if n not in diference:
            diference.append(n)

    for i in range(1, lenght):
        if i not in diference:
            return False

    return True


while True:
    try:
        seq = list(map(int, input().split()))
        print("Alegre" if jolly_jumper_checker(seq) else "Nao alegre")
    except EOFError:
        break
