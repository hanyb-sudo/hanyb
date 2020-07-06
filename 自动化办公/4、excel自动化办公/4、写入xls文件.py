'''

只能写入xls文件

'''

from collections import OrderedDict
#写入数据
from pyexcel_xls import save_data

def makeExcelFile(path, data):
    dic = OrderedDict()
    for sheetName, sheetValue in data.items():
        d={}
        d[sheetName] = sheetValue
        dic.update(d)
    print(dic)
    save_data(path, dic)

path = r"a.xls"
data = {"表1":[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]],"表2":[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]}
makeExcelFile(path, data)