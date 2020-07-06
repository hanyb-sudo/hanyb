import tkinter

win = tkinter.Tk()
win.title("hanyb")
win.geometry("400x400+200+0")

'''
文本控件，用于显示多行文本
'''

text = tkinter.Text(win, width = 30, height = 4)
text.pack()

str = '''Today, I was so excited to buy a new pair of shoes, 
because I have saved the money for a month. In order to get enough money, 
I controlled myself to eat less snacks. What’s more, 
I helped my mother to do her housework to get more pocket money.
 When I get the new shoes, I was so proud of myself. 
 I realized a small goal.'''

text.insert(tkinter.INSERT, str)




win.mainloop()