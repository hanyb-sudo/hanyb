import tkinter
from tkinter import ttk


win = tkinter.Tk()
win.title("hanyb")
win.geometry("400x400+200+0")

# 绑定变量
cv = tkinter.StringVar()
com = ttk.Combobox(win, textvariable = cv)
com.pack()

# 设置下拉控件
com['value'] = ('成都','南充','绵阳','泸州','德阳','凉山州','阿坝州')

# 设置默认值
com.current(0)

def func(event):
    print(com.get())
    print(cv.get())
# 绑定事件
com.bind("<<ComboboxSelected>>",func)



win.mainloop()