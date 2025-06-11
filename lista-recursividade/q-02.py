def primo(n, d=1):

    if n == 0:
        return 0
    
    if d > n:
        return 0

    if n % d == 0:
        return True + primo(n, d+1)
    else:
        return False + primo(n, d+1)
    
print(primo(int(input())))