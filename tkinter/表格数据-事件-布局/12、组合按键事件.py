import tkinter


win = tkinter.Tk()
win.title("hanyb")
win.geometry("400x400+200+0")

label = tkinter.Label(win, text = "you are a good man!")

# 设置焦点
label.focus_set()
label.pack()

# <Shift-Up>  Shift+Up
# <Alt-Up>    Alt+Up
# <Control-Up>  Ctrl+Up
# <Control-A>   Ctrl+shift+a
def func(event):
    print("event.char=",event.char)
    print("event.keycode=", event.keycode)
label.bind("<Control-A>",func)


win.mainloop()