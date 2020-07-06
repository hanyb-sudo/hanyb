import tkinter


win = tkinter.Tk()
win.title("hanyb")
win.geometry("400x400+200+0")

# 菜单条
menubar = tkinter.Menu(win)
# 菜单
menu = tkinter.Menu(menubar, tearoff=False)
for item in ["Python","R","C","C++","Java","shell","c#","JS","PHP","汇编","NodeJS","quit"]:
    menu.add_command(label=item)
menubar.add_cascade(label="语言", menu=menu)

def showMenu(event):
    menubar.post(event.x_root, event.y_root)
win.bind("<Button-3>", showMenu)


win.mainloop()