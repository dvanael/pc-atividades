def conta_bits(n):
    if n == 0:
        return 0
    else:
        return 1 + conta_bits(n // 2)


print(conta_bits(int(input())))
