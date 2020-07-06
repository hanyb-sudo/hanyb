import tkinter
import os
from tkinter import ttk

class InfoWindows(tkinter.Frame):
    def __init__(self, master):
        self.frame = tkinter.Frame(master)
        self.frame.grid(row = 0, column = 1)

        # 绑定变量
        self.ev = tkinter.Variable()
        self.entry = tkinter.Entry(self.frame, textvariable = self.ev)
        self.entry.pack()

        self.txt = tkinter.Text(self.frame)
        self.txt.pack(side=tkinter.LEFT, fill=tkinter.Y)

        # 给txt添加滚动条
        self.scroll = tkinter.Scrollbar(self.frame)
        self.scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.scroll.config(command=self.txt.yview)
        self.txt.config(yscrollcommand=self.scroll.set)