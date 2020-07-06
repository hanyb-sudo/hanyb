class Person(object):
    def __init__(self,name,age,height,weight):
        print("init.....")
        print(name,age,weight,height)

        # 定义属性
        self.age = age
        self.name = name
        self.height = height
        self.weight = weight
    # 在构造函数中定义属性
    # name = ""
    # age = 0
    # height = 0
    # weight = 0
    def run(self):
        print("run.....")
    def eat(self,food):
        print("eat "+food)

per = Person("Hanne",22,180,60)

'''
构造函数：__init__()在使用类创建对象的时候自动调用

注意：如果不显示写出的构造函数，默认会自动添加一个空的构造函数
'''