import win32com
import win32com.client
import time

def readWordFileToOtherFile(path, toPath):
    # 调用系统word功能，可以处理doc和docx两种文件
    mw = win32com.client.Dispatch("Word.Application")
    #打开文件
    doc = mw.Documents.Open(path)
    doc.SaveAs(toPath, 2)      #2表示为txt文件

    doc.Close()
    #退出word
    mw.Quit()



path1 = r"C:\Users\Lenovo\Desktop\毕业论文\论文\201607020213-韩义博 《毕业论文指导论文过程》.doc"

toPath = r"C:\Users\Lenovo\Desktop\毕业论文\论文\a.txt"
readWordFileToOtherFile(path1, toPath)