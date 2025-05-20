n = int(input())

if n <= 10:
    v = 7
elif n <= 30:
    v = n - 10 + 7
elif n <= 100:
    v = ((n - 30)*2) + 27
else:
    v = ((n - 100)*5) + 167

print(v)