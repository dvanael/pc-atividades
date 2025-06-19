def comb(n, k):
    if k == n:
        return 1
    elif k == 1:
        return n
    else:
        return comb(n - 1, k - 1) + comb(n - 1, k)


print(comb(5, 3))
