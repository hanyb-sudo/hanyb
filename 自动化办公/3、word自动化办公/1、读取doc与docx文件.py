# Python 有针对 .docx 后缀文件的第三方库如 python-docx、pydocx等等，
# 但是没有针对 .doc 和 .wps 的第三方库，所以这里就只能使用 win32com 模块。

import win32com
import win32com.client

def readWordFile(path):
    # 调用系统word功能，可以处理doc和docx两种文件
    mw = win32com.client.Dispatch("Word.Application")
    #打开文件
    # mw.Visible = 0  # 后台  运行
    # mw.DisplayAlerts = 0  # 不显示，不警告
    # 如果不声明上述属性，运行的时候会显示的打开office软件操作文档
    doc = mw.Documents.Open(path)
    for paragraph in doc.Paragraphs:
        line = paragraph.Range.Text
        print(line)


    #关闭文件
    doc.Close()
    #退出word
    mw.Quit()


path = r"C:\Users\Lenovo\Desktop\毕业论文\论文\201607020213-韩义博 《毕业论文指导论文过程》.doc"
readWordFile(path)