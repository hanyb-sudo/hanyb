import tkinter

win = tkinter.Tk()
win.title("hanyb")
# win.geometry("400x400+200+0")

# EXTENDED  可以使listbox支持shift和control
lb = tkinter.Listbox(win, selectmode = tkinter.EXTENDED)
lb.pack()
for item in ["good","nice","handsome","great","perfect","good","nice","handsome","great","perfect","good","nice","handsome","great","perfect"]:
    lb.insert(tkinter.END, item)

# 按住shift，可以实现连选
# 按住control，可以实现多选

# 滚动条
sc = tkinter.Scrollbar(win)
sc.pack(side=tkinter.RIGHT, fill =tkinter.Y )
lb.configure(yscrollcommand=sc.set)
lb.pack(side=tkinter.LEFT, fill=tkinter.BOTH)

# 额外给属性赋值
# sc['command'] = lb.yview
sc.config(command = lb.yview)

win.mainloop()