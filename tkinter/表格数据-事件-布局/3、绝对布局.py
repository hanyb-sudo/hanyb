import tkinter


win = tkinter.Tk()
win.title("hanyb")
win.geometry("400x400+200+0")

label1 = tkinter.Label(win, text="good", bg="blue")
label2 = tkinter.Label(win, text="nice", bg="pink")
label3 = tkinter.Label(win, text="perfect", bg="red")

# 绝对布局
label1.place(x=10,y=10)
label2.place(x=40,y=40)
label3.place(x=70,y=70)



win.mainloop()