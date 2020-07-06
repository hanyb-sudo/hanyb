import tkinter


win = tkinter.Tk()
win.title("hanyb")
win.geometry("400x400+200+0")


label1 = tkinter.Label(win, text="good", bg="blue")
label2 = tkinter.Label(win, text="nice", bg="pink")
label3 = tkinter.Label(win, text="perfect", bg="red")

# 相对布局
# tkinter.BOTH
label1.pack(fill=tkinter.BOTH, side=tkinter.TOP)
label2.pack(fill=tkinter.Y, side=tkinter.RIGHT)
label3.pack()

win.mainloop()