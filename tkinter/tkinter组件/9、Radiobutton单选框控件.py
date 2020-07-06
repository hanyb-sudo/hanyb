import tkinter

def update():
    print(r.get())

win = tkinter.Tk()
win.title("hanyb")
win.geometry("400x400+200+0")

# 一组单选框要绑定同一个变量
r = tkinter.IntVar()
radio1 = tkinter.Radiobutton(win, text = "male", value = 1, variable = r, command = update)
radio1.pack()
radio2 = tkinter.Radiobutton(win, text = "female", value = 2, variable = r, command = update)
radio2.pack()

win.mainloop()