def dia_da_semana(h, d):
    dias_semana = [
        "Domingo",
        "Segunda-feira",
        "Terca-feira",
        "Quarta-feira",
        "Quinta-feira",
        "Sexta-feira",
        "Sabado",
    ]

    x = dias_semana.index(h)
    d = (x + d) % 7
    dia = dias_semana[d]
    return dia


# print(dia_da_semana(input(), int(input())))
