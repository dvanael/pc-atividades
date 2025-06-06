def dia(dia, mes, ano):
    meses = [
        "janeiro",
        "fevereiro",
        "marco",
        "abril",
        "maio",
        "junho",
        "julho",
        "agosto",
        "setembro",
        "outubro",
        "novembro",
        "dezembro",
    ]

    if mes < 1 or mes > 12:
        return "Data Invalida"

    if mes in [1, 3, 5, 7, 8, 10, 12]:
        max_dia = 31
    elif mes in [4, 6, 9, 11]:
        max_dia = 30
    elif mes == 2:
        max_dia = 28
    else:
        return "Data Invalida"

    if dia < 1 or dia > max_dia:
        return "Data Invalida"

    data = f"{'{:02d}'.format(dia)} de {meses[mes-1]} de {ano}"
    return data


# print(dia(11,1,908))
