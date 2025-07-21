# C. Lâmpadas


def bool_to_int(b: bool) -> int:
    if b:
        return 1
    return 0


# I¹ = ~A
def inverter_a(estado: bool) -> bool:
    return not estado


# I² = ~A ~B
def inverter_a_b(estado_a: bool, estado_b: bool) -> bool:
    return not estado_a, not estado_b


n = int(input())
cliques = list(map(int, input().split()))
a = False
b = False

for i in range(n):
    if cliques[i] == 1:
        a = inverter_a(a)
    if cliques[i] == 2:
        a, b = inverter_a_b(a, b)

print(bool_to_int(a))
print(bool_to_int(b))
