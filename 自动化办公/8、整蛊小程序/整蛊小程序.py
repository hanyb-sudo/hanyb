import win32api
import win32con
import win32gui
import time
import pygame
import threading

def go():

    pygame.mixer.init()
    while True:
        for item in range(2):
            track = pygame.mixer.music.load(str(item)+".mp3")
            # print(item)
            pygame.mixer.music.play()
            time.sleep(10)
            pygame.mixer.music.stop()


def setWallPaper():
    for item in range(5):
        # 打开注册表
        reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
        path = str(item)+".jpg"
        print(path)
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, win32con.SPIF_SENDCHANGE)
        time.sleep(3)

# th = threading.Thread(target=go, name="LoopThread")
# th.start()
while True:
    setWallPaper()