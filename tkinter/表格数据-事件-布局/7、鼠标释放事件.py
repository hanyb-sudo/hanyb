import tkinter


win = tkinter.Tk()
win.title("hanyb")
win.geometry("400x400+200+0")

# <ButtonRelease-1>  鼠标左键释放
# <ButtonRelease-2>  鼠标中键释放
# <ButtonRelease-3>  鼠标右键释放

label = tkinter.Label(win, text="you are a good man!")
label.pack()

def func(event):
    print(event.x,event.y)
label.bind("<ButtonRelease-1>",func)

win.mainloop()