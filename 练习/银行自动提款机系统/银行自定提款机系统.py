'''
人
类名：Person
属性：姓名  身份证号  电话号  卡
行为：


卡
类名：Card
属性：卡号  密码  余额
行为：


提款机
类名：ATM
属性：
行为：1、开户 2、查询 3、存储 4、转账 5、改密 6、锁定 7、解锁 8、补卡 9、销户 10、退出 11、取款


界面
类名：View
属性：
行为：管理员界面   系统功能界面  管理员登录


银行
类名：Bank
属性：用户列表  提款机
'''

from view import View
import time
from atm import ATM
import pickle
import os
#389383
def main():
    # 创建窗口对象
    view = View()
    #创建atm对象
    filePath = os.path.join(os.getcwd(), "practice.txt")
    if os.path.isfile(filePath):
        with open(filePath, "rb") as f:
            allUsers = pickle.load(f)
    else:
        allUsers={}
    atm = ATM(allUsers)
    if view.printAdminView():
        return 1

    while True:
        view.sysFuncView()
        #等待用户操作
        option = input("请输入您的操作：")
        if option =="open":
            atm.createUser()
            # 开户
        elif option =="search":
            atm.searchUserInfo()
        elif option =="withdrawal":
            pass
        elif option =="deposit":
            pass
        elif option =="tranfer":
            pass
        elif option =="change":
            pass
        elif option =="lock":
            atm.lockUser()
        elif option =="unlock":
            atm.unLockUser()
        elif option =="reissue":
            pass
        elif option =="close":
            pass
        elif option == "quit":
            filePath = os.path.join(os.getcwd(), "practice.txt")
            with open(filePath, "wb") as f:
                pickle.dump(atm.allUser, f)
            return 1
        time.sleep(2)





if __name__ == '__main__':
    main()

