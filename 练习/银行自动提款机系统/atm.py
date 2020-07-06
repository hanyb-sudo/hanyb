import random
from user import User
from card import Card

class ATM(object):
    def __init__(self, allUsers):
        self.allUser = allUsers     #卡号-用户

    #开户
    def createUser(self):
# 目标：向用户自字典中添加一对键值对(卡号-用户)
        name = input("请输入您的姓名：")
        idCard = input("请输入您的身份证号码：")
        phoneNumber = input("请输入您的电话号码：")
        prestoreMoney = int(input("请输入预存款金额："))
        if prestoreMoney < 0 :
            print("预存款输入有误！开户失败！")
            return 1

        cardPasswd = input("请设置密码：")
        self.checkPasswd(cardPasswd)
        #随机生成卡号
        cardId = self.randomCardId()

    #     创建用户
        card = Card(cardId, cardPasswd, prestoreMoney)
        user = User(name, idCard, phoneNumber, card)
    #     存到字典中
        self.allUser[cardId] = user
        # print(self.allUser)
        print("开户成功！")
        print("您的卡号为：",cardId)


    def checkPasswd(self, realPasswd):
        for i in range(3):
            tempPasswd = input("请输入密码：")
            if tempPasswd == realPasswd:
                return True
        return False

    def randomCardId(self):
        while True:
            str = ""
            for i in range(6):
                ch = chr(random.randrange(ord('0'), ord('9') + 1))
                str  += ch

            #判断是否重复
            if str not in self.allUser:
                return str

    def searchUserInfo(self):
        cardNum = input("请输入您的卡号：")
        user = self.allUser.get(cardNum)
        if cardNum not in self.allUser:
            print("卡号不存在！")
            return 0

        # 判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定！！请解锁后再进行其他操作！")
            return 0


        print("您的卡号为：",cardNum)

        print("您的余额为:",user.card.cardMoney)
        return 1

    def lockUser(self):
        cardNum = input("请输入您的卡号：")
#         验证卡号是否存在
        user = self.allUser.get(cardNum)
        if not user:
            print("卡号不存在！！锁定失败！")
            return 0

        if user.card.cardLock:
            print("该卡已被锁定！！请解锁后再使用其它功能！")
            return 0

#         锁卡
        user.card.cardLock = True
        print("锁定成功！")

    #解锁
    def unLockUser(self):
        cardNum = input("请输入您的卡号：")
        #         验证卡号是否存在
        user = self.allUser.get(cardNum)
        if not user:
            print("卡号不存在！！解锁失败！")
            return 0

        if not user.card.cardLock:
            print("该卡未锁定！！")
            return 0
        user.card.cardLock = False
        print("解锁成功！")



