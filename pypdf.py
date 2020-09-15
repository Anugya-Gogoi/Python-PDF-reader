from PyPDF2 import PdfFileReader
file=open('E:\LATEX for Beginners.pdf','rb')
reader=PdfFileReader(file)
print("Printing document info...",(reader.getNumPages()))
print()
print("PDF file created by ",reader.getDocumentInfo().creator)
print("**********************************************")
pages=reader.getNumPages()
for i in range(0,pages):
    print("Page no",i+1)
    pageObj=reader.getPage(i)
    print(pageObj.extractText())

file.close()