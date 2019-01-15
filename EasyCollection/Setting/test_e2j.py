#coding=utf-8
import xlrd
import xlwt
import json
import codecs

def _tongjiFirstRow():
    # xlrd.Book.encoding = "gbk"
    data = xlrd.open_workbook('D:/Users/yangyongqing/PycharmProjects/EasyCollection/src/refund_template.xlsx')
    table=data.sheets()[0]
    # 找到有几列几列
    nrows = table.nrows  # 行数
    ncols = table.ncols  # 列数
    totalArray = []
    arr = []
    for i in range(0, ncols):
        arr.append(table.cell(0, i).value);
        # end for
    for rowindex in range(1, nrows):
        dic = {}
        for colindex in range(0, ncols):
            s = table.cell(rowindex, colindex).value
            dic[arr[colindex]] = int(s)
            # end for
        totalArray.append(dic);
        # end for
    a = json.dumps(totalArray)
    return a
_tongjiFirstRow()