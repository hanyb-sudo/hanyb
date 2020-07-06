class Person(object):
    name = ""
    age = 0
    height = 0
    weight = 0
    def run(self):
        print("run.....")
    def eat(self,food):
        print("eat "+food)


person1 = Person()
'''
访问属性
格式：对象名.属性名
赋值：对象名.属性名 = 新值
'''
person1.name = "韩义博"
person1.age = 23
person1.weight = 60
person1.height = 170
print(person1.name,person1.age,person1.weight,person1.height)

'''
访问方法：
格式：对象名.方法名(参数列表)
'''
person1.eat("banana")

# 问题：目前来看Person创建的所有对象属性都是一样的