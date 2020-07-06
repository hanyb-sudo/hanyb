import tkinter
import os
from tkinter import ttk

class TreeWindows(tkinter.Frame):
    def __init__(self, master, path, infoWin):
        self.infoWin = infoWin
        frame = tkinter.Frame(master)
        frame.grid(row = 0, column = 0)

        self.tree = ttk.Treeview(frame)
        self.tree.pack(side = tkinter.LEFT, fill = tkinter.Y)
        valuePath = path.replace('\\','$')
        root = self.tree.insert("","end",text=self.getLastPath(path), values=valuePath)
        self.loadTree(root, path)

    #     添加滚动条
        self.scroll = tkinter.Scrollbar(frame)
        self.scroll.pack(side = tkinter.RIGHT, fill = tkinter.Y)
        self.scroll.config(command=self.tree.yview)
        self.tree.config(yscrollcommand= self.scroll.set)

        #绑定事件
        self.tree.bind("<<TreeviewSelect>>",self.func)

    def func(self, event):
        self.v = event.widget.selection()
        for sv in self.v:
            file = self.tree.item(sv)['text']
            self.infoWin.ev.set(file)
            absPath = self.tree.item(sv)['values'][0].replace('$','\\')
            print(absPath)
            # 每一次点击都清空Text
            self.infoWin.txt.delete(1.0, "end")
            if absPath.endswith(".py") or absPath.endswith(".txt"):
                #打开.py文件，并加入到Text中
                self.open_Insert(absPath)



    def open_Insert(self, absPath):
        with open(absPath, "r", encoding='utf-8') as f:
            str = f.read()
            self.infoWin.txt.insert(tkinter.INSERT, str)


    def getLastPath(self, path):
        pathList = os.path.split(path)
        return pathList[-1]


    def loadTree(self, parent, parentPath):
        fileList = os.listdir(parentPath)
        for i, fileName in enumerate(fileList):
            # 绝对路径
            # print(i,file)
            absPath = os.path.join(parentPath, fileName)
            if os.path.isdir(absPath):
                # print(file)
                valuePath = absPath.replace('\\', '$')
                treeB = self.tree.insert(parent, "end", text=fileName, values=valuePath)
                # 递归调用
                self.loadTree(treeB, absPath)
            else:
                # print(file)
                valuePath = absPath.replace('\\', '$')
                leaf = self.tree.insert(parent, i, text=fileName, values=valuePath)