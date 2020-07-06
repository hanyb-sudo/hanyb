import tkinter


win = tkinter.Tk()
win.title("hanyb")
win.geometry("400x400+200+0")

label1 = tkinter.Label(win, text="good", bg="blue")
label2 = tkinter.Label(win, text="nice", bg="pink")
label3 = tkinter.Label(win, text="perfect", bg="red")
label4 = tkinter.Label(win, text="hello", bg="yellow")

# 表格布局
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)
label4.grid(row=1, column=1)




win.mainloop()