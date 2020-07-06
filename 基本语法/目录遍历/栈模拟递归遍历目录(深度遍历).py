import os
def getAllDirDeep(path):#深度遍历
    stack=[]     #建立一个栈
    stack.append(path)    #将第一个目录进行压栈

    #处理栈，当栈为空的时候结束循环
    while len(stack) != 0:
        # 从栈里取出数据
        dirpath = stack.pop()
        # 目录下所有文件
        fileList=os.listdir(dirpath)

        # 处理一个文件，如果是普通文件则打印出来，如果是目录文件就将该目录的地址压栈
        for fileName in fileList:
            # 获取绝对路径
            absPath = os.path.join(dirpath, fileName)
            if os.path.isdir(absPath):#判断是否是目录
                # 是目录则压栈
                print("目录："+fileName)
                stack.append(absPath)
            else:
                # 不是目录则打印普通文件
                print("普通文件："+fileName)



getAllDirDeep(r"C:\Users\Lenovo\Desktop\数据挖掘实验")