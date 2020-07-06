import tkinter


win = tkinter.Tk()
win.title("hanyb")
win.geometry("400x400+200+0")


label = tkinter.Label(win, text="you are a good man!")
label.pack()

# <Enter> 鼠标光标进入事件
# <Leave> 鼠标光标离开事件
def func(event):
    print(event.x,event.y)
label.bind("<Leave>",func)

win.mainloop()