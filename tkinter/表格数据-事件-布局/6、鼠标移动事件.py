import tkinter


win = tkinter.Tk()
win.title("hanyb")
win.geometry("400x400+200+0")

label = tkinter.Label(win, text="you are a good man!")
label.pack()

# <B1-Motion> 鼠标左键移动
# <B2-Motion> 鼠标中键移动
# <B3-Motion> 鼠标右键移动
def func(event):
    print(event.x,event.y)
label.bind("<B1-Motion>",func)



win.mainloop()