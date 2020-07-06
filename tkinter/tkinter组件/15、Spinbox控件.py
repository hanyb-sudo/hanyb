import tkinter


win = tkinter.Tk()
win.title("hanyb")
win.geometry("400x400+200+0")

def update():
    print(v.get())
'''
数值范围控件
'''
# 绑定变量
v = tkinter.StringVar()
# increment  步长，默认为1
# values 最好不要与from_=, to=,increment=同时使用  values = (0,2,4,6,8))
# command 只要值改变就会执行对应的方法
sp = tkinter.Spinbox(win, from_=0, to=100,increment=5, textvariable = v, command =update)
                     # values = (0,2,4,6,8))
sp.pack()

# 赋值
v.set(30)
# 取值
# print(v.get())


win.mainloop()