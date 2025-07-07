# H. Loop Musical

while True:
    n = int(input())
    if n == 0:
        break

    h = list(map(int, input().split()))

    picos = 0
    for i in range(n):
        # pico. + - + or - + -
        if h[i-2] < h[i-1] > h[i]:
            picos += 1

        elif h[i-2] > h[i-1] < h[i]:
            picos += 1

    print(picos)