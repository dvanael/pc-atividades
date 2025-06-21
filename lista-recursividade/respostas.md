# Respostas da Lista de Recursividade

## 1.
```python
def conta_divisores(n):
    def conta(d):
        if d == 0:
            return 0
        elif n % d == 0:
            return 1 + conta(d - 1)
        else:
            return conta(d - 1)

    return conta(n)

```

## 2.
```python
def primo(n):
    def conta(d):
        if d == 0:
            return 0
        elif n % d == 0:
            return 1 + conta(d - 1)
        else:
            return conta(d - 1)

    if conta(n) == 2:
        return True
    else:
        return False

```

## 3.

### a.

```scss
f(1,8)
 ├── f(3,7)
 │    ├── f(5,6)
 │    │    ├── f(7,5) → 6
 │    │    ├── f(6,4) → 5
 │    │    → f(6,5) → 5.5
 │    ├── f(4,5)
 │    │    ├── f(6,4) → 5
 │    │    ├── f(5,3) → 4
 │    │    → f(5,4) → 4.5
 │    → f(5.5,4.5) → 5
 ├── f(2,6)
 │    ├── f(4,5) → 4.5
 │    ├── f(3,4)
 │    │    ├── f(5,3) → 4
 │    │    ├── f(4,2) → 3
 │    │    → f(4,3) → 3.5
 │    → f(4.5,3.5) → 4
 → f(5,4) → 4.5
```

### b.

```bash
4.5
```


### c.

Calcula uma média entre `x` e `y` quando que `x ≥ y`, recursivamente faz adicioções em `x` e subtrações em `y` até a condição, então retorna `(x + y) / 2`.


## 4.

```python
def conta_algarismos(n):
    if n < 10:
        return 1
    else:
        return 1 + conta_algarismos(n // 10)

```

## 5.
```python
def conta_bits(n):
    if n == 0:
        return 0
    else:
        return 1 + conta_bits(n // 2)

```

## 6.
```python
def comb(n, k):
    if k == n:
        return 1
    elif k == 1:
        return n
    else:
        return comb(n - 1, k - 1) + comb(n - 1, k)

```

```scss
comb(6,4)
 ├── comb(5,3)
 │    ├── comb(4,2)
 │    │    ├── comb(3,1) → 3
 │    │    ├── comb(3,2)
 │    │    │    ├── comb(2,1) → 2
 │    │    │    ├── comb(2,2) → 1
 │    │    │    → 2 + 1 = 3
 │    │    → 3 + 3 = 6
 │    ├── comb(4,3)
 │    │    ├── comb(3,2) → 3
 │    │    ├── comb(3,3) → 1
 │    │    → 3 + 1 = 4
 │    → 6 + 4 = 10
 ├── comb(5,4)
 │    ├── comb(4,3) → 4
 │    ├── comb(4,4) → 1
 │    → 4 + 1 = 5
→ 10 + 5 = 15

```

```scss
comb(6,3)
 ├── comb(5,2)
 │    ├── comb(4,1) → 4
 │    ├── comb(4,2)
 │    │    ├── comb(3,1) → 3
 │    │    ├── comb(3,2)
 │    │    │    ├── comb(2,1) → 2
 │    │    │    ├── comb(2,2) → 1
 │    │    │    → 2 + 1 = 3
 │    │    → 3 + 3 = 6
 │    → 4 + 6 = 10
 ├── comb(5,3)
 │    ├── comb(4,2) → 6
 │    ├── comb(4,3)
 │    │    ├── comb(3,2) → 3
 │    │    ├── comb(3,3) → 1
 │    │    → 3 + 1 = 4
 │    → 6 + 4 = 10
→ 10 + 10 = 20

```

## 7.

```python
def divisores(n, k=None):
    d = []

    if k == None:
        k = n

    def adiciona_div(x, y):
        if x == 0 or y == 0:
            return d

        if x % y == 0:
            d.append(y)

        return adiciona_div(x, y - 1)

    return adiciona_div(n, k)

```

## 8.

```python
def indice_do_maior(lista):
    def busca_index(index, maior):
        if index == len(lista):
            return maior
        if lista[index] > lista[maior]:
            maior = index
        return busca_index(index + 1, maior)

    return busca_index(1, 0)

```

## 9.

```python
def soma_pares(lista):
    if len(lista) == 0:
        return 0
    else:
        if lista[-1] % 2 == 0:
            return lista[-1] + soma_pares(lista[:-1])
        else:
            return soma_pares(lista[:-1])

```

## 10.

```python
def ordenada(lista):
    # se uma lista nao tem elementos, ela é ordenada?
    if len(lista) == 0 or len(lista) == 1:
        return True
    else:
        if lista[-1] > lista[-2]:
            return ordenada(lista[:-1])
        else:
            return False

```

## 11.

```python
def primos(lista):
    l = []

    def primo(n):
        def conta(d):
            if d == 0:
                return 0
            elif n % d == 0:
                return 1 + conta(d - 1)
            else:
                return conta(d - 1)

        if conta(n) == 2:
            return True
        else:
            return False

    def adiciona_primo(l1):
        if len(l1) == 0:
            return l

        if primo(l1[-1]):
            l.append(l1[-1])

        return adiciona_primo(l1[:-1])

    return adiciona_primo(lista)

```

## 12.

```python
def ocorrencias(lista, x):
    if len(lista) == 0:
        return 0
    else:
        if lista[-1] == x:
            return 1 + ocorrencias(lista[:-1], x)
        else:
            return ocorrencias(lista[:-1], x)

```

## 13.

```python
def inverter_lista(lista):
    if len(lista) == 0:
        return []
    else:
        return [lista[-1]] + inverter_lista(lista[:-1])


```

## 14.

```python
def palindromo(s):
    if len(s) == 0:
        return True
    else:
        # compara primiero e ultimo & prox lista sem o primeiro e o ultimo
        return s[0] == s[-1] and palindromo(s[1:-1])

```

## 15.

```python
def polinomio(coeficientes, x):
    if len(coeficientes) == 0:
        return 0
    else:
        # Pn(x) = x.Pn-1(x) + an -> an + x.Pn-1(x)
        return coeficientes[0] + x * polinomio(coeficientes[1:], x)

```

## 16.

```python
def junta(l1, l2):
    if len(l1) == 0:
        return l2
    if len(l2) == 0:
        return l1

    if l1[-1] > l2[-1]:
        return junta(l1[:-1], l2) + [l1[-1]]
    else:
        return junta(l1, l2[:-1]) + [l2[-1]]

```