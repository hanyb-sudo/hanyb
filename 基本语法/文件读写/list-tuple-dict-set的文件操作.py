import pickle #数据持久性模块

path="file.txt"

myList=["韩","义","博",1,2,3,4,5]

# 写入文件
with open(path,"wb") as f:
    pickle.dump(myList,f)

# 读取文件
tempList=[]
with open(path,"rb") as f1:
    tempList=pickle.load(f1)
    print(tempList)