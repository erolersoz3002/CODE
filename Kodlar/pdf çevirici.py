from pdf2docx import Converter

pdf_path="ornek.pdf"
docx_pdf="ornek.docx"
cv =Converter(pdf_file=pdf_path)
cv.convert(docx_filename=docx_pdf)
cv.close()