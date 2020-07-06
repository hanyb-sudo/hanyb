import tkinter


win = tkinter.Tk()
win.title("hanyb")
win.geometry("400x400+200+0")
'''
label = tkinter.Label(win, text = "you are a good man!")

# 设置焦点 只有给小控件添加键盘事件时才会设置焦点
label.focus_set()
label.pack()

# <Key> 响应所有的按键
def func(event):
    print("event.char=",event.char)
    print("event.keycode=", event.keycode)
label.bind("<Key>",func)
'''

# win绑定键盘事件不用设置焦点
def func(event):
    print("event.char=",event.char)
    print("event.keycode=", event.keycode)
win.bind("<Key>",func)

win.mainloop()