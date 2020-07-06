import tkinter


win = tkinter.Tk()
win.title("hanyb")
win.geometry("400x400+200+0")

'''
输入控件
用于显示简单的文本内容
'''

# 绑定变量
e = tkinter.Variable()
# show 密文显示 show = "*"、
# textvariable 绑定变量
entry = tkinter.Entry(win, textvariable = e)
entry.pack()

# e就代表输入框这个对象
# 设置值
e.set("韩义博你好！")
# 取值
print(e.get())
print(entry.get())#作用与上面一样




win.mainloop()