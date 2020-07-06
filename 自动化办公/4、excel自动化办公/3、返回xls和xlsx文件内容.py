#有序字典
from collections import OrderedDict

from pyexcel_xls import get_data

def readXlsAndXlsxFile(path):
    #创建一个有序的字典，excel中的数据都是有顺序的，所以用有序字典
    dic = OrderedDict()

    #抓取数据
    xdata = get_data(path) #OrderedDict([('Sheet1', [['年度', '总人口(万人)', '出生人口(万人)', '死亡人口(万人)'.....
    for sheet in xdata:
        dic[sheet] = xdata[sheet]

    return dic



path1 =r"C:\Users\Lenovo\Desktop\课程设计\aleardy deal data.xls"
path2 =r"C:\Users\Lenovo\Desktop\课程设计\2015data.xlsx"

readXlsAndXlsxFile(path2)
dic = readXlsAndXlsxFile(path2)
print(dic)