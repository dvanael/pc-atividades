a, b = map(int, input().split())

if a == 1:
    print("Total: R$", "{:.2f}".format(4 * b))
elif a == 2:
    print("Total: R$", "{:.2f}".format(4.50 * b))
elif a == 3:
    print("Total: R$", "{:.2f}".format(5 * b))
elif a == 4:
    print("Total: R$", "{:.2f}".format(2 * b))
elif a == 5:
    print("Total: R$", "{:.2f}".format(1.5 * b))
