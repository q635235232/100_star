from PyPDF2 import PdfFileReader
from io import open, StringIO
from pdfminer.converter import  TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager

def main1():
    with open('./res/Docker入门教程.pdf', 'rb') as f:
        reader = PdfFileReader(f, strict=False)
        print(reader.numPages)
        if reader.isEncrypted:
            reader.decrypt('')
        current_page = reader.getPage(5)
        print(current_page)
        print(current_page.extractText())
