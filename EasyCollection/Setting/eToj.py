import xlrd
import json


def eToj(file):
    data = xlrd.open_workbook(file)
    table = data.sheets()[0]
    nrows = table.nrows  # 行数
    ncols = table.ncols

    key=[]
    value = []
    # i=0
    # while i<=71:
    for i in range(0,ncols):
        a=table.cell(0,i).value
        key.append(a)
    for j in range(1,nrows):
        dic={}
        for k in range(0,ncols):
            cell_data=table.cell(j,k).value
            dic[key[k]]=str(cell_data)
        value.append(dic)
    return value



