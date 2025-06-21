def palindromo(s):
    if len(s) == 0:
        return True
    else:
        # compara primiero e ultimo & prox lista sem o primeiro e o ultimo
        return s[0] == s[-1] and palindromo(s[1:-1])


print(palindromo("arara"))
print(palindromo("arar"))
