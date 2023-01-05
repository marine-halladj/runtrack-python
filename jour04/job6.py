def quelconque():
    ninja=["naruto","sasuke","rocklee","kakashi","jiraya"]
    idx1 = ninja.index('naruto')
    idx2 = ninja.index('jiraya')
    ninja[idx1],ninja[idx2] = ninja[idx2],ninja[idx1]
    print(ninja)

quelconque()