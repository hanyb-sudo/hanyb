import win32con
import win32gui
import random
import time
import math

qqWin = win32gui.FindWindow("TXGuiFoundation","QQ")

# 参数1：控制的窗体
# 参数2：大致方位,HWND_TOPMOST上方
# 参数3：位置x
# 参数4：位置y
# 参数5：长度
# 参数6：宽度
while True:
    x=random.choice(range(1000))
    y=random.choice(range(500))
    time.sleep(0.1)
    win32gui.SetWindowPos(qqWin,win32con.HWND_TOPMOST,x,y,200,300,win32con.SWP_SHOWWINDOW)
    


# 用while循环走圆形
'''
r = 1
rr = r * r
i = r
while i >= -r :
    j = -r
    while j <= r:
        if(abs(j) == int(math.sqrt(rr - i * i))):
            print("* ",end='')
        else :
            print("  ",end='')
        j+=1
    i-=1
    print()
'''