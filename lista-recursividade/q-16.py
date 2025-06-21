def junta(l1, l2):
    if len(l1) == 0:
        return l2
    if len(l2) == 0:
        return l1

    if l1[-1] > l2[-1]:
        return junta(l1[:-1], l2) + [l1[-1]]
    else:
        return junta(l1, l2[:-1]) + [l2[-1]]


print(junta([1, 2, 3], [4, 5, 6]))
