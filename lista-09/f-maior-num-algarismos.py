# F. Maior número de algarismos
def int_to_list(n: int) -> list:
    return list(map(int, str(n)))


def maior_num_algatismos(n: list, m: list) -> int:
    if len(str(sum(n))) > 1 or len(str(sum(m))) > 1:
        return maior_num_algatismos(int_to_list(sum(n)), int_to_list(sum(m)))

    if sum(n) > sum(m):
        return 1

    if sum(m) > sum(n):
        return 2

    if sum(n) == sum(m):
        return 0


n, m = map(int, input().split())
while not (n == 0 and m == 0):
    n = int_to_list(n)
    m = int_to_list(m)

    print(maior_num_algatismos(n, m))

    n, m = map(int, input().split())
