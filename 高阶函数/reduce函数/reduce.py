'''
reduce函数也是一个参数为函数，一个为可迭代对象的高阶函数，
reduce把结果继续和序列的下一个元素累计运算
其返回值为一个值而不是迭代器对象，故其常用与叠加、叠乘等，

'''

#reduce函数不是内置函数，而是在模块functools中的函数，故需要导入
from functools import reduce

nums=[1,2,3,4,5,6]
#reduce函数的机制
def reduce_test(func,array,ini=None): #ini作为基数
    if ini == None:
        ret =array.pop(0)
    else:
        ret=ini
    for i in array:
        ret=func(ret,i)
        # print(ret,i)
    return ret
'''
#reduce_test函数，叠乘
print(reduce_test(lambda x,y:x*y,nums,100))
#reduce函数，叠乘
print(reduce(lambda x,y:x*y,nums,100))
'''
num = ["1","2","3","4","5"]
a = reduce(lambda x,y:x+y,num)
print(a)
print(type(a))