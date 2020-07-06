# pip install pygame
import time
import pygame

# 音乐路径
filePath = r"韩寒 - 奉献.mp3"

# 初始化
pygame.mixer.init()

# 加载音乐
track = pygame.mixer.music.load(filePath)

# 播放
pygame.mixer.music.play()

# time.sleep(100)#播放多长时间
while True:#一直循环代表一直播放
    pass
# 暂停
# pygame.mixer.music.pause()

# 停止
pygame.mixer.music.stop()
