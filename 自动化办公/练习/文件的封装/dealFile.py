import sys
import importlib
importlib.reload(sys)

from pdfminer.pdfparser import  PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed



class DealFile(object):
    def readPDF(self, path, callback=None, toPath=""):
        # 以二进制形式打开pdf文件
        f = open(path, "rb")

        # 创建一个pdf文档分析器
        parser = PDFParser(f)

        # 创建一个pdf文档
        pdfFile = PDFDocument()

        # 连接分析器和文档对象
        parser.set_document(pdfFile)
        pdfFile.set_parser(parser)

        # 提供初始化密码
        pdfFile.initialize()

        # 检测文档是否提供txt转换
        if not pdfFile.is_extractable:
            raise PDFTextExtractionNotAllowed
        else:
            # 解析数据
            # 数据管理器
            manager = PDFResourceManager()
            # 创建一个PDF设备对象
            laparams = LAParams()
            device = PDFPageAggregator(manager, laparams=laparams)
            # 创建一个PDF解释其对象
            interpreter = PDFPageInterpreter(manager, device)

            # 循环遍历列表，每次处理一个page内容
            # pdfFile.get_pages() 获取page列表
            for page in pdfFile.get_pages():
                interpreter.process_page(page)
                # 接受该页面的LTPage对象
                layout = device.get_result()
                # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象
                # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等
                # 想要获取文本就获得对象的text属性，
                for x in layout:
                    # 判断类型isinstance()x是LTTextBoxHorizontal类型
                    if (isinstance(x, LTTextBoxHorizontal)):
                        if toPath != "":
                            with open(r'pdf.txt', 'a', encoding='utf-8') as f:
                                str = x.get_text()
                                # print(str)
                                f.write(str + "\n")
                        else:
                            str = x.get_text()
                            if callback == None:
                                print(str)
                            else:
                                callback(str)
