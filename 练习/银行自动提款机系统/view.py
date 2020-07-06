import time

class View(object):

    dictAcount = {1:1,2:2}


    def printAdminView(self):
        print("*********************************************************************")
        print("*                                                                   *")
        print("*                      Welcome to the Bank!                         *")
        print("*                                                                   *")
        print("*                                                                   *")
        print("*                                                                   *")
        print("*                                                                   *")
        print("*                                                                   *")
        print("*                                                                   *")
        print("*********************************************************************")

        inputAdmin = int(input("账号："))
        inputPasswd = int(input("密码："))
        if inputAdmin in self.dictAcount :
            if inputPasswd == self.dictAcount.get(inputAdmin):
                print("登陆成功！请稍候....")
                time.sleep(3)
                return 0
        else:
            print("账号或者密码输入有误！")
            return 1


    def sysFuncView(self):
        print("*********************************************************************")
        print("*             开户(open)                查询(search)                *")
        print("*             取款(withdrawal)          存款(deposit)               *")
        print("*             转账(tranfer)             改密(change)                *")
        print("*             锁定(lock)                解锁(unlock)                *")
        print("*             补卡(reissue)             销户(close)                 *")
        print("*                           退出（quit）                            *")
        print("*                                                                   *")
        print("*                                                                   *")
        print("*********************************************************************")

