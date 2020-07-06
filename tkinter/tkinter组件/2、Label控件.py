import tkinter


# 创建主窗口
win = tkinter.Tk()
win.title("hanyb")
win.geometry("400x400+200+0")

'''
Label：标签控件可以显示文本
'''
# win  父窗体
# bg 背景色
# fg 字体颜色
# font 字体和大小
# width，height 高度和宽度
# wraplength 指定文本中多宽进行换行
# justify 设置换行后的对齐方式
# anchor 位置 n s e w代表4个方向center代表居中
label = tkinter.Label(win, text = "hanyb",
                      bg = "black",
                      fg = "white",
                      font = ("黑体",20),
                      width = 10,height = 10,
                      wraplength = 100,
                      justify = "left",
                      anchor = "s")

# 显示出来
label.pack()



win.mainloop()