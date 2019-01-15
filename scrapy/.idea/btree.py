class BtNode(object):
    def __init__(self,key=None,lchild=None,rchild=None):
        self.key = key
        self.lchild = lchild
        self.rchild = rchild


class BiTree(object):
    def __init__(self,data_list):
        self.it = iter(data_list)
    
    def createBiTree(self,bt=None):
        try:
            next_data = next(self.it)
            if next_data == None:
                bt = None
            else:
                bt = BtNode(next_data)
                bt.rchild = self.createBiTree(bt.rchild)
                bt.lchild = self.createBiTree(bt.lchild)
        except Exception as e:
            print(e)
        return bt
    
    # def preOrderTrave(self,bt):
        # if bt is not None: