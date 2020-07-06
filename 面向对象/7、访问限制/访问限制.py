class Person(object):
    def __init__(self, name, age, height, weight, money):
        print("init runing......")
        self.age = age
        self.name = name
        self._height = height
        self.weight = weight
        self.__money = money

    def run(self):
        print("run.....")

    def eat(self, food):
        print("eat " + food)

    # 通过内部的方法，去修改私有属性
    # 通过自定义的方法实现私有属性的赋值与取值
    def setMoney(self, money):
        # 数据的过滤
        if money < 0:
            money = 0
        self.__money = money

    def getMoney(self):
        return self.__money

per = Person("han", 22, 170, 60,10000)
# per.age = 30
# print(per.age)

# 相当于自行增加的属性
per.__money = 10
print(per.__money)


# 在动态运行中可以自行增加属性
# per.a = 0
# print(per.a)
'''
如果要让类的内部属性不被外部直接访问，在属性前加两个下划线(__)，
在Python中如果在属性前加两个下划线，那么这个属性就变成了私有属性。
外部不能使用，内部能访问

'''

# 不能直接访问per.__money是因为Python解释器把__money变成了_Person__money，
# 仍然可以用_Person__money去访问，但是强烈建议不要这么干，
# 不同的解释器可能存在解释的变量名不一致

print(per._Person__money)

# 在Python中，__xxx__属于特殊变量，可以直接访问
# 在Python中，_xxx 这样的实例变量外部是可以访问的，但是，按照约定的规则，当我们看到这样的变量时，
# 意思是“虽然我可以被访问，但是请把我视为私有变量，不要直接访问我”
print(per._height)