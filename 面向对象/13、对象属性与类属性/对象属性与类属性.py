
class Person(object):

    # 这里的属性实质上属于类属性(用类名来调用)
    name = "person"
    def __init__(self, name):
        # 对象属性
        self.name = name
        pass


print(Person.name)
per = Person("tom")
# per.name = "han"
# 对象属性的优先级是高于类属性的，同名时没有对象属性会使用类属性
print(per.name)
# 动态的给对象添加对象属性，只针对当前对象生效，对于类创建的其他对象没有作用
per.age = 20
print(Person.name)

# 删除对象中的name属性，在调用会使用到同名的类属性
del per.name
print(per.name)

# 注意：以后千万不要将对象属性与类属性重名，因为对象属性会屏蔽类属性。但是当删除对象属性时，在使用又能使用类属性。