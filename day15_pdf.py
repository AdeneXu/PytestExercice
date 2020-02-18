"""
读取PDF文件
"""

import PyPDF2
from PyPDF2 import PdfFileReader

with open('D:/document/鸟哥的Linux私房菜 基础学习篇(第三版).pdf','rb') as f:
    reader = PdfFileReader(f,strict=False)
    print(reader.numPages)
    if reader.isEncrypted:
        reader.decrypt('')
    current_page = reader.getPage(15)
    print(current_page)
    print('---------------')
    print(current_page.extractText())