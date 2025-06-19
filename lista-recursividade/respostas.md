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