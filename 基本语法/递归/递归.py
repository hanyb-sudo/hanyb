#输入一个数（大于等于1），求1+2+···+n的和

# 递归
def func(n):
    if n == 1:
        return 1
    else:
        return n + func(n-1)
while True:
    n=int(input("输入一个大于等于1的数："))
    if n>=1:
        break
print(func(n))