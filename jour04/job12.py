def insertion(list):
    for i in range(1, len(list)):
        k=list[i]
        j=i-1
        while j >=0 and k < list[j] : 
            list[j+1] = list[j]
            j -= 1
        list[j + 1] = k
list = [54,42,89,74,12,36,45]
insertion(list)
for i in range(len(list)):
    print( list)