def test1(n):
    lst=[]
    for i in range(n*10000):
        lst = lst + lst
    print(lst)

test1(1)