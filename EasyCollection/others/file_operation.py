def f_operat():
    f = open("D:/Users/yangyongqing/PycharmProjects/EasyCollection/src/save_session.txt", 'r+')
    session="ajsngkg12sse45"
    #print(session)
    f.write(session)
    fo=f.read()
    print(fo)
    position = f.tell()
    #print(position)
    f.close()

def read_entrust_id():
    f=open("D:/Users/yangyongqing/PycharmProjects/EasyCollection/src/save_entrust_id.txt",'r')
    entrust_id=f.read()
    f.close()
    return int(entrust_id)
def read_file():
    f=open("D:/Users/yangyongqing/PycharmProjects/EasyCollection/src/save_session.txt",'r')
    session_key=f.read()
    f.close()
    return session_key
def read_group_id():
    f = open("D:/Users/yangyongqing/PycharmProjects/EasyCollection/src/save_group_id.txt", 'r')
    group_id=f.read()
    f.close()
    return int(group_id)
