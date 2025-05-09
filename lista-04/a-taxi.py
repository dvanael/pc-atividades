la, lg, ra, rg = map(float, input().split())
if (la / ra) == (lg / rg):
    print("G")
elif (la / ra) < (lg / rg):
    print("A")
else:
    print("G")
