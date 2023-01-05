def calculate(paires):
    total = 0
    for i in range(0, len(paires)):
        if paires[i] %2 == 0:
            total += paires[i]
    return total
L=[8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

print(calculate(L))

calculate(L)
