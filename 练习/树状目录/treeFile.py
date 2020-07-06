import tkinter
from tkinter import ttk
import os
from treeWindows import TreeWindows
from infoWindows import InfoWindows

win = tkinter.Tk()
win.title("树状目录")
win.geometry("900x400+200+0")


path = r"C:\Users\Lenovo\Desktop\python学习（公司）"

infoWin = InfoWindows(win)
treeWin = TreeWindows(win, path, infoWin)



win.mainloop()