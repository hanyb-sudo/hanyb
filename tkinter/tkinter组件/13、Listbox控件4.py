import tkinter

win = tkinter.Tk()
win.title("hanyb")
win.geometry("400x400+200+0")

# MULTIPLE  支持多选
lb = tkinter.Listbox(win, selectmode = tkinter.MULTIPLE)
lb.pack()
for item in ["good","nice","handsome","great","perfect","good","nice","handsome","great","perfect","good","nice","handsome","great","perfect"]:
    lb.insert(tkinter.END, item)


win.mainloop()
