from dealFile import DealFile

def func(str):
    str +="******"
    print(str)
dealFile = DealFile()

path = r"C:\Users\Lenovo\Desktop\毕业论文\论文\20200318_2020届论文指导过程.pdf"
# callback   回调函数
dealFile.readPDF(path, callback=func)