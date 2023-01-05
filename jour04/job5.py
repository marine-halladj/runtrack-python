def list_L():
    L=[10,15,25,45,23]
    print(L[1])
    L[3]=L[2]+L[4]
    L.insert(4,L[3])
    print(L[4])
    
list_L()