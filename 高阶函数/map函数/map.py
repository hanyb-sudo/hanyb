'''
map函数接收的是两个参数，一个函数，一个序列，其功能是将序列中的值处理再依次返回至列表内。
其返回值为一个迭代器对象--》例如：<map object at 0x00000214EEF40BA8>。

'''
num=[1,2,3,4,5]
def square(x):
    return x**2
#map函数模拟
def map_test(func,iter):
    num_1=[]
    for i in iter:
        ret=func(i)
        # print(ret)
        num_1.append(ret)
    return num_1.__iter__() #将列表转为迭代器对象


#map_test函数
print(list(map_test(square,num)))
#map函数
print(list(map(square,num)))

#当然map函数的参数1也可以是匿名函数、参数2也可以是字符串
print(list(map_test(lambda x:x.upper(),"amanda")))
# print(type(map_test(lambda x:x.upper(),"amanda")))
print(list(map(lambda x:x.upper(),"amanda")))
'''

num = ["1","2","3","4","5"]
a = map(lambda x:int(x),num)
print(a)
'''