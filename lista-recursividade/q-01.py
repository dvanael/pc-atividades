def conta_divisores(n, d=1):
    if n == 0:
        return 0
    
    if d > n:
        return 0

    print(n, d)
    if n % d == 0:
        return 1 + conta_divisores(n, d+1)
    else:
        return conta_divisores(n, d+1)

print(conta_divisores(int(input())))
