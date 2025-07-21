# G. Flores Florecem na França


def tautogram(phase: list) -> str:
    letter = None
    for i, word in enumerate(phase):
        if i == 0:
            letter = (word[0]).upper()
        else:
            if not (word[0].upper() == letter):
                return "N"
    return "Y"


phase = list(input().split())
while phase[0] != "*":
    print(tautogram(phase))
    phase = list(input().split())
