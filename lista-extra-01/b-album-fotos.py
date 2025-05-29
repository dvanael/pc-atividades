l, h = map(int, input().split())
l1, h1 = map(int, input().split())
l2, h2 = map(int, input().split())

ls=l1+l2
hs=h2+h1



if (ls == l or ls == h) and (hs==l or hs == h):
    print("S")
elif (l1+h2 == l or l1+h2 == h) and (l2+h1 == l or l2+h1 == h):
    print("S")
else:
    print("N")

