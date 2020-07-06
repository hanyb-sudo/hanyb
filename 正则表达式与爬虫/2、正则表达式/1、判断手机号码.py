'''
给你一串字符串，判断是否是手机号码

'''
import re

def checkPhone(str):
    if len(str) != 11:
        return False
    elif str[0] != "1":
        return False
    for i in str:
        if i < '0' or i > '9':
            return False

    return True


def checkPhone2(str):
    if re.match("(^1[34578]\d{9})$", str) != None:
        return True
    return False

# print(checkPhone("13540598422"))
# print(checkPhone2("13540598482"))

# QQ
def QQ(str):
    pat = "^[1-9]\d{5,9}$"
    re_QQ = re.compile(pat)
    if re_QQ.match(str) != None:
        return True
    return False

print(QQ("21230"))
