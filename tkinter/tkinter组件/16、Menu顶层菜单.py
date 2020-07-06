import tkinter


win = tkinter.Tk()
win.title("hanyb")
win.geometry("400x400+200+0")

# 菜单条
menubar = tkinter.Menu(win)
win.config(menu=menubar)

# 创建一个菜单选项
menu1 = tkinter.Menu(menubar, tearoff=False)
# 给菜单选项添加内容
for item in ["Python","R","C","C++","Java","shell","c#","JS","PHP","汇编","NodeJS","quit"]:
    if item =="quit":
        # 添加一个分隔线
        menu1.add_separator()
        menu1.add_command(label=item, command=win.quit)
    else:
        menu1.add_command(label=item)

# 向菜单条上添加菜单选项
menubar.add_cascade(label="语言", menu=menu1)

# 再创建一个菜单
menu2 = tkinter.Menu(menubar, tearoff=False)
menu2.add_command(label="red")
menu2.add_command(label="white")
menu2.add_command(label="black")
menubar.add_cascade(label="color", menu=menu2)

win.mainloop()