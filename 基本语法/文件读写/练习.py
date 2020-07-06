placeName = input("请输入要查找的地方：")

def findPlace(placeName):
    path = r"C:\Users\Lenovo\Desktop\毕业论文\毕业论文数据\监测点信息.txt"
    with open(path,"r") as f:
        '''
        line = f.readline()
        while line != '':
            line = f.readline()
            if placeName in line:
                print(line)
        '''
        # print(f.readlines())
        # print(type(f.readlines()))

        f.readline()
        for line in f.readlines():
            if placeName in line:
                print(line)
                break


print(placeName+"的监测点信息为：")
findPlace(placeName)