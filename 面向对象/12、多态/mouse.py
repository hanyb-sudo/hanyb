from animal import Animal

class Mouse(Animal):
    def __init__(self, name):
        super(Mouse, self).__init__(name)# 也可以写为super().__init__(name)