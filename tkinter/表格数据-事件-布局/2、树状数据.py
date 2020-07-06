import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("hanyb")
win.geometry("400x400+200+0")

tree = ttk.Treeview(win)
tree.pack()

# 添加一级树枝
treeF1 = tree.insert("", 0, "中国", text="China", values="F1")
treeF2 = tree.insert("", 1, "美国", text="USA", values="F2")
treeF3 = tree.insert("", 2, "英国", text="UK", values="F3")

# 添加二级树枝
treeF1_1 = tree.insert(treeF1, 0,"四川", text="四川", values = "F1_1")
treeF1_2 = tree.insert(treeF1, 1,"重庆", text="重庆", values = "F1_2")
treeF1_3 = tree.insert(treeF1, 2,"甘肃", text="甘肃", values = "F1_3")

treeF2_1= tree.insert(treeF2, 0,"纽约", text="NewYork", values = "F2_1")
treeF2_2 = tree.insert(treeF2, 1,"旧金山", text="旧金山", values = "F2_2")
treeF2_3 = tree.insert(treeF2, 2,"洛杉矶", text="LosAngel", values = "F2_3")

# 添加三级树枝
treeF1_1_1 = tree.insert(treeF1_1, 0,"成都", text="成都", values = "F1_1_1")
treeF1_1_2 = tree.insert(treeF1_1, 0,"南充", text="南充", values = "F1_1_2")
treeF1_1_3 = tree.insert(treeF1_1, 0,"德阳", text="德阳", values = "F1_1_3")


win.mainloop()