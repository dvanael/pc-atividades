def polinomio(coeficientes, x):
    if len(coeficientes) == 0:
        return 0
    else:
        # Pn(x) = x.Pn-1(x) + an -> an + x.Pn-1(x)
        return coeficientes[0] + x * polinomio(coeficientes[1:], x)


print(polinomio([1, 2, 3], 2))
print(polinomio([1, 2, 3], 3))
