
# -*- coding=utf-8 -*-
import xlrd
import json
import jsonobject

def get_repay():
    #读取本地excel文件
    data=xlrd.open_workbook('D:/Users/yangyongqing/Desktop/repayments.xlsx')
    #获取工作簿
    table=data.sheets()[0]
    #table=data.sheet_by_index(0)
    #获取行数和列数
    nrows=table.nrows
    ncols=table.ncols
    #获取标题行
    title=[]
    for i  in range(ncols):
        title_list=[]
        title_list=table.row(0)[i].value
        #print(title_list)
        title.append(title_list)
    print(title)
    #还款信息

get_repay()



