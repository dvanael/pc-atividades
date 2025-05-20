m = int(input())
a = int(input())
b = int(input())
c = m - (a+b)

maior = a
if maior < b:
    maior = b
if maior < c:
    maior = c

print(maior)