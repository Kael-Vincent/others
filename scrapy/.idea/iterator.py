
def iterator():
    R = range(10)
    print(R)
    r = iter(R)
    l = list(r)
    print(len(l))
    print(l[0])
    for r1 in l:
            print(r1)

    M = map(abs,(-1,0,1))
    for x in M:
            print(x)
    
    Z = zip((1,2,3),(4,5,6),(7,8,9,10))
    print(Z)
    for z in Z:print(z)
    S = 'ahhkklklhl'
    sum = 0
    for s in S:
            print(ord(s))
            sum+=ord(s)
        #     print(sum)
            print(map(ord,s))
    f = maker(2)

    print(f(4))

def maker(n):
        def action(m):
                return n**m
        return action


def mysum(L):
        # print(L)
        # if not L:
        #         return 0
        # else:
        #         return L[0]+mysum(L[1:])
        return 0 if not L else L[0]+mysum(L[1:])

def echo(message):print(message)

def indirect(func,args):
        func(args)
if __name__ == '__main__':
    iterator()
    mysum([1,2,3,4,5,6])
    indirect(echo,'hello world!')
    maker(9)