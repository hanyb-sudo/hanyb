import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("hanyb")
win.geometry("400x400+200+0")

# 表格
tree = ttk.Treeview(win)
tree.pack()

# 定义列
tree['columns'] = ("姓名","年龄","身高","体重")
# 设置列,列还不显示
tree.column("姓名", width=50)
tree.column("年龄", width=50)
tree.column("身高", width=50)
tree.column("体重", width=50)

# 设置表头
tree.heading("姓名", text="姓名")
tree.heading("年龄", text="年龄")
tree.heading("身高", text="身高")
tree.heading("体重", text="体重")

# 添加数据
tree.insert("", 0, text="line1", values=("韩义博","23","170","60"))
tree.insert("", 1, text="line2", values=("韩义博","23","170","60"))


win.mainloop()