import win32com
import win32com.client


def makePPT(path):
    ppt = win32com.client.Dispatch("PowerPoint.Application")
    ppt.Visible = True

    #增加一个文件
    pptFile = ppt.Presentations.Add()

    #创建第一页
    page1 = pptFile.Slides.Add(1, 1)  #参数1为页数，从1开始 ，参数2 为ppt主题框的类型
    t1 = page1.Shapes[0].TextFrame.TextRange
    t1.Text = "hanyb"
    t1 = page1.Shapes[1].TextFrame.TextRange
    t1.Text = "is a good boy！"

    page2 = pptFile.Slides.Add(2, 1)  # 参数1为页数，从1开始 ，参数2 为ppt主题框的类型
    t2 = page2.Shapes[0].TextFrame.TextRange
    t2.Text = "hanyb"
    t2 = page2.Shapes[1].TextFrame.TextRange
    t2.Text = "is a good boy！"

    page3 = pptFile.Slides.Add(3, 3)  # 参数1为页数，从1开始 ，参数2 为ppt主题框的类型


    #保存
    pptFile.SaveAs(path)
    pptFile.Close()
    ppt.Quit()



path = r"C:\Users\Lenovo\Desktop\b.pptx"
makePPT(path)