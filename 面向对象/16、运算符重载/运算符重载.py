
class Person(object):
    def __init__(self, num):
        self.num = num

    # 运算符重载
    def __add__(self, other):
        return self.num + other.num

per1 = Person(1)
per2 = Person(2)
print("method1 =",per1 + per2)  #等价于per1.__add__(per2)
print("method2 =",per1.__add__(per2))