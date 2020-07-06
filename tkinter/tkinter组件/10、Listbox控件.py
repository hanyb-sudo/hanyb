import tkinter


win = tkinter.Tk()
win.title("hanyb")
win.geometry("400x400+200+0")

'''
列表框控件，可以包含一个或者多个文本框
作用：在listbox控件的小窗口显示一个字符串
'''

# 创建一个listbox，添加几个元素
lb = tkinter.Listbox(win, selectmode = tkinter.BROWSE)
lb.pack()
for item in ["good","nice","handsome"]:
    # 按顺序添加
    lb.insert(tkinter.END, item)
# 在开始添加
lb.insert(tkinter.ACTIVE, "cool")
# 将列表当成一个元素进行添加
# lb.insert(tkinter.END, ["perfect","fantastic"])

# 删除  参数1未开始的索引，参数2为结束的索引，如果不指定参数2，只删除第一个索引出的内容
# lb.delete(1,2)

# 选中  参数1未开始的索引，参数2为结束的索引，如果不指定参数2，只选中第一个索引出的内容
# lb.select_set(0,2)
lb.select_set(0,2)

# 取消选中
# lb.select_clear(0,1)
# lb.select_clear(1)

# 获取列表中的元素个数
print(lb.size())

# 从列表中取值  参数1未开始的索引，参数2为结束的索引，如果不指定参数2，只获取第一个索引出的内容
print(lb.get(0,2))
print(lb.get(2))

#  返回当前选中的索引项
print(lb.curselection())

# 判断一个选项是否被选中
print(lb.select_includes(1))

win.mainloop()