import os
import os.path

def getAllDir(path,space=""):
    fileList = os.listdir(path)
    # 每一次调用就加一次空格
    space+="   "

    for file in fileList:
        # 绝对路径
        absPath = os.path.join(path, file)
        if os.path.isdir(absPath):
            print(space+file)
            # 递归调用
            getAllDir(absPath,space)
        else:
            print(space+file)



getAllDir(r"C:\Users\Lenovo\Desktop\python学习（公司）")