# E. Achando monótonos não maximais
n = int(input())
linha = input()

count = 0
i = 0
while i < n:
    if linha[i] == "a":
        start = i
        while i < n and linha[i] == "a":
            i += 1
        length = i - start
        if length >= 2:
            count += length
    else:
        i += 1

print(count)
