#人开枪射击子弹

class Person(object):
    def __init__(self, Gun):
        self.Gun = Gun
    def fire(self):
        print("fire....")
        self.Gun.unloading(1)

    def loadBullet(self,number):
        print("loading",number,"bullets!")
        self.Gun.loading(number)


class Gun(object):
    def __init__(self, Bullet):
        self.Bullet = Bullet

    def loading(self,number):
        if self.Bullet.number <= 30:
            self.Bullet.number+=number
        else:
            print("bullet is full!")
    def unloading(self, number):
        if self.Bullet.number > 0:
            self.Bullet.number-=number
        else:
            print("bullet is empty!")

class Bullet(object):
    def __init__(self, number):
        self.number = number


bull = Bullet(10)
gun = Gun(bull)
per = Person(gun)
# for i in range(11):
#     per.fire()
#     print(bull.number)
per.loadBullet(20)
print(bull.number)