from person import Person

class Student(Person):
    def __init__(self, name, age, stuId, money):
        # 调用父类中的__init__
        super(Student, self).__init__(name, age, money)
        # 子类可以有一些自己独有的属性
        self.stuId = stuId