'''
多态：一种事物，多种形态

最终目标：人可以喂任何一种动物
'''
from mouse import Mouse
from cat import Cat
from person import Person

tom = Cat("tom")

jerry = Mouse("jerry")

# tom.eat()
# jerry.eat()


# 定义一个人类，可以喂猫和老鼠吃东西
per = Person()
# tom和jerry都能喂，因为tom和jerry都继承自动物
per.feedAnimal(tom)
