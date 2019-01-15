import datetime


def add():
    begin = datetime.datetime.now()
    a = 10000
    for i in range(a):
        a+=1
        print(a)
    end = datetime.datetime.now()
    print(end-begin)


if __name__ == '__main__':
    add()