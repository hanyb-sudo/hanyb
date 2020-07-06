import tkinter

def update():
    message = ""
    if hobby1.get() == True:
        message+="money\n"
    if hobby2.get() == True:
        message+="poswer\n"
    if hobby3.get() == True:
        message+="people\n"
        
    #清空text的所有内容
    text.delete(0.0, tkinter.END)
    text.insert(tkinter.INSERT, message)


win = tkinter.Tk()
win.title("hanyb")
win.geometry("400x400+200+0")

hobby1 = tkinter.BooleanVar()
check1 = tkinter.Checkbutton(win, text = "money", variable = hobby1, command = update)
check1.pack()
hobby2 = tkinter.BooleanVar()
check2 = tkinter.Checkbutton(win, text = "power", variable = hobby2, command = update)
check2.pack()
hobby3 = tkinter.BooleanVar()
check3 = tkinter.Checkbutton(win, text = "people", variable = hobby3, command = update)
check3.pack()

text = tkinter.Text(win, width = 40, height = 6)
text.pack()

win.mainloop()