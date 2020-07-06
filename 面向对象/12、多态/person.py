from animal import Animal
class Person(object):
    # def feedCat(self,cat):
    #     print("给你食物")
    #     cat.eat()
    #
    # def feedMouse(self,mouse):
    #     print("给你食物")
    #     mouse.eat()

    # 多态
    def feedAnimal(self, animal):
        print("给你食物")
        animal.eat()

    def eat(self):
        print("人要吃东西了！！")