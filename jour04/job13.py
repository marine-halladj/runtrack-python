def doublon():
    L=[10,20,30,20,10,50,60,40,80,50,40]
    newL=[]

    for i in L:
        if i not in newL:
            newL.append(i)

    print(newL)
doublon()