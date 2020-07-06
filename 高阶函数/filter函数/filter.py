'''
filter函数也是接收一个函数和一个序列的高阶函数，其主要功能是过滤。
其返回值也是迭代器对象，例如：<filter object at 0x000002042D25EA90>

'''
names=["Alex","amanda","xiaowu"]
#filter函数机制
def filter_test(func,iter):
    names_1=[]
    for i in iter:
        if func(i): #传入的func函数其结果必须为bool值，才有意义
            names_1.append(i)
    return names_1
#filter_test函数
print(filter_test(lambda x:x.islower(),names))
#filter函数
print(list(filter(lambda x:x.islower(),names)))