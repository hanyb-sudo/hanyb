import tkinter


win = tkinter.Tk()
win.title("hanyb")
win.geometry("400x400+200+0")

label = tkinter.Label(win, text = "you are a good man!")

# 设置焦点
label.focus_set()
label.pack()

# a 指定按键，直接写指定按键名
def func(event):
    print("event.char=",event.char)
    print("event.keycode=", event.keycode)
label.bind("a",func)


win.mainloop()