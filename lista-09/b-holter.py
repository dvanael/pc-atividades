# B. Holter
n = int(input())
batimentos = []
for _ in range(n):
    b = int(input())
    batimentos.append(b)

media = sum(batimentos) // n
dez_cent = media * 0.1

a = 0
for i in batimentos:
    if i > int(media + dez_cent) or i < int(media - dez_cent):
        a += 1

print(int(media))
print(a)
