# H. Escadinha
n = int(input())
seq = list(map(int, input().split()))

if n == 1:
    print(1)

else:
    count = 0
    start = 0
    diff = seq[1] - seq[0]

    for i in range(1, n):
        diff_atual = seq[i] - seq[i - 1]
        if diff_atual != diff:
            count += 1
            start = i - 1
            diff = diff_atual

    count += 1
    print(count)
