"""
PDF Watermarker
This automation script will simply help you Watermark your PDF page by page. 
This script uses the PyPDF4 module to read and add watermark. 
Check out the code below:
    
"""  

# Watermark PDF files
# pip install PyPDF4
import PyPDF4

def Watermark():
    pdf_file= "test.pdf"
    output_pdf= "output.pdf"
    watermark= "watermark.pdf"
    
watermark_read = PyPDF4.PdfFileReader(watermark)
watermark_page = watermark_read.getPage(0)
pdf_reader = PyPDF4.PdfFileReader(pdf_file)
pdf_writer = PyPDF4.PdfFileWriter()
for page in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(page)
    page.mergePage(watermark_page)
    pdf_writer.addPage(page)
    
# writing output pdf file
with open(output_pdf, 'wb') as pdf:
    pdf_writer.write(pdf)
Watermark()
