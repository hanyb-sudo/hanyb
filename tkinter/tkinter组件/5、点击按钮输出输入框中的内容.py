import tkinter

def printInfo():
    # 通过entry显示
    print(entry.get())
win = tkinter.Tk()
win.title("hanyb")
win.geometry("400x400+200+0")

entry = tkinter.Entry(win)
entry.pack()

button2 = tkinter.Button(win,text = "按钮", command = printInfo)
button2.pack()


win.mainloop()