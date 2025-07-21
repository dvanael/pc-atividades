# D. Enigma
def check_same_letter(a: list, b: list) -> bool:
    for i in range(len(a)):
        if a[i] == b[i]:
            return False
    return True


coded = input()
crib = input()
crib_certa = 0
i = 0
while not (len(crib) + i) > len(coded):
    if check_same_letter(a=coded[i : len(crib) + i], b=crib):
        crib_certa += 1
    i += 1

print(crib_certa)
