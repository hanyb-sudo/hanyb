import tkinter


win = tkinter.Tk()
win.title("hanyb")
win.geometry("400x400+200+0")

# 鼠标绑定
# <Button-1> 鼠标左键
# <Button-2> 鼠标中键
# <Button-3> 鼠标右键
# <Double-Button-1> 双击鼠标左键
# <Triple-Button-1> 三击鼠标左键
def func(event):
    print(event.x,event.y)
button1 = tkinter.Button(win, text="leftmouse button")
# bind  给控件绑定事件
button1.bind("<Button-1>",func)
button1.pack()


win.mainloop()