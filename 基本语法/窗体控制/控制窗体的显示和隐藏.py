import win32con
import win32gui
import time


# 找处窗体的编号
qqWin = win32gui.FindWindow("TXGuiFoundation","QQ")
while True:
    # 显示窗体
    win32gui.ShowWindow(qqWin,win32con.SW_HIDE)

    time.sleep(1)
    win32gui.ShowWindow(qqWin,win32con.SW_SHOW)
    time.sleep(1)