import csv

def readCsv(path):
    with open(path, "r") as f:
        listInfo = []
        allFileInfo = csv.reader(f)
        print(allFileInfo)
        for row in allFileInfo:
            listInfo.append(row)
    return listInfo

path =r"C:\Users\Lenovo\Desktop\大数据方法实验\贝叶斯网络-bayes数据.csv"

Info = readCsv(path)
print(Info)
# 形如[[],[],[]...]形式