from person import Person
from student import Student
from worker import Worker

per = Person("1", 20, 3000)

stu = Student("Han", 23,201607020213, 1000 )
# print(stu.__money)私有属性
print(stu.getMoney())#通过继承过来的公有方法访问私有属性
# 或者通过以下方法名访问
# print(stu._Person__money)

wor = Worker("Yan", 22, 2000)
# print(wor)
wor.setMoney(20000)


print(per.getMoney())
