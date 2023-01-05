def first_number():
    for i in range(0,1001):
        if i > 1:
            for n in range(2,i):
                if (i%n) == 0:
                    break
            else:
                 print(i)
first_number()