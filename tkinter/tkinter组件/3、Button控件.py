import tkinter

def func():
    print("Hello!")
win = tkinter.Tk()
win.title("hanyb")
win.geometry("400x400+200+0")

button1 = tkinter.Button(win,text = "按钮", command = func,
                        width = 10,
                        height = 10)
button1.pack()
button2 = tkinter.Button(win,text = "退出", command = win.quit)
button2.pack()






win.mainloop()